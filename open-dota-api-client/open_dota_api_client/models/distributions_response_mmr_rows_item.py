from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DistributionsResponseMmrRowsItem")


@_attrs_define
class DistributionsResponseMmrRowsItem:
    """
    Attributes:
        bin_ (Union[Unset, int]): bin
        bin_name (Union[Unset, int]): bin_name
        count (Union[Unset, int]): count
        cumulative_sum (Union[Unset, int]): cumulative_sum
    """

    bin_: Union[Unset, int] = UNSET
    bin_name: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    cumulative_sum: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bin_ = self.bin_
        bin_name = self.bin_name
        count = self.count
        cumulative_sum = self.cumulative_sum

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bin_ is not UNSET:
            field_dict["bin"] = bin_
        if bin_name is not UNSET:
            field_dict["bin_name"] = bin_name
        if count is not UNSET:
            field_dict["count"] = count
        if cumulative_sum is not UNSET:
            field_dict["cumulative_sum"] = cumulative_sum

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bin_ = d.pop("bin", UNSET)

        bin_name = d.pop("bin_name", UNSET)

        count = d.pop("count", UNSET)

        cumulative_sum = d.pop("cumulative_sum", UNSET)

        distributions_response_mmr_rows_item = cls(
            bin_=bin_,
            bin_name=bin_name,
            count=count,
            cumulative_sum=cumulative_sum,
        )

        distributions_response_mmr_rows_item.additional_properties = d
        return distributions_response_mmr_rows_item

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
