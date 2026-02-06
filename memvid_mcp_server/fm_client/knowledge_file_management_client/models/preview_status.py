from enum import Enum


class PreviewStatus(str, Enum):
    DONE = "done"
    FAILED = "failed"
    NONE = "none"
    PENDING = "pending"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
