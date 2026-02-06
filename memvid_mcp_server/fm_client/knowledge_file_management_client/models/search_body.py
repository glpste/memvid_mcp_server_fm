from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.page_request import PageRequest


T = TypeVar("T", bound="SearchBody")


@_attrs_define
class SearchBody:
    """
    Attributes:
        query (str):
        pageable (PageRequest):
    """

    query: str
    pageable: PageRequest
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        pageable = self.pageable.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "pageable": pageable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_request import PageRequest

        d = dict(src_dict)
        query = d.pop("query")

        pageable = PageRequest.from_dict(d.pop("pageable"))

        search_body = cls(
            query=query,
            pageable=pageable,
        )

        search_body.additional_properties = d
        return search_body

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
