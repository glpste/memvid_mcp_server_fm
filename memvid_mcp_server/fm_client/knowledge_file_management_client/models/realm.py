from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.realm_settings import RealmSettings


T = TypeVar("T", bound="Realm")


@_attrs_define
class Realm:
    """External representation of a realm entity

    Attributes:
        id (str | Unset): The ID of the realm
        name (str | Unset): the name of the realm
        settings (RealmSettings | Unset): The configured settings of a realm
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    settings: RealmSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.realm_settings import RealmSettings

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: RealmSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = RealmSettings.from_dict(_settings)

        realm = cls(
            id=id,
            name=name,
            settings=settings,
        )

        realm.additional_properties = d
        return realm

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
