from enum import Enum


class SystemToolResultStatus(str, Enum):
    ERROR = "error"
    SKIPPED = "skipped"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
