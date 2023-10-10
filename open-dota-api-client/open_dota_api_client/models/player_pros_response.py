import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerProsResponse")


@_attrs_define
class PlayerProsResponse:
    """
    Attributes:
        account_id (Union[Unset, int]): The player account ID
        name (Union[Unset, None, str]): name
        country_code (Union[Unset, str]): country_code
        fantasy_role (Union[Unset, int]): fantasy_role
        team_id (Union[Unset, int]): team_id
        team_name (Union[Unset, None, str]): Team name Example: Newbee.
        team_tag (Union[Unset, None, str]): team_tag
        is_locked (Union[Unset, bool]): is_locked
        is_pro (Union[Unset, bool]): is_pro
        locked_until (Union[Unset, None, int]): locked_until
        steamid (Union[Unset, None, str]): steamid
        avatar (Union[Unset, None, str]): avatar
        avatarmedium (Union[Unset, None, str]): avatarmedium
        avatarfull (Union[Unset, None, str]): avatarfull
        profileurl (Union[Unset, None, str]): profileurl
        last_login (Union[Unset, None, datetime.datetime]): last_login
        full_history_time (Union[Unset, None, datetime.datetime]): full_history_time
        cheese (Union[Unset, None, int]): cheese
        fh_unavailable (Union[Unset, None, bool]): fh_unavailable
        loccountrycode (Union[Unset, None, str]): loccountrycode
        last_played (Union[Unset, None, int]): last_played
        win (Union[Unset, int]): win
        games (Union[Unset, int]): games
        with_win (Union[Unset, int]): with_win
        with_games (Union[Unset, int]): with_games
        against_win (Union[Unset, int]): against_win
        against_games (Union[Unset, int]): against_games
        with_gpm_sum (Union[Unset, None, int]): with_gpm_sum
        with_xpm_sum (Union[Unset, None, int]): with_xpm_sum
    """

    account_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    fantasy_role: Union[Unset, int] = UNSET
    team_id: Union[Unset, int] = UNSET
    team_name: Union[Unset, None, str] = UNSET
    team_tag: Union[Unset, None, str] = UNSET
    is_locked: Union[Unset, bool] = UNSET
    is_pro: Union[Unset, bool] = UNSET
    locked_until: Union[Unset, None, int] = UNSET
    steamid: Union[Unset, None, str] = UNSET
    avatar: Union[Unset, None, str] = UNSET
    avatarmedium: Union[Unset, None, str] = UNSET
    avatarfull: Union[Unset, None, str] = UNSET
    profileurl: Union[Unset, None, str] = UNSET
    last_login: Union[Unset, None, datetime.datetime] = UNSET
    full_history_time: Union[Unset, None, datetime.datetime] = UNSET
    cheese: Union[Unset, None, int] = UNSET
    fh_unavailable: Union[Unset, None, bool] = UNSET
    loccountrycode: Union[Unset, None, str] = UNSET
    last_played: Union[Unset, None, int] = UNSET
    win: Union[Unset, int] = UNSET
    games: Union[Unset, int] = UNSET
    with_win: Union[Unset, int] = UNSET
    with_games: Union[Unset, int] = UNSET
    against_win: Union[Unset, int] = UNSET
    against_games: Union[Unset, int] = UNSET
    with_gpm_sum: Union[Unset, None, int] = UNSET
    with_xpm_sum: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        name = self.name
        country_code = self.country_code
        fantasy_role = self.fantasy_role
        team_id = self.team_id
        team_name = self.team_name
        team_tag = self.team_tag
        is_locked = self.is_locked
        is_pro = self.is_pro
        locked_until = self.locked_until
        steamid = self.steamid
        avatar = self.avatar
        avatarmedium = self.avatarmedium
        avatarfull = self.avatarfull
        profileurl = self.profileurl
        last_login: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_login, Unset):
            last_login = self.last_login.isoformat() if self.last_login else None

        full_history_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.full_history_time, Unset):
            full_history_time = self.full_history_time.isoformat() if self.full_history_time else None

        cheese = self.cheese
        fh_unavailable = self.fh_unavailable
        loccountrycode = self.loccountrycode
        last_played = self.last_played
        win = self.win
        games = self.games
        with_win = self.with_win
        with_games = self.with_games
        against_win = self.against_win
        against_games = self.against_games
        with_gpm_sum = self.with_gpm_sum
        with_xpm_sum = self.with_xpm_sum

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if name is not UNSET:
            field_dict["name"] = name
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if fantasy_role is not UNSET:
            field_dict["fantasy_role"] = fantasy_role
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if team_name is not UNSET:
            field_dict["team_name"] = team_name
        if team_tag is not UNSET:
            field_dict["team_tag"] = team_tag
        if is_locked is not UNSET:
            field_dict["is_locked"] = is_locked
        if is_pro is not UNSET:
            field_dict["is_pro"] = is_pro
        if locked_until is not UNSET:
            field_dict["locked_until"] = locked_until
        if steamid is not UNSET:
            field_dict["steamid"] = steamid
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if avatarmedium is not UNSET:
            field_dict["avatarmedium"] = avatarmedium
        if avatarfull is not UNSET:
            field_dict["avatarfull"] = avatarfull
        if profileurl is not UNSET:
            field_dict["profileurl"] = profileurl
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if full_history_time is not UNSET:
            field_dict["full_history_time"] = full_history_time
        if cheese is not UNSET:
            field_dict["cheese"] = cheese
        if fh_unavailable is not UNSET:
            field_dict["fh_unavailable"] = fh_unavailable
        if loccountrycode is not UNSET:
            field_dict["loccountrycode"] = loccountrycode
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        name = d.pop("name", UNSET)

        country_code = d.pop("country_code", UNSET)

        fantasy_role = d.pop("fantasy_role", UNSET)

        team_id = d.pop("team_id", UNSET)

        team_name = d.pop("team_name", UNSET)

        team_tag = d.pop("team_tag", UNSET)

        is_locked = d.pop("is_locked", UNSET)

        is_pro = d.pop("is_pro", UNSET)

        locked_until = d.pop("locked_until", UNSET)

        steamid = d.pop("steamid", UNSET)

        avatar = d.pop("avatar", UNSET)

        avatarmedium = d.pop("avatarmedium", UNSET)

        avatarfull = d.pop("avatarfull", UNSET)

        profileurl = d.pop("profileurl", UNSET)

        _last_login = d.pop("last_login", UNSET)
        last_login: Union[Unset, None, datetime.datetime]
        if _last_login is None:
            last_login = None
        elif isinstance(_last_login, Unset):
            last_login = UNSET
        else:
            last_login = isoparse(_last_login)

        _full_history_time = d.pop("full_history_time", UNSET)
        full_history_time: Union[Unset, None, datetime.datetime]
        if _full_history_time is None:
            full_history_time = None
        elif isinstance(_full_history_time, Unset):
            full_history_time = UNSET
        else:
            full_history_time = isoparse(_full_history_time)

        cheese = d.pop("cheese", UNSET)

        fh_unavailable = d.pop("fh_unavailable", UNSET)

        loccountrycode = d.pop("loccountrycode", UNSET)

        last_played = d.pop("last_played", UNSET)

        win = d.pop("win", UNSET)

        games = d.pop("games", UNSET)

        with_win = d.pop("with_win", UNSET)

        with_games = d.pop("with_games", UNSET)

        against_win = d.pop("against_win", UNSET)

        against_games = d.pop("against_games", UNSET)

        with_gpm_sum = d.pop("with_gpm_sum", UNSET)

        with_xpm_sum = d.pop("with_xpm_sum", UNSET)

        player_pros_response = cls(
            account_id=account_id,
            name=name,
            country_code=country_code,
            fantasy_role=fantasy_role,
            team_id=team_id,
            team_name=team_name,
            team_tag=team_tag,
            is_locked=is_locked,
            is_pro=is_pro,
            locked_until=locked_until,
            steamid=steamid,
            avatar=avatar,
            avatarmedium=avatarmedium,
            avatarfull=avatarfull,
            profileurl=profileurl,
            last_login=last_login,
            full_history_time=full_history_time,
            cheese=cheese,
            fh_unavailable=fh_unavailable,
            loccountrycode=loccountrycode,
            last_played=last_played,
            win=win,
            games=games,
            with_win=with_win,
            with_games=with_games,
            against_win=against_win,
            against_games=against_games,
            with_gpm_sum=with_gpm_sum,
            with_xpm_sum=with_xpm_sum,
        )

        player_pros_response.additional_properties = d
        return player_pros_response

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
