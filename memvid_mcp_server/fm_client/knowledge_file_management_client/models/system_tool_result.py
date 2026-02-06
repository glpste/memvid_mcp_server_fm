from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.system_tool_result_status import SystemToolResultStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemToolResult")


@_attrs_define
class SystemToolResult:
    """The result of a system tool's execution

    Attributes:
        text (str | Unset): The result of the system tool's execution
        status (SystemToolResultStatus | Unset): The status of the system tool's execution
        duration (str | Unset): The duration of the system tool's execution
    """

    text: str | Unset = UNSET
    status: SystemToolResultStatus | Unset = UNSET
    duration: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        duration = self.duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if status is not UNSET:
            field_dict["status"] = status
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text", UNSET)

        _status = d.pop("status", UNSET)
        status: SystemToolResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SystemToolResultStatus(_status)

        duration = d.pop("duration", UNSET)

        system_tool_result = cls(
            text=text,
            status=status,
            duration=duration,
        )

        system_tool_result.additional_properties = d
        return system_tool_result

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
