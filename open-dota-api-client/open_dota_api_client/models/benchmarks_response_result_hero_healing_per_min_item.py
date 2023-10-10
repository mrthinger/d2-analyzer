from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BenchmarksResponseResultHeroHealingPerMinItem")


@_attrs_define
class BenchmarksResponseResultHeroHealingPerMinItem:
    """
    Attributes:
        percentile (Union[Unset, float]): percentile
        value (Union[Unset, float]): value
    """

    percentile: Union[Unset, float] = UNSET
    value: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        percentile = self.percentile
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percentile is not UNSET:
            field_dict["percentile"] = percentile
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        percentile = d.pop("percentile", UNSET)

        value = d.pop("value", UNSET)

        benchmarks_response_result_hero_healing_per_min_item = cls(
            percentile=percentile,
            value=value,
        )

        benchmarks_response_result_hero_healing_per_min_item.additional_properties = d
        return benchmarks_response_result_hero_healing_per_min_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
