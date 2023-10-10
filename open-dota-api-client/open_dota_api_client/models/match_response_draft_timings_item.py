from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchResponseDraftTimingsItem")


@_attrs_define
class MatchResponseDraftTimingsItem:
    """draft_stage

    Attributes:
        order (Union[Unset, int]): order
        pick (Union[Unset, bool]): pick
        active_team (Union[Unset, int]): active_team
        hero_id (Union[Unset, int]): The ID value of the hero played
        player_slot (Union[Unset, None, int]): Which slot the player is in. 0-127 are Radiant, 128-255 are Dire
        extra_time (Union[Unset, int]): extra_time
        total_time_taken (Union[Unset, int]): total_time_taken
    """

    order: Union[Unset, int] = UNSET
    pick: Union[Unset, bool] = UNSET
    active_team: Union[Unset, int] = UNSET
    hero_id: Union[Unset, int] = UNSET
    player_slot: Union[Unset, None, int] = UNSET
    extra_time: Union[Unset, int] = UNSET
    total_time_taken: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order = self.order
        pick = self.pick
        active_team = self.active_team
        hero_id = self.hero_id
        player_slot = self.player_slot
        extra_time = self.extra_time
        total_time_taken = self.total_time_taken

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if pick is not UNSET:
            field_dict["pick"] = pick
        if active_team is not UNSET:
            field_dict["active_team"] = active_team
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if player_slot is not UNSET:
            field_dict["player_slot"] = player_slot
        if extra_time is not UNSET:
            field_dict["extra_time"] = extra_time
        if total_time_taken is not UNSET:
            field_dict["total_time_taken"] = total_time_taken

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order = d.pop("order", UNSET)

        pick = d.pop("pick", UNSET)

        active_team = d.pop("active_team", UNSET)

        hero_id = d.pop("hero_id", UNSET)

        player_slot = d.pop("player_slot", UNSET)

        extra_time = d.pop("extra_time", UNSET)

        total_time_taken = d.pop("total_time_taken", UNSET)

        match_response_draft_timings_item = cls(
            order=order,
            pick=pick,
            active_team=active_team,
            hero_id=hero_id,
            player_slot=player_slot,
            extra_time=extra_time,
            total_time_taken=total_time_taken,
        )

        match_response_draft_timings_item.additional_properties = d
        return match_response_draft_timings_item

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
