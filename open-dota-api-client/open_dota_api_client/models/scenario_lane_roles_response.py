from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScenarioLaneRolesResponse")


@_attrs_define
class ScenarioLaneRolesResponse:
    """
    Attributes:
        hero_id (Union[Unset, int]): The ID value of the hero played
        lane_role (Union[Unset, int]): The hero's lane role
        time (Union[Unset, int]): Maximum game length in seconds
        games (Union[Unset, str]): The number of games where the hero played in this lane role
        wins (Union[Unset, str]): The number of games won where the hero played in this lane role
    """

    hero_id: Union[Unset, int] = UNSET
    lane_role: Union[Unset, int] = UNSET
    time: Union[Unset, int] = UNSET
    games: Union[Unset, str] = UNSET
    wins: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hero_id = self.hero_id
        lane_role = self.lane_role
        time = self.time
        games = self.games
        wins = self.wins

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if lane_role is not UNSET:
            field_dict["lane_role"] = lane_role
        if time is not UNSET:
            field_dict["time"] = time
        if games is not UNSET:
            field_dict["games"] = games
        if wins is not UNSET:
            field_dict["wins"] = wins

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hero_id = d.pop("hero_id", UNSET)

        lane_role = d.pop("lane_role", UNSET)

        time = d.pop("time", UNSET)

        games = d.pop("games", UNSET)

        wins = d.pop("wins", UNSET)

        scenario_lane_roles_response = cls(
            hero_id=hero_id,
            lane_role=lane_role,
            time=time,
            games=games,
            wins=wins,
        )

        scenario_lane_roles_response.additional_properties = d
        return scenario_lane_roles_response

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
