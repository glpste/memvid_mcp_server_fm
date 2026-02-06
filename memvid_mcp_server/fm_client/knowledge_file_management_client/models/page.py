from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_entity import BaseEntity


T = TypeVar("T", bound="Page")


@_attrs_define
class Page:
    """A page of search results

    Attributes:
        content (list[BaseEntity] | Unset): The actual search results
        page (int | Unset): The current page number of the search result
        total_pages (int | Unset): The total number of pages of the search result
        total_elements (int | Unset): The total number of search results
    """

    content: list[BaseEntity] | Unset = UNSET
    page: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    total_elements: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)

        page = self.page

        total_pages = self.total_pages

        total_elements = self.total_elements

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if page is not UNSET:
            field_dict["page"] = page
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if total_elements is not UNSET:
            field_dict["totalElements"] = total_elements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_entity import BaseEntity

        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: list[BaseEntity] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
                content_item = BaseEntity.from_dict(content_item_data)

                content.append(content_item)

        page = d.pop("page", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        total_elements = d.pop("totalElements", UNSET)

        page = cls(
            content=content,
            page=page,
            total_pages=total_pages,
            total_elements=total_elements,
        )

        page.additional_properties = d
        return page

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
