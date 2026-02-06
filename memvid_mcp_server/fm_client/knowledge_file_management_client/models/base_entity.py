from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseEntity")


@_attrs_define
class BaseEntity:
    """The base parent DTO of the File Management service, offering the shared attributes needed by both
    [Documents](#/components/schemas/Document) and [Folders](#/components/schemas/Folder)

        Attributes:
            title (str): The title of the entity
            id (str | Unset): The ID of the entity
            parent_folder_id (str | Unset): The ID of this entity's parent folder. This is the folder the entity resides in.
            created (datetime.datetime | Unset): The date the entity was created
            last_modified (datetime.datetime | Unset): The date the entity was last modified
            is_folder (bool | Unset): Whether this entity is a folder
    """

    title: str
    id: str | Unset = UNSET
    parent_folder_id: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    last_modified: datetime.datetime | Unset = UNSET
    is_folder: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        id = self.id

        parent_folder_id = self.parent_folder_id

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        last_modified: str | Unset = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        is_folder = self.is_folder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if parent_folder_id is not UNSET:
            field_dict["parentFolderId"] = parent_folder_id
        if created is not UNSET:
            field_dict["created"] = created
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if is_folder is not UNSET:
            field_dict["isFolder"] = is_folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        id = d.pop("id", UNSET)

        parent_folder_id = d.pop("parentFolderId", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: datetime.datetime | Unset
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        is_folder = d.pop("isFolder", UNSET)

        base_entity = cls(
            title=title,
            id=id,
            parent_folder_id=parent_folder_id,
            created=created,
            last_modified=last_modified,
            is_folder=is_folder,
        )

        base_entity.additional_properties = d
        return base_entity

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
