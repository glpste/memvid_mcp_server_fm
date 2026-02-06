from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

if TYPE_CHECKING:
    from ..models.base_entity import BaseEntity


T = TypeVar("T", bound="UpdateFileBody")


@_attrs_define
class UpdateFileBody:
    """
    Attributes:
        file (File): The file to upload
        document (BaseEntity): The base parent DTO of the File Management service, offering the shared attributes needed
            by both [Documents](#/components/schemas/Document) and [Folders](#/components/schemas/Folder)
    """

    file: File
    document: BaseEntity
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        document = self.document.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "document": document,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        files.append(("document", (None, json.dumps(self.document.to_dict()).encode(), "application/json")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_entity import BaseEntity

        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        document = BaseEntity.from_dict(d.pop("document"))

        update_file_body = cls(
            file=file,
            document=document,
        )

        update_file_body.additional_properties = d
        return update_file_body

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
