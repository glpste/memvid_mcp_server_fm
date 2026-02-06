from enum import Enum


class RealmSettingKey(str, Enum):
    FILE_UPLOAD_AV_WHITELIST = "file.upload.av.whitelist"
    FILE_UPLOAD_RESTRICTION = "file.upload.restriction"
    FILE_UPLOAD_RESTRICTION_TYPE = "file.upload.restriction.type"
    FILE_URL_LIFETIME_SECONDS = "file.url.lifetime.seconds"

    def __str__(self) -> str:
        return str(self.value)
