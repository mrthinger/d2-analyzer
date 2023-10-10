from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchResponsePlayersItemConnectionLogItem")


@_attrs_define
class MatchResponsePlayersItemConnectionLogItem:
    """
    Attributes:
        time (Union[Unset, int]): Game time in seconds the event ocurred
        event (Union[Unset, str]): Event that occurred
        player_slot (Union[Unset, None, int]): Which slot the player is in. 0-127 are Radiant, 128-255 are Dire
    """

    time: Union[Unset, int] = UNSET
    event: Union[Unset, str] = UNSET
    player_slot: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time
        event = self.event
        player_slot = self.player_slot

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if event is not UNSET:
            field_dict["event"] = event
        if player_slot is not UNSET:
            field_dict["player_slot"] = player_slot

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = d.pop("time", UNSET)

        event = d.pop("event", UNSET)

        player_slot = d.pop("player_slot", UNSET)

        match_response_players_item_connection_log_item = cls(
            time=time,
            event=event,
            player_slot=player_slot,
        )

        match_response_players_item_connection_log_item.additional_properties = d
        return match_response_players_item_connection_log_item

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
