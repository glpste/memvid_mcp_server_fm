from enum import Enum


class RequestHeaders(str, Enum):
    X_AV_PRIVILEGE = "X-AV-Privilege"
    X_REALM_ID = "X-Realm-ID"

    def __str__(self) -> str:
        return str(self.value)
