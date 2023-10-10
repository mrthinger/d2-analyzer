from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchResponsePlayersItemBuybackLogItem")


@_attrs_define
class MatchResponsePlayersItemBuybackLogItem:
    """
    Attributes:
        time (Union[Unset, int]): Time in seconds the buyback occurred
        slot (Union[Unset, int]): slot
        player_slot (Union[Unset, None, int]): Which slot the player is in. 0-127 are Radiant, 128-255 are Dire
    """

    time: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    player_slot: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time
        slot = self.slot
        player_slot = self.player_slot

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if slot is not UNSET:
            field_dict["slot"] = slot
        if player_slot is not UNSET:
            field_dict["player_slot"] = player_slot

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = d.pop("time", UNSET)

        slot = d.pop("slot", UNSET)

        player_slot = d.pop("player_slot", UNSET)

        match_response_players_item_buyback_log_item = cls(
            time=time,
            slot=slot,
            player_slot=player_slot,
        )

        match_response_players_item_buyback_log_item.additional_properties = d
        return match_response_players_item_buyback_log_item

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
