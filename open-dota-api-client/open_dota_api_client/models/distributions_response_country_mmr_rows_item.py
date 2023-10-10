from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DistributionsResponseCountryMmrRowsItem")


@_attrs_define
class DistributionsResponseCountryMmrRowsItem:
    """
    Attributes:
        loccountrycode (Union[Unset, None, str]): loccountrycode
        count (Union[Unset, int]): count
        avg (Union[Unset, str]): avg
        common (Union[Unset, str]): common
    """

    loccountrycode: Union[Unset, None, str] = UNSET
    count: Union[Unset, int] = UNSET
    avg: Union[Unset, str] = UNSET
    common: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        loccountrycode = self.loccountrycode
        count = self.count
        avg = self.avg
        common = self.common

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loccountrycode is not UNSET:
            field_dict["loccountrycode"] = loccountrycode
        if count is not UNSET:
            field_dict["count"] = count
        if avg is not UNSET:
            field_dict["avg"] = avg
        if common is not UNSET:
            field_dict["common"] = common

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        loccountrycode = d.pop("loccountrycode", UNSET)

        count = d.pop("count", UNSET)

        avg = d.pop("avg", UNSET)

        common = d.pop("common", UNSET)

        distributions_response_country_mmr_rows_item = cls(
            loccountrycode=loccountrycode,
            count=count,
            avg=avg,
            common=common,
        )

        distributions_response_country_mmr_rows_item.additional_properties = d
        return distributions_response_country_mmr_rows_item

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
