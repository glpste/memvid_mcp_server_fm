from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicatesRequest")


@_attrs_define
class DuplicatesRequest:
    """A request to retrieve all possible duplicates of given sets of CRC32 and MD5 checksums

    Attributes:
        crc32 (list[int] | Unset): The crc32 checksums of the files to search for duplicates of
        md5 (list[str] | Unset): The md5 checksums of the files to search for duplicates of
    """

    crc32: list[int] | Unset = UNSET
    md5: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crc32: list[int] | Unset = UNSET
        if not isinstance(self.crc32, Unset):
            crc32 = self.crc32

        md5: list[str] | Unset = UNSET
        if not isinstance(self.md5, Unset):
            md5 = self.md5

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crc32 is not UNSET:
            field_dict["crc32"] = crc32
        if md5 is not UNSET:
            field_dict["md5"] = md5

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crc32 = cast(list[int], d.pop("crc32", UNSET))

        md5 = cast(list[str], d.pop("md5", UNSET))

        duplicates_request = cls(
            crc32=crc32,
            md5=md5,
        )

        duplicates_request.additional_properties = d
        return duplicates_request

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
