from enum import Enum


class SystemTools(str, Enum):
    NONE = "none"
    RESETPREVIEWS = "resetPreviews"
    SYNCPATHCACHE = "syncPathCache"

    def __str__(self) -> str:
        return str(self.value)
