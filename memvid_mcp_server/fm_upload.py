"""
Background upload manager for video memory files.

Handles asynchronous upload of video memory files without blocking MCP operations.
"""

import asyncio
import logging
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

from .fm_auth import FMAuthManager
from .fm_client import FMClient
from .fm_config import FMConfig

logger = logging.getLogger(__name__)


class UploadStatus(Enum):
    """Status of an upload task."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class UploadTask:
    """Represents a video memory upload task."""

    video_path: str
    index_path: str
    project_name: Optional[str]
    status: UploadStatus
    created_at: datetime
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    video_doc_id: Optional[str] = None
    index_doc_id: Optional[str] = None


class UploadManager:
    """Manages background uploads of video memory files."""

    def __init__(self, config: FMConfig, auth_manager: FMAuthManager):
        self.config = config
        self.auth_manager = auth_manager
        self.fm_client = FMClient(config, auth_manager)
        self._upload_queue: asyncio.Queue = asyncio.Queue()
        self._upload_tasks: dict[str, UploadTask] = {}
        self._worker_task: Optional[asyncio.Task] = None
        self._running = False

    def start(self) -> None:
        """Start the background upload worker."""
        if not self._running:
            self._running = True
            self._worker_task = asyncio.create_task(self._upload_worker())
            logger.info("Upload manager started")

    async def stop(self) -> None:
        """Stop the background upload worker."""
        self._running = False
        if self._worker_task:
            self._worker_task.cancel()
            try:
                await self._worker_task
            except asyncio.CancelledError:
                pass
        await self.fm_client.close()
        logger.info("Upload manager stopped")

    def queue_upload(
        self, video_path: str, index_path: str, project_name: Optional[str] = None
    ) -> str:
        """
        Queue a video memory upload.

        Args:
            video_path: Path to the video file
            index_path: Path to the index file
            project_name: Optional project name

        Returns:
            Task ID for tracking the upload
        """
        task_id = f"{video_path}_{datetime.utcnow().isoformat()}"

        task = UploadTask(
            video_path=video_path,
            index_path=index_path,
            project_name=project_name,
            status=UploadStatus.PENDING,
            created_at=datetime.utcnow(),
        )

        self._upload_tasks[task_id] = task
        self._upload_queue.put_nowait(task_id)

        logger.info(f"Queued upload task: {task_id}")
        return task_id

    def get_upload_status(self, task_id: str) -> Optional[UploadTask]:
        """
        Get the status of an upload task.

        Args:
            task_id: The task ID

        Returns:
            UploadTask or None if not found
        """
        return self._upload_tasks.get(task_id)

    def get_all_uploads(self) -> list[UploadTask]:
        """Get all upload tasks."""
        return list(self._upload_tasks.values())

    async def _upload_worker(self) -> None:
        """Background worker that processes upload queue."""
        logger.info("Upload worker started")

        while self._running:
            try:
                # Wait for a task with timeout to allow checking _running flag
                task_id = await asyncio.wait_for(
                    self._upload_queue.get(), timeout=1.0
                )

                task = self._upload_tasks.get(task_id)
                if task is None:
                    continue

                # Update status
                task.status = UploadStatus.IN_PROGRESS
                logger.info(f"Processing upload task: {task_id}")

                # Perform upload with retry logic
                success = await self._upload_with_retry(task)

                # Update status
                if success:
                    task.status = UploadStatus.COMPLETED
                    logger.info(f"Upload task completed: {task_id}")
                else:
                    task.status = UploadStatus.FAILED
                    logger.error(f"Upload task failed: {task_id}")

                task.completed_at = datetime.utcnow()

            except asyncio.TimeoutError:
                # No task in queue, continue waiting
                continue
            except asyncio.CancelledError:
                logger.info("Upload worker cancelled")
                break
            except Exception as e:
                logger.error(f"Error in upload worker: {e}", exc_info=True)

        logger.info("Upload worker stopped")

    async def _upload_with_retry(
        self, task: UploadTask, max_retries: int = 3
    ) -> bool:
        """
        Upload with retry logic.

        Args:
            task: The upload task
            max_retries: Maximum number of retry attempts

        Returns:
            True if successful, False otherwise
        """
        for attempt in range(max_retries):
            try:
                logger.info(
                    f"Upload attempt {attempt + 1}/{max_retries} for {task.video_path}"
                )

                video_doc_id, index_doc_id = await self.fm_client.upload_video_memory(
                    video_path=task.video_path,
                    index_path=task.index_path,
                    project_name=task.project_name,
                )

                if video_doc_id and index_doc_id:
                    task.video_doc_id = video_doc_id
                    task.index_doc_id = index_doc_id
                    return True

                # Partial success - log but retry
                if video_doc_id or index_doc_id:
                    logger.warning(
                        f"Partial upload success: video={video_doc_id}, index={index_doc_id}"
                    )

            except Exception as e:
                logger.error(
                    f"Upload attempt {attempt + 1} failed: {e}", exc_info=True
                )
                task.error_message = str(e)

            # Wait before retry with exponential backoff
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # 1s, 2s, 4s
                logger.info(f"Retrying in {wait_time} seconds...")
                await asyncio.sleep(wait_time)

        return False
