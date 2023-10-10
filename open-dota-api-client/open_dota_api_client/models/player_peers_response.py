from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerPeersResponse")


@_attrs_define
class PlayerPeersResponse:
    """
    Attributes:
        account_id (Union[Unset, int]): The player account ID
        last_played (Union[Unset, int]): last_played
        win (Union[Unset, int]): win
        games (Union[Unset, int]): games
        with_win (Union[Unset, int]): with_win
        with_games (Union[Unset, int]): with_games
        against_win (Union[Unset, int]): against_win
        against_games (Union[Unset, int]): against_games
        with_gpm_sum (Union[Unset, int]): with_gpm_sum
        with_xpm_sum (Union[Unset, int]): with_xpm_sum
        personaname (Union[Unset, None, str]): Player's Steam name Example: 420 booty wizard.
        name (Union[Unset, None, str]): name
        is_contributor (Union[Unset, bool]): is_contributor
        is_subscriber (Union[Unset, bool]): is_subscriber
        last_login (Union[Unset, None, str]): last_login
        avatar (Union[Unset, None, str]): avatar
        avatarfull (Union[Unset, None, str]): avatarfull
    """

    account_id: Union[Unset, int] = UNSET
    last_played: Union[Unset, int] = UNSET
    win: Union[Unset, int] = UNSET
    games: Union[Unset, int] = UNSET
    with_win: Union[Unset, int] = UNSET
    with_games: Union[Unset, int] = UNSET
    against_win: Union[Unset, int] = UNSET
    against_games: Union[Unset, int] = UNSET
    with_gpm_sum: Union[Unset, int] = UNSET
    with_xpm_sum: Union[Unset, int] = UNSET
    personaname: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    is_contributor: Union[Unset, bool] = UNSET
    is_subscriber: Union[Unset, bool] = UNSET
    last_login: Union[Unset, None, str] = UNSET
    avatar: Union[Unset, None, str] = UNSET
    avatarfull: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        last_played = self.last_played
        win = self.win
        games = self.games
        with_win = self.with_win
        with_games = self.with_games
        against_win = self.against_win
        against_games = self.against_games
        with_gpm_sum = self.with_gpm_sum
        with_xpm_sum = self.with_xpm_sum
        personaname = self.personaname
        name = self.name
        is_contributor = self.is_contributor
        is_subscriber = self.is_subscriber
        last_login = self.last_login
        avatar = self.avatar
        avatarfull = self.avatarfull

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if last_played is not UNSET:
            field_dict["last_played"] = last_played
        if win is not UNSET:
            field_dict["win"] = win
        if games is not UNSET:
            field_dict["games"] = games
        if with_win is not UNSET:
            field_dict["with_win"] = with_win
        if with_games is not UNSET:
            field_dict["with_games"] = with_games
        if against_win is not UNSET:
            field_dict["against_win"] = against_win
        if against_games is not UNSET:
            field_dict["against_games"] = against_games
        if with_gpm_sum is not UNSET:
            field_dict["with_gpm_sum"] = with_gpm_sum
        if with_xpm_sum is not UNSET:
            field_dict["with_xpm_sum"] = with_xpm_sum
        if personaname is not UNSET:
            field_dict["personaname"] = personaname
        if name is not UNSET:
            field_dict["name"] = name
        if is_contributor is not UNSET:
            field_dict["is_contributor"] = is_contributor
        if is_subscriber is not UNSET:
            field_dict["is_subscriber"] = is_subscriber
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if avatarfull is not UNSET:
            field_dict["avatarfull"] = avatarfull

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        last_played = d.pop("last_played", UNSET)

        win = d.pop("win", UNSET)

        games = d.pop("games", UNSET)

        with_win = d.pop("with_win", UNSET)

        with_games = d.pop("with_games", UNSET)

        against_win = d.pop("against_win", UNSET)

        against_games = d.pop("against_games", UNSET)

        with_gpm_sum = d.pop("with_gpm_sum", UNSET)

        with_xpm_sum = d.pop("with_xpm_sum", UNSET)

        personaname = d.pop("personaname", UNSET)

        name = d.pop("name", UNSET)

        is_contributor = d.pop("is_contributor", UNSET)

        is_subscriber = d.pop("is_subscriber", UNSET)

        last_login = d.pop("last_login", UNSET)

        avatar = d.pop("avatar", UNSET)

        avatarfull = d.pop("avatarfull", UNSET)

        player_peers_response = cls(
            account_id=account_id,
            last_played=last_played,
            win=win,
            games=games,
            with_win=with_win,
            with_games=with_games,
            against_win=against_win,
            against_games=against_games,
            with_gpm_sum=with_gpm_sum,
            with_xpm_sum=with_xpm_sum,
            personaname=personaname,
            name=name,
            is_contributor=is_contributor,
            is_subscriber=is_subscriber,
            last_login=last_login,
            avatar=avatar,
            avatarfull=avatarfull,
        )

        player_peers_response.additional_properties = d
        return player_peers_response

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
