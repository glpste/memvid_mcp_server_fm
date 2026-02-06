from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_entity import BaseEntity


T = TypeVar("T", bound="UpdateDocumentBody")


@_attrs_define
class UpdateDocumentBody:
    """
    Attributes:
        document (BaseEntity | Unset): The base parent DTO of the File Management service, offering the shared
            attributes needed by both [Documents](#/components/schemas/Document) and [Folders](#/components/schemas/Folder)
    """

    document: BaseEntity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document is not UNSET:
            field_dict["document"] = document

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.document, Unset):
            files.append(("document", (None, json.dumps(self.document.to_dict()).encode(), "application/json")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_entity import BaseEntity

        d = dict(src_dict)
        _document = d.pop("document", UNSET)
        document: BaseEntity | Unset
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = BaseEntity.from_dict(_document)

        update_document_body = cls(
            document=document,
        )

        update_document_body.additional_properties = d
        return update_document_body

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
