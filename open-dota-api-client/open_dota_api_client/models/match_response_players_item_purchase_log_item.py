from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchResponsePlayersItemPurchaseLogItem")


@_attrs_define
class MatchResponsePlayersItemPurchaseLogItem:
    """
    Attributes:
        time (Union[Unset, int]): Time in seconds the item was bought
        key (Union[Unset, str]): String item ID
        charges (Union[Unset, int]): Integer amount of charges
    """

    time: Union[Unset, int] = UNSET
    key: Union[Unset, str] = UNSET
    charges: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time
        key = self.key
        charges = self.charges

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if key is not UNSET:
            field_dict["key"] = key
        if charges is not UNSET:
            field_dict["charges"] = charges

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = d.pop("time", UNSET)

        key = d.pop("key", UNSET)

        charges = d.pop("charges", UNSET)

        match_response_players_item_purchase_log_item = cls(
            time=time,
            key=key,
            charges=charges,
        )

        match_response_players_item_purchase_log_item.additional_properties = d
        return match_response_players_item_purchase_log_item

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
