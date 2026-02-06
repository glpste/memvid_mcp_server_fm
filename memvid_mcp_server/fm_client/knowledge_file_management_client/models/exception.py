from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Exception_")


@_attrs_define
class Exception_:
    """External representation of an error encountered in the application

    Attributes:
        exception (str): The name of the exception that was thrown
        message (str): The message of the exception that was thrown
        status (int): The HTTP status associated with the error
        code (int): The error code associated with the error Default: 1.
        params (list[str] | Unset): The parameters of the exception, e.g. for parameterized error messages in subsequent
            processing
    """

    exception: str
    message: str
    status: int
    code: int = 1
    params: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exception = self.exception

        message = self.message

        status = self.status

        code = self.code

        params: list[str] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exception": exception,
                "message": message,
                "status": status,
                "code": code,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exception = d.pop("exception")

        message = d.pop("message")

        status = d.pop("status")

        code = d.pop("code")

        params = cast(list[str], d.pop("params", UNSET))

        exception = cls(
            exception=exception,
            message=message,
            status=status,
            code=code,
            params=params,
        )

        exception.additional_properties = d
        return exception

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
