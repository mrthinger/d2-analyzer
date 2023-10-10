from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamPlayersResponse")


@_attrs_define
class TeamPlayersResponse:
    """
    Attributes:
        account_id (Union[Unset, int]): The player account ID
        name (Union[Unset, None, str]): name
        games_played (Union[Unset, int]): Number of games played
        wins (Union[Unset, int]): Number of wins
        is_current_team_member (Union[Unset, bool]): If this player is on the current roster
    """

    account_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    games_played: Union[Unset, int] = UNSET
    wins: Union[Unset, int] = UNSET
    is_current_team_member: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        name = self.name
        games_played = self.games_played
        wins = self.wins
        is_current_team_member = self.is_current_team_member

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if name is not UNSET:
            field_dict["name"] = name
        if games_played is not UNSET:
            field_dict["games_played"] = games_played
        if wins is not UNSET:
            field_dict["wins"] = wins
        if is_current_team_member is not UNSET:
            field_dict["is_current_team_member"] = is_current_team_member

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        name = d.pop("name", UNSET)

        games_played = d.pop("games_played", UNSET)

        wins = d.pop("wins", UNSET)

        is_current_team_member = d.pop("is_current_team_member", UNSET)

        team_players_response = cls(
            account_id=account_id,
            name=name,
            games_played=games_played,
            wins=wins,
            is_current_team_member=is_current_team_member,
        )

        team_players_response.additional_properties = d
        return team_players_response

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
