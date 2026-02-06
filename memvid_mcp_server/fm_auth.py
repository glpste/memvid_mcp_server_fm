"""
Authentication module for Keycloak integration.

Handles OAuth2 token acquisition and management for the File Management API.
"""

import logging
import os
from typing import Optional

from keycloak import KeycloakOpenID

logger = logging.getLogger(__name__)


class FMAuthManager:
    """Manages authentication for the File Management API."""

    def __init__(
        self,
        keycloak_url: str,
        realm: str,
        client_id: str,
        client_secret: str,
    ):
        self.keycloak_url = keycloak_url
        self.realm = realm
        self.client_id = client_id
        self.client_secret = client_secret
        self._token: Optional[str] = None
        self._keycloak_openid: Optional[KeycloakOpenID] = None

    def _initialize_keycloak(self) -> None:
        """Initialize the Keycloak OpenID Connect client."""
        if self._keycloak_openid is None:
            self._keycloak_openid = KeycloakOpenID(
                server_url=self.keycloak_url,
                client_id=self.client_id,
                realm_name=self.realm,
                client_secret_key=self.client_secret,
            )
            logger.info(
                f"Initialized Keycloak client for realm '{self.realm}' at {self.keycloak_url}"
            )

    def get_token(self) -> str:
        """
        Get a valid access token.

        Returns:
            str: A valid bearer token

        Raises:
            Exception: If token acquisition fails
        """
        self._initialize_keycloak()

        try:
            # Get token using client credentials grant
            token_response = self._keycloak_openid.token(
                grant_type="client_credentials"
            )
            self._token = token_response["access_token"]
            logger.info("Successfully acquired access token")
            return self._token

        except Exception as e:
            logger.error(f"Failed to acquire access token: {e}")
            raise

    def get_auth_header(self) -> dict:
        """
        Get the authorization header for API requests.

        Returns:
            dict: Authorization header with bearer token
        """
        token = self.get_token()
        return {"Authorization": f"Bearer {token}"}


def create_auth_manager_from_env() -> Optional[FMAuthManager]:
    """
    Create an FMAuthManager from environment variables.

    Returns:
        FMAuthManager if all required env vars are present, None otherwise
    """
    keycloak_url = os.getenv("FM_KEYCLOAK_URL")
    realm = os.getenv("FM_KEYCLOAK_REALM")
    client_id = os.getenv("FM_KEYCLOAK_CLIENT_ID")
    client_secret = os.getenv("FM_KEYCLOAK_CLIENT_SECRET")

    if not all([keycloak_url, realm, client_id, client_secret]):
        missing = [
            var
            for var, val in [
                ("FM_KEYCLOAK_URL", keycloak_url),
                ("FM_KEYCLOAK_REALM", realm),
                ("FM_KEYCLOAK_CLIENT_ID", client_id),
                ("FM_KEYCLOAK_CLIENT_SECRET", client_secret),
            ]
            if not val
        ]
        logger.warning(
            f"FM authentication not configured. Missing environment variables: {', '.join(missing)}"
        )
        return None

    return FMAuthManager(
        keycloak_url=keycloak_url,
        realm=realm,
        client_id=client_id,
        client_secret=client_secret,
    )
