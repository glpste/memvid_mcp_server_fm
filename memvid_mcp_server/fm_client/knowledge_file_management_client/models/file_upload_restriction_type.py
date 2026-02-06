from enum import Enum


class FileUploadRestrictionType(str, Enum):
    BLACKLIST = "blacklist"
    NONE = "none"
    WHITELIST = "whitelist"

    def __str__(self) -> str:
        return str(self.value)
