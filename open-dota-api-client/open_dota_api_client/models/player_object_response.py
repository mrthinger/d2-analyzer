import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerObjectResponse")


@_attrs_define
class PlayerObjectResponse:
    """
    Attributes:
        account_id (Union[Unset, int]): The player account ID
        steamid (Union[Unset, str]): Player's steam identifier
        avatar (Union[Unset, str]): Steam picture URL (small picture)
        avatarmedium (Union[Unset, str]): Steam picture URL (medium picture)
        avatarfull (Union[Unset, str]): Steam picture URL (full picture)
        profileurl (Union[Unset, str]): Steam profile URL
        personaname (Union[Unset, None, str]): Player's Steam name Example: 420 booty wizard.
        last_login (Union[Unset, datetime.datetime]): Date and time of last login to OpenDota
        full_history_time (Union[Unset, datetime.datetime]): Date and time of last request to refresh player's match
            history
        cheese (Union[Unset, int]): Amount of dollars the player has donated to OpenDota
        fh_unavailable (Union[Unset, bool]): Whether the refresh of player' match history failed
        loccountrycode (Union[Unset, str]): Player's country identifier, e.g. US
        name (Union[Unset, str]): Verified player name, e.g. 'Miracle-'
        country_code (Union[Unset, str]): Player's country code
        fantasy_role (Union[Unset, int]): Player's ingame role (core: 1 or support: 2)
        team_id (Union[Unset, int]): Player's team identifier
        team_name (Union[Unset, None, str]): Team name Example: Newbee.
        team_tag (Union[Unset, str]): Player's team shorthand tag, e.g. 'EG'
        is_locked (Union[Unset, bool]): Whether the roster lock is active
        is_pro (Union[Unset, bool]): Whether the player is professional or not
        locked_until (Union[Unset, int]): When the roster lock will end
    """

    account_id: Union[Unset, int] = UNSET
    steamid: Union[Unset, str] = UNSET
    avatar: Union[Unset, str] = UNSET
    avatarmedium: Union[Unset, str] = UNSET
    avatarfull: Union[Unset, str] = UNSET
    profileurl: Union[Unset, str] = UNSET
    personaname: Union[Unset, None, str] = UNSET
    last_login: Union[Unset, datetime.datetime] = UNSET
    full_history_time: Union[Unset, datetime.datetime] = UNSET
    cheese: Union[Unset, int] = UNSET
    fh_unavailable: Union[Unset, bool] = UNSET
    loccountrycode: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    fantasy_role: Union[Unset, int] = UNSET
    team_id: Union[Unset, int] = UNSET
    team_name: Union[Unset, None, str] = UNSET
    team_tag: Union[Unset, str] = UNSET
    is_locked: Union[Unset, bool] = UNSET
    is_pro: Union[Unset, bool] = UNSET
    locked_until: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        steamid = self.steamid
        avatar = self.avatar
        avatarmedium = self.avatarmedium
        avatarfull = self.avatarfull
        profileurl = self.profileurl
        personaname = self.personaname
        last_login: Union[Unset, str] = UNSET
        if not isinstance(self.last_login, Unset):
            last_login = self.last_login.isoformat()

        full_history_time: Union[Unset, str] = UNSET
        if not isinstance(self.full_history_time, Unset):
            full_history_time = self.full_history_time.isoformat()

        cheese = self.cheese
        fh_unavailable = self.fh_unavailable
        loccountrycode = self.loccountrycode
        name = self.name
        country_code = self.country_code
        fantasy_role = self.fantasy_role
        team_id = self.team_id
        team_name = self.team_name
        team_tag = self.team_tag
        is_locked = self.is_locked
        is_pro = self.is_pro
        locked_until = self.locked_until

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
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
        if personaname is not UNSET:
            field_dict["personaname"] = personaname
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        steamid = d.pop("steamid", UNSET)

        avatar = d.pop("avatar", UNSET)

        avatarmedium = d.pop("avatarmedium", UNSET)

        avatarfull = d.pop("avatarfull", UNSET)

        profileurl = d.pop("profileurl", UNSET)

        personaname = d.pop("personaname", UNSET)

        _last_login = d.pop("last_login", UNSET)
        last_login: Union[Unset, datetime.datetime]
        if isinstance(_last_login, Unset):
            last_login = UNSET
        else:
            last_login = isoparse(_last_login)

        _full_history_time = d.pop("full_history_time", UNSET)
        full_history_time: Union[Unset, datetime.datetime]
        if isinstance(_full_history_time, Unset):
            full_history_time = UNSET
        else:
            full_history_time = isoparse(_full_history_time)

        cheese = d.pop("cheese", UNSET)

        fh_unavailable = d.pop("fh_unavailable", UNSET)

        loccountrycode = d.pop("loccountrycode", UNSET)

        name = d.pop("name", UNSET)

        country_code = d.pop("country_code", UNSET)

        fantasy_role = d.pop("fantasy_role", UNSET)

        team_id = d.pop("team_id", UNSET)

        team_name = d.pop("team_name", UNSET)

        team_tag = d.pop("team_tag", UNSET)

        is_locked = d.pop("is_locked", UNSET)

        is_pro = d.pop("is_pro", UNSET)

        locked_until = d.pop("locked_until", UNSET)

        player_object_response = cls(
            account_id=account_id,
            steamid=steamid,
            avatar=avatar,
            avatarmedium=avatarmedium,
            avatarfull=avatarfull,
            profileurl=profileurl,
            personaname=personaname,
            last_login=last_login,
            full_history_time=full_history_time,
            cheese=cheese,
            fh_unavailable=fh_unavailable,
            loccountrycode=loccountrycode,
            name=name,
            country_code=country_code,
            fantasy_role=fantasy_role,
            team_id=team_id,
            team_name=team_name,
            team_tag=team_tag,
            is_locked=is_locked,
            is_pro=is_pro,
            locked_until=locked_until,
        )

        player_object_response.additional_properties = d
        return player_object_response

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
