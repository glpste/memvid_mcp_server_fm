from enum import Enum


class FileTextContentMode(str, Enum):
    FULL = "full"
    SUMMARY = "summary"

    def __str__(self) -> str:
        return str(self.value)
