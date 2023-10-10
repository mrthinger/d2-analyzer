from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeroMatchupsResponse")


@_attrs_define
class HeroMatchupsResponse:
    """
    Attributes:
        hero_id (Union[Unset, int]): The ID value of the hero played
        games_played (Union[Unset, int]): Number of games played
        wins (Union[Unset, int]): Number of games won
    """

    hero_id: Union[Unset, int] = UNSET
    games_played: Union[Unset, int] = UNSET
    wins: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hero_id = self.hero_id
        games_played = self.games_played
        wins = self.wins

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if games_played is not UNSET:
            field_dict["games_played"] = games_played
        if wins is not UNSET:
            field_dict["wins"] = wins

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hero_id = d.pop("hero_id", UNSET)

        games_played = d.pop("games_played", UNSET)

        wins = d.pop("wins", UNSET)

        hero_matchups_response = cls(
            hero_id=hero_id,
            games_played=games_played,
            wins=wins,
        )

        hero_matchups_response.additional_properties = d
        return hero_matchups_response

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
