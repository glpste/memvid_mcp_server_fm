"""
Configuration management for File Management API integration.

Handles environment variable loading, validation, and configuration state.
"""

import logging
import os
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class FMConfig:
    """Configuration for File Management API integration."""

    api_base_url: str
    realm_id: str
    folder_id: str
    keycloak_url: str
    keycloak_realm: str
    keycloak_client_id: str
    keycloak_client_secret: str
    upload_enabled: bool = True

    def validate(self) -> tuple[bool, Optional[str]]:
        """
        Validate the configuration.

        Returns:
            tuple: (is_valid, error_message)
        """
        if not self.api_base_url:
            return False, "FM_API_BASE_URL is required"
        if not self.realm_id:
            return False, "FM_REALM_ID is required"
        if not self.folder_id:
            return False, "FM_FOLDER_ID is required"
        if not self.keycloak_url:
            return False, "FM_KEYCLOAK_URL is required"
        if not self.keycloak_realm:
            return False, "FM_KEYCLOAK_REALM is required"
        if not self.keycloak_client_id:
            return False, "FM_KEYCLOAK_CLIENT_ID is required"
        if not self.keycloak_client_secret:
            return False, "FM_KEYCLOAK_CLIENT_SECRET is required"

        # Validate URL format
        if not self.api_base_url.startswith(("http://", "https://")):
            return False, "FM_API_BASE_URL must start with http:// or https://"
        if not self.keycloak_url.startswith(("http://", "https://")):
            return False, "FM_KEYCLOAK_URL must start with http:// or https://"

        return True, None


def load_fm_config() -> Optional[FMConfig]:
    """
    Load File Management configuration from environment variables.

    Returns:
        FMConfig if all required variables are present and valid, None otherwise
    """
    # Check if upload is explicitly disabled
    upload_enabled_str = os.getenv("FM_UPLOAD_ENABLED", "false").lower()
    upload_enabled = upload_enabled_str in ("true", "1", "yes", "on")

    if not upload_enabled:
        logger.info("FM upload is disabled via FM_UPLOAD_ENABLED=false")
        return None

    # Load all configuration variables
    api_base_url = os.getenv("FM_API_BASE_URL", "").rstrip("/")
    realm_id = os.getenv("FM_REALM_ID", "")
    folder_id = os.getenv("FM_FOLDER_ID", "")
    keycloak_url = os.getenv("FM_KEYCLOAK_URL", "").rstrip("/")
    keycloak_realm = os.getenv("FM_KEYCLOAK_REALM", "")
    keycloak_client_id = os.getenv("FM_KEYCLOAK_CLIENT_ID", "")
    keycloak_client_secret = os.getenv("FM_KEYCLOAK_CLIENT_SECRET", "")

    # Check if any are missing
    required_vars = {
        "FM_API_BASE_URL": api_base_url,
        "FM_REALM_ID": realm_id,
        "FM_FOLDER_ID": folder_id,
        "FM_KEYCLOAK_URL": keycloak_url,
        "FM_KEYCLOAK_REALM": keycloak_realm,
        "FM_KEYCLOAK_CLIENT_ID": keycloak_client_id,
        "FM_KEYCLOAK_CLIENT_SECRET": keycloak_client_secret,
    }

    missing = [name for name, value in required_vars.items() if not value]
    if missing:
        logger.info(
            f"FM integration not configured. Missing variables: {', '.join(missing)}"
        )
        return None

    # Create config
    config = FMConfig(
        api_base_url=api_base_url,
        realm_id=realm_id,
        folder_id=folder_id,
        keycloak_url=keycloak_url,
        keycloak_realm=keycloak_realm,
        keycloak_client_id=keycloak_client_id,
        keycloak_client_secret=keycloak_client_secret,
        upload_enabled=upload_enabled,
    )

    # Validate
    is_valid, error_msg = config.validate()
    if not is_valid:
        logger.error(f"FM configuration validation failed: {error_msg}")
        return None

    logger.info(
        f"FM integration configured: API={api_base_url}, Realm={realm_id}, Folder={folder_id}"
    )
    return config
