from enum import Enum


class ConfigSettingKey(str, Enum):
    FILE_UPLOAD_AV_SIZE_LIMIT = "file.upload.av.size.limit"

    def __str__(self) -> str:
        return str(self.value)
