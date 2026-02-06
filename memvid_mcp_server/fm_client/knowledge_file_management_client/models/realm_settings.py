from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_upload_restriction_type import FileUploadRestrictionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RealmSettings")


@_attrs_define
class RealmSettings:
    """The configured settings of a realm

    Attributes:
        file_upload_restriction_type (FileUploadRestrictionType | Unset): The type of file upload restriction
        file_upload_restriction (list[str] | Unset): The list of file extensions that are allowed or disallowed,
            depending on the value of [file.upload.restriction.type](#/components/schemas/FileUploadRestrictionType)
        file_upload_av_size_limit (int | Unset): The maximum file size in bytes that is allowed to be uploaded.
            Configured for the entire instance and not per realm. This is actually a config setting and not a realm setting,
            but it is included here for ease of use.
        file_upload_av_whitelist (list[str] | Unset): The set of arbitrary identifiers that are allowed to bypass the
            virus scan when uploading. Values must be unique and are case-sensitive.
        file_url_lifetime_seconds (int | Unset): The lifetime of the isTemporary URLs to files in seconds. Default: 600.
    """

    file_upload_restriction_type: FileUploadRestrictionType | Unset = UNSET
    file_upload_restriction: list[str] | Unset = UNSET
    file_upload_av_size_limit: int | Unset = UNSET
    file_upload_av_whitelist: list[str] | Unset = UNSET
    file_url_lifetime_seconds: int | Unset = 600
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_upload_restriction_type: str | Unset = UNSET
        if not isinstance(self.file_upload_restriction_type, Unset):
            file_upload_restriction_type = self.file_upload_restriction_type.value

        file_upload_restriction: list[str] | Unset = UNSET
        if not isinstance(self.file_upload_restriction, Unset):
            file_upload_restriction = self.file_upload_restriction

        file_upload_av_size_limit = self.file_upload_av_size_limit

        file_upload_av_whitelist: list[str] | Unset = UNSET
        if not isinstance(self.file_upload_av_whitelist, Unset):
            file_upload_av_whitelist = self.file_upload_av_whitelist

        file_url_lifetime_seconds = self.file_url_lifetime_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_upload_restriction_type is not UNSET:
            field_dict["file.upload.restriction.type"] = file_upload_restriction_type
        if file_upload_restriction is not UNSET:
            field_dict["file.upload.restriction"] = file_upload_restriction
        if file_upload_av_size_limit is not UNSET:
            field_dict["file.upload.av.size.limit"] = file_upload_av_size_limit
        if file_upload_av_whitelist is not UNSET:
            field_dict["file.upload.av.whitelist"] = file_upload_av_whitelist
        if file_url_lifetime_seconds is not UNSET:
            field_dict["file.url.lifetime.seconds"] = file_url_lifetime_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _file_upload_restriction_type = d.pop("file.upload.restriction.type", UNSET)
        file_upload_restriction_type: FileUploadRestrictionType | Unset
        if isinstance(_file_upload_restriction_type, Unset):
            file_upload_restriction_type = UNSET
        else:
            file_upload_restriction_type = FileUploadRestrictionType(_file_upload_restriction_type)

        file_upload_restriction = cast(list[str], d.pop("file.upload.restriction", UNSET))

        file_upload_av_size_limit = d.pop("file.upload.av.size.limit", UNSET)

        file_upload_av_whitelist = cast(list[str], d.pop("file.upload.av.whitelist", UNSET))

        file_url_lifetime_seconds = d.pop("file.url.lifetime.seconds", UNSET)

        realm_settings = cls(
            file_upload_restriction_type=file_upload_restriction_type,
            file_upload_restriction=file_upload_restriction,
            file_upload_av_size_limit=file_upload_av_size_limit,
            file_upload_av_whitelist=file_upload_av_whitelist,
            file_url_lifetime_seconds=file_url_lifetime_seconds,
        )

        realm_settings.additional_properties = d
        return realm_settings

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
