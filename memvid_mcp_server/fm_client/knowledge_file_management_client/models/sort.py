from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sort_direction import SortDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="Sort")


@_attrs_define
class Sort:
    """
    Attributes:
        direction (SortDirection | Unset): The direction to sort by
        properties (list[str] | Unset): The properties to sort by
    """

    direction: SortDirection | Unset = UNSET
    properties: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        properties: list[str] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if direction is not UNSET:
            field_dict["direction"] = direction
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _direction = d.pop("direction", UNSET)
        direction: SortDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = SortDirection(_direction)

        properties = cast(list[str], d.pop("properties", UNSET))

        sort = cls(
            direction=direction,
            properties=properties,
        )

        sort.additional_properties = d
        return sort

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
