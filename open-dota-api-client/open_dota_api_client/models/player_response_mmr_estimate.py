from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerResponseMmrEstimate")


@_attrs_define
class PlayerResponseMmrEstimate:
    """mmr_estimate

    Attributes:
        estimate (Union[Unset, None, float]): estimate
    """

    estimate: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        estimate = self.estimate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if estimate is not UNSET:
            field_dict["estimate"] = estimate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        estimate = d.pop("estimate", UNSET)

        player_response_mmr_estimate = cls(
            estimate=estimate,
        )

        player_response_mmr_estimate.additional_properties = d
        return player_response_mmr_estimate

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
