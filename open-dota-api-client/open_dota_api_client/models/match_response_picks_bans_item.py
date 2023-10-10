from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchResponsePicksBansItem")


@_attrs_define
class MatchResponsePicksBansItem:
    """
    Attributes:
        is_pick (Union[Unset, bool]): Boolean indicating whether the choice is a pick or a ban
        hero_id (Union[Unset, int]): The ID value of the hero played
        team (Union[Unset, int]): The team that picked or banned the hero
        order (Union[Unset, int]): The order of the pick or ban
    """

    is_pick: Union[Unset, bool] = UNSET
    hero_id: Union[Unset, int] = UNSET
    team: Union[Unset, int] = UNSET
    order: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_pick = self.is_pick
        hero_id = self.hero_id
        team = self.team
        order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_pick is not UNSET:
            field_dict["is_pick"] = is_pick
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if team is not UNSET:
            field_dict["team"] = team
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_pick = d.pop("is_pick", UNSET)

        hero_id = d.pop("hero_id", UNSET)

        team = d.pop("team", UNSET)

        order = d.pop("order", UNSET)

        match_response_picks_bans_item = cls(
            is_pick=is_pick,
            hero_id=hero_id,
            team=team,
            order=order,
        )

        match_response_picks_bans_item.additional_properties = d
        return match_response_picks_bans_item

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
