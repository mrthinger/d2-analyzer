import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RankingsResponseRankingsItem")


@_attrs_define
class RankingsResponseRankingsItem:
    """
    Attributes:
        account_id (Union[Unset, int]): The player account ID
        score (Union[Unset, float]): Score
        steamid (Union[Unset, None, str]): steamid
        avatar (Union[Unset, None, str]): avatar
        avatarmedium (Union[Unset, None, str]): avatarmedium
        avatarfull (Union[Unset, None, str]): avatarfull
        profileurl (Union[Unset, None, str]): profileurl
        personaname (Union[Unset, None, str]): Player's Steam name Example: 420 booty wizard.
        last_login (Union[Unset, None, datetime.datetime]): last_login
        full_history_time (Union[Unset, datetime.datetime]): full_history_time
        cheese (Union[Unset, None, int]): cheese
        fh_unavailable (Union[Unset, None, bool]): fh_unavailable
        loccountrycode (Union[Unset, None, str]): loccountrycode
        rank_tier (Union[Unset, None, int]): rank_tier
    """

    account_id: Union[Unset, int] = UNSET
    score: Union[Unset, float] = UNSET
    steamid: Union[Unset, None, str] = UNSET
    avatar: Union[Unset, None, str] = UNSET
    avatarmedium: Union[Unset, None, str] = UNSET
    avatarfull: Union[Unset, None, str] = UNSET
    profileurl: Union[Unset, None, str] = UNSET
    personaname: Union[Unset, None, str] = UNSET
    last_login: Union[Unset, None, datetime.datetime] = UNSET
    full_history_time: Union[Unset, datetime.datetime] = UNSET
    cheese: Union[Unset, None, int] = UNSET
    fh_unavailable: Union[Unset, None, bool] = UNSET
    loccountrycode: Union[Unset, None, str] = UNSET
    rank_tier: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        score = self.score
        steamid = self.steamid
        avatar = self.avatar
        avatarmedium = self.avatarmedium
        avatarfull = self.avatarfull
        profileurl = self.profileurl
        personaname = self.personaname
        last_login: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_login, Unset):
            last_login = self.last_login.isoformat() if self.last_login else None

        full_history_time: Union[Unset, str] = UNSET
        if not isinstance(self.full_history_time, Unset):
            full_history_time = self.full_history_time.isoformat()

        cheese = self.cheese
        fh_unavailable = self.fh_unavailable
        loccountrycode = self.loccountrycode
        rank_tier = self.rank_tier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if score is not UNSET:
            field_dict["score"] = score
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
        if rank_tier is not UNSET:
            field_dict["rank_tier"] = rank_tier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        score = d.pop("score", UNSET)

        steamid = d.pop("steamid", UNSET)

        avatar = d.pop("avatar", UNSET)

        avatarmedium = d.pop("avatarmedium", UNSET)

        avatarfull = d.pop("avatarfull", UNSET)

        profileurl = d.pop("profileurl", UNSET)

        personaname = d.pop("personaname", UNSET)

        _last_login = d.pop("last_login", UNSET)
        last_login: Union[Unset, None, datetime.datetime]
        if _last_login is None:
            last_login = None
        elif isinstance(_last_login, Unset):
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

        rank_tier = d.pop("rank_tier", UNSET)

        rankings_response_rankings_item = cls(
            account_id=account_id,
            score=score,
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
            rank_tier=rank_tier,
        )

        rankings_response_rankings_item.additional_properties = d
        return rankings_response_rankings_item

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
