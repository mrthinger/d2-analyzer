from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerHeroesResponse")


@_attrs_define
class PlayerHeroesResponse:
    """hero

    Attributes:
        hero_id (Union[Unset, int]): The ID value of the hero played
        last_played (Union[Unset, int]): last_played
        games (Union[Unset, int]): games
        win (Union[Unset, int]): win
        with_games (Union[Unset, int]): with_games
        with_win (Union[Unset, int]): with_win
        against_games (Union[Unset, int]): against_games
        against_win (Union[Unset, int]): against_win
    """

    hero_id: Union[Unset, int] = UNSET
    last_played: Union[Unset, int] = UNSET
    games: Union[Unset, int] = UNSET
    win: Union[Unset, int] = UNSET
    with_games: Union[Unset, int] = UNSET
    with_win: Union[Unset, int] = UNSET
    against_games: Union[Unset, int] = UNSET
    against_win: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hero_id = self.hero_id
        last_played = self.last_played
        games = self.games
        win = self.win
        with_games = self.with_games
        with_win = self.with_win
        against_games = self.against_games
        against_win = self.against_win

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if last_played is not UNSET:
            field_dict["last_played"] = last_played
        if games is not UNSET:
            field_dict["games"] = games
        if win is not UNSET:
            field_dict["win"] = win
        if with_games is not UNSET:
            field_dict["with_games"] = with_games
        if with_win is not UNSET:
            field_dict["with_win"] = with_win
        if against_games is not UNSET:
            field_dict["against_games"] = against_games
        if against_win is not UNSET:
            field_dict["against_win"] = against_win

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hero_id = d.pop("hero_id", UNSET)

        last_played = d.pop("last_played", UNSET)

        games = d.pop("games", UNSET)

        win = d.pop("win", UNSET)

        with_games = d.pop("with_games", UNSET)

        with_win = d.pop("with_win", UNSET)

        against_games = d.pop("against_games", UNSET)

        against_win = d.pop("against_win", UNSET)

        player_heroes_response = cls(
            hero_id=hero_id,
            last_played=last_played,
            games=games,
            win=win,
            with_games=with_games,
            with_win=with_win,
            against_games=against_games,
            against_win=against_win,
        )

        player_heroes_response.additional_properties = d
        return player_heroes_response

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
