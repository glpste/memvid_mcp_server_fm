from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_tool_params import SystemToolParams
    from ..models.system_tool_result import SystemToolResult


T = TypeVar("T", bound="SystemTool")


@_attrs_define
class SystemTool:
    """A system tool that can be executed to perform a specific task for a single realm, e.g. cleanup operations

    Attributes:
        name (str): The name of the system tool to execute. See [SystemTools](#/components/schemas/SystemTools)
        realm_id (str): The ID of the realm the system tool shall be or was executed for
        result (SystemToolResult | Unset): The result of a system tool's execution
        params (SystemToolParams | Unset): The parameters of a system tool
    """

    name: str
    realm_id: str
    result: SystemToolResult | Unset = UNSET
    params: SystemToolParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        realm_id = self.realm_id

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "realmId": realm_id,
            }
        )
        if result is not UNSET:
            field_dict["result"] = result
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_tool_params import SystemToolParams
        from ..models.system_tool_result import SystemToolResult

        d = dict(src_dict)
        name = d.pop("name")

        realm_id = d.pop("realmId")

        _result = d.pop("result", UNSET)
        result: SystemToolResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = SystemToolResult.from_dict(_result)

        _params = d.pop("params", UNSET)
        params: SystemToolParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = SystemToolParams.from_dict(_params)

        system_tool = cls(
            name=name,
            realm_id=realm_id,
            result=result,
            params=params,
        )

        system_tool.additional_properties = d
        return system_tool

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
