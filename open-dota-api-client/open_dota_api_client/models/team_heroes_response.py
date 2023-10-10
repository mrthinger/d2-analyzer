from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamHeroesResponse")


@_attrs_define
class TeamHeroesResponse:
    """
    Attributes:
        hero_id (Union[Unset, int]): The ID value of the hero played
        name (Union[Unset, str]): Hero name Example: Anti-Mage.
        games_played (Union[Unset, int]): Number of games played
        wins (Union[Unset, int]): Number of wins
    """

    hero_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    games_played: Union[Unset, int] = UNSET
    wins: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hero_id = self.hero_id
        name = self.name
        games_played = self.games_played
        wins = self.wins

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if name is not UNSET:
            field_dict["name"] = name
        if games_played is not UNSET:
            field_dict["games_played"] = games_played
        if wins is not UNSET:
            field_dict["wins"] = wins

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hero_id = d.pop("hero_id", UNSET)

        name = d.pop("name", UNSET)

        games_played = d.pop("games_played", UNSET)

        wins = d.pop("wins", UNSET)

        team_heroes_response = cls(
            hero_id=hero_id,
            name=name,
            games_played=games_played,
            wins=wins,
        )

        team_heroes_response.additional_properties = d
        return team_heroes_response

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
