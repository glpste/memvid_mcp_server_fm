from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.component_status import ComponentStatus


T = TypeVar("T", bound="HealthComponents")


@_attrs_define
class HealthComponents:
    """Information about the statuses of all health components

    Attributes:
        fm (ComponentStatus): The health status of a health component
        db (ComponentStatus): The health status of a health component
        av (ComponentStatus): The health status of a health component
        s3 (ComponentStatus): The health status of a health component
        conv (ComponentStatus): The health status of a health component
    """

    fm: ComponentStatus
    db: ComponentStatus
    av: ComponentStatus
    s3: ComponentStatus
    conv: ComponentStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fm = self.fm.to_dict()

        db = self.db.to_dict()

        av = self.av.to_dict()

        s3 = self.s3.to_dict()

        conv = self.conv.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FM": fm,
                "DB": db,
                "AV": av,
                "S3": s3,
                "CONV": conv,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.component_status import ComponentStatus

        d = dict(src_dict)
        fm = ComponentStatus.from_dict(d.pop("FM"))

        db = ComponentStatus.from_dict(d.pop("DB"))

        av = ComponentStatus.from_dict(d.pop("AV"))

        s3 = ComponentStatus.from_dict(d.pop("S3"))

        conv = ComponentStatus.from_dict(d.pop("CONV"))

        health_components = cls(
            fm=fm,
            db=db,
            av=av,
            s3=s3,
            conv=conv,
        )

        health_components.additional_properties = d
        return health_components

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
