from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.health_status import HealthStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.health_status_details import HealthStatusDetails


T = TypeVar("T", bound="ComponentStatus")


@_attrs_define
class ComponentStatus:
    """The health status of a health component

    Attributes:
        status (HealthStatus): The possible health statuses of a component
        details (HealthStatusDetails | Unset): The detailed health status of a health component
    """

    status: HealthStatus
    details: HealthStatusDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.health_status_details import HealthStatusDetails

        d = dict(src_dict)
        status = HealthStatus(d.pop("status"))

        _details = d.pop("details", UNSET)
        details: HealthStatusDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = HealthStatusDetails.from_dict(_details)

        component_status = cls(
            status=status,
            details=details,
        )

        component_status.additional_properties = d
        return component_status

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
