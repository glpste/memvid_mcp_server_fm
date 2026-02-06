from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceToken")


@_attrs_define
class ResourceToken:
    """Wrapper DTO for a temporary download token for a resource/file

    Attributes:
        jwt (str | Unset): The token in JWT format
        expires (datetime.datetime | Unset): The date the token expires
        relative_url (str | Unset): The relative URL to download the resource/file using the token
    """

    jwt: str | Unset = UNSET
    expires: datetime.datetime | Unset = UNSET
    relative_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jwt = self.jwt

        expires: str | Unset = UNSET
        if not isinstance(self.expires, Unset):
            expires = self.expires.isoformat()

        relative_url = self.relative_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jwt is not UNSET:
            field_dict["jwt"] = jwt
        if expires is not UNSET:
            field_dict["expires"] = expires
        if relative_url is not UNSET:
            field_dict["relativeUrl"] = relative_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        jwt = d.pop("jwt", UNSET)

        _expires = d.pop("expires", UNSET)
        expires: datetime.datetime | Unset
        if isinstance(_expires, Unset):
            expires = UNSET
        else:
            expires = isoparse(_expires)

        relative_url = d.pop("relativeUrl", UNSET)

        resource_token = cls(
            jwt=jwt,
            expires=expires,
            relative_url=relative_url,
        )

        resource_token.additional_properties = d
        return resource_token

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
