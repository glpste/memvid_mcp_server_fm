"""
File Management API client wrapper.

Provides high-level interface for uploading and managing video memory files.
"""

import asyncio
import json
import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

import httpx

from .fm_auth import FMAuthManager
from .fm_config import FMConfig

logger = logging.getLogger(__name__)


class FMClient:
    """Client for interacting with the File Management API."""

    def __init__(self, config: FMConfig, auth_manager: FMAuthManager):
        self.config = config
        self.auth_manager = auth_manager
        self._http_client: Optional[httpx.AsyncClient] = None

    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create the async HTTP client."""
        if self._http_client is None:
            self._http_client = httpx.AsyncClient(
                base_url=self.config.api_base_url,
                timeout=300.0,  # 5 minutes for large file uploads
            )
        return self._http_client

    async def close(self) -> None:
        """Close the HTTP client."""
        if self._http_client is not None:
            await self._http_client.aclose()
            self._http_client = None

    async def upload_video_memory(
        self,
        video_path: str,
        index_path: str,
        project_name: Optional[str] = None,
    ) -> tuple[Optional[str], Optional[str]]:
        """
        Upload video memory files (MP4 and JSON) to the File Management API.

        Args:
            video_path: Path to the video file (.mp4)
            index_path: Path to the index file (.json)
            project_name: Optional project name for organization

        Returns:
            tuple: (video_document_id, index_document_id) or (None, None) on failure
        """
        try:
            # Validate files exist
            if not os.path.exists(video_path):
                logger.error(f"Video file not found: {video_path}")
                return None, None
            if not os.path.exists(index_path):
                logger.error(f"Index file not found: {index_path}")
                return None, None

            # Determine project name from filename if not provided
            if project_name is None:
                project_name = Path(video_path).stem.replace("_memory", "")

            # Get authentication headers
            auth_headers = self.auth_manager.get_auth_header()

            # Upload video file
            logger.info(f"Uploading video memory for project '{project_name}'...")
            video_doc_id = await self._upload_file(
                file_path=video_path,
                title=f"{project_name} - Video Memory",
                description=f"Video memory file for project {project_name}",
                auth_headers=auth_headers,
                project_name=project_name,
                file_type="video",
            )

            if video_doc_id is None:
                logger.error("Failed to upload video file")
                return None, None

            # Upload index file
            index_doc_id = await self._upload_file(
                file_path=index_path,
                title=f"{project_name} - Video Memory Index",
                description=f"Video memory index file for project {project_name}",
                auth_headers=auth_headers,
                project_name=project_name,
                file_type="index",
                related_video_id=video_doc_id,
            )

            if index_doc_id is None:
                logger.error("Failed to upload index file")
                return video_doc_id, None

            logger.info(
                f"Successfully uploaded video memory: video={video_doc_id}, index={index_doc_id}"
            )
            return video_doc_id, index_doc_id

        except Exception as e:
            logger.error(f"Error uploading video memory: {e}", exc_info=True)
            return None, None

    async def _upload_file(
        self,
        file_path: str,
        title: str,
        description: str,
        auth_headers: dict,
        project_name: str,
        file_type: str,
        related_video_id: Optional[str] = None,
    ) -> Optional[str]:
        """
        Upload a single file to the File Management API.

        Args:
            file_path: Path to the file to upload
            title: Document title
            description: Document description
            auth_headers: Authentication headers
            project_name: Project name for metadata
            file_type: Type of file (video or index)
            related_video_id: ID of related video document (for index files)

        Returns:
            Document ID on success, None on failure
        """
        try:
            client = await self._get_client()

            # Prepare document metadata
            meta_info = {
                "project_name": project_name,
                "file_type": file_type,
                "upload_timestamp": datetime.utcnow().isoformat(),
                "memvid_version": "0.2.1",
            }

            if related_video_id:
                meta_info["related_video_id"] = related_video_id

            document_data = {
                "title": title,
                "description": description,
                "parentFolderId": self.config.folder_id,
                "metaInfo": meta_info,
            }

            # Prepare multipart form data
            with open(file_path, "rb") as f:
                files = {"file": (os.path.basename(file_path), f)}
                data = {"document": json.dumps(document_data)}

                # Make request
                headers = {
                    **auth_headers,
                    "X-Realm-ID": self.config.realm_id,
                }

                response = await client.post(
                    "/file/v2", files=files, data=data, headers=headers
                )

            if response.status_code in (200, 201):
                result = response.json()
                doc_id = result.get("id")
                logger.info(f"Uploaded {file_type} file: {doc_id}")
                return doc_id
            else:
                logger.error(
                    f"Upload failed with status {response.status_code}: {response.text}"
                )
                return None

        except Exception as e:
            logger.error(f"Error uploading file {file_path}: {e}", exc_info=True)
            return None

    async def list_remote_memories(self, project_name: Optional[str] = None) -> list:
        """
        List video memories stored remotely.

        Args:
            project_name: Optional project name to filter by

        Returns:
            List of document metadata dictionaries
        """
        try:
            client = await self._get_client()
            auth_headers = self.auth_manager.get_auth_header()

            # Get folder contents
            headers = {
                **auth_headers,
                "X-Realm-ID": self.config.realm_id,
            }

            response = await client.get(
                f"/folder/v2/content/{self.config.folder_id}", headers=headers
            )

            if response.status_code != 200:
                logger.error(
                    f"Failed to list memories: {response.status_code} {response.text}"
                )
                return []

            contents = response.json()

            # Filter for video memory files
            memories = []
            for item in contents:
                if item.get("isFolder"):
                    continue

                meta_info = item.get("metaInfo", {})
                if meta_info.get("file_type") == "video":
                    # Filter by project name if specified
                    if project_name and meta_info.get("project_name") != project_name:
                        continue

                    memories.append(
                        {
                            "id": item.get("id"),
                            "title": item.get("title"),
                            "project_name": meta_info.get("project_name"),
                            "upload_timestamp": meta_info.get("upload_timestamp"),
                            "filename": item.get("filename"),
                            "file_size": item.get("fileSize"),
                        }
                    )

            return memories

        except Exception as e:
            logger.error(f"Error listing remote memories: {e}", exc_info=True)
            return []

    async def download_video_memory(
        self, video_doc_id: str, output_dir: str
    ) -> tuple[Optional[str], Optional[str]]:
        """
        Download video memory files from remote storage.

        Args:
            video_doc_id: Document ID of the video file
            output_dir: Directory to save downloaded files

        Returns:
            tuple: (video_path, index_path) or (None, None) on failure
        """
        try:
            client = await self._get_client()
            auth_headers = self.auth_manager.get_auth_header()
            headers = {
                **auth_headers,
                "X-Realm-ID": self.config.realm_id,
            }

            # Get video document metadata to find related index
            response = await client.get(
                f"/document/v2/{video_doc_id}", headers=headers
            )
            if response.status_code != 200:
                logger.error(
                    f"Failed to get video document: {response.status_code} {response.text}"
                )
                return None, None

            video_doc = response.json()
            video_filename = video_doc.get("filename", "memory.mp4")

            # Download video file
            video_path = await self._download_file(
                doc_id=video_doc_id,
                output_dir=output_dir,
                filename=video_filename,
                headers=headers,
            )

            if video_path is None:
                return None, None

            # Find and download index file
            # Search for index file with matching related_video_id
            folder_contents = await client.get(
                f"/folder/v2/content/{self.config.folder_id}", headers=headers
            )

            if folder_contents.status_code != 200:
                logger.error("Failed to list folder contents")
                return video_path, None

            index_doc_id = None
            index_filename = None
            for item in folder_contents.json():
                meta_info = item.get("metaInfo", {})
                if meta_info.get("related_video_id") == video_doc_id:
                    index_doc_id = item.get("id")
                    index_filename = item.get("filename", "memory.json")
                    break

            if index_doc_id is None:
                logger.warning(f"No index file found for video {video_doc_id}")
                return video_path, None

            index_path = await self._download_file(
                doc_id=index_doc_id,
                output_dir=output_dir,
                filename=index_filename,
                headers=headers,
            )

            return video_path, index_path

        except Exception as e:
            logger.error(f"Error downloading video memory: {e}", exc_info=True)
            return None, None

    async def _download_file(
        self, doc_id: str, output_dir: str, filename: str, headers: dict
    ) -> Optional[str]:
        """Download a file from the API."""
        try:
            client = await self._get_client()

            response = await client.get(f"/file/v2/{doc_id}", headers=headers)

            if response.status_code != 200:
                logger.error(
                    f"Failed to download file: {response.status_code} {response.text}"
                )
                return None

            output_path = os.path.join(output_dir, filename)
            os.makedirs(output_dir, exist_ok=True)

            with open(output_path, "wb") as f:
                f.write(response.content)

            logger.info(f"Downloaded file to: {output_path}")
            return output_path

        except Exception as e:
            logger.error(f"Error downloading file {doc_id}: {e}", exc_info=True)
            return None
