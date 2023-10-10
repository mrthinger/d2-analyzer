from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerResponseProfile")


@_attrs_define
class PlayerResponseProfile:
    """profile

    Attributes:
        account_id (Union[Unset, int]): The player account ID
        personaname (Union[Unset, None, str]): Player's Steam name Example: 420 booty wizard.
        name (Union[Unset, None, str]): name
        plus (Union[Unset, bool]): Boolean indicating status of current Dota Plus subscription
        cheese (Union[Unset, None, int]): cheese
        steamid (Union[Unset, None, str]): steamid
        avatar (Union[Unset, None, str]): avatar
        avatarmedium (Union[Unset, None, str]): avatarmedium
        avatarfull (Union[Unset, None, str]): avatarfull
        profileurl (Union[Unset, None, str]): profileurl
        last_login (Union[Unset, None, str]): last_login
        loccountrycode (Union[Unset, None, str]): loccountrycode
        is_contributor (Union[Unset, bool]): Boolean indicating if the user contributed to the development of OpenDota
        is_subscriber (Union[Unset, bool]): Boolean indicating if the user subscribed to OpenDota
    """

    account_id: Union[Unset, int] = UNSET
    personaname: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    plus: Union[Unset, bool] = UNSET
    cheese: Union[Unset, None, int] = UNSET
    steamid: Union[Unset, None, str] = UNSET
    avatar: Union[Unset, None, str] = UNSET
    avatarmedium: Union[Unset, None, str] = UNSET
    avatarfull: Union[Unset, None, str] = UNSET
    profileurl: Union[Unset, None, str] = UNSET
    last_login: Union[Unset, None, str] = UNSET
    loccountrycode: Union[Unset, None, str] = UNSET
    is_contributor: Union[Unset, bool] = False
    is_subscriber: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        personaname = self.personaname
        name = self.name
        plus = self.plus
        cheese = self.cheese
        steamid = self.steamid
        avatar = self.avatar
        avatarmedium = self.avatarmedium
        avatarfull = self.avatarfull
        profileurl = self.profileurl
        last_login = self.last_login
        loccountrycode = self.loccountrycode
        is_contributor = self.is_contributor
        is_subscriber = self.is_subscriber

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if personaname is not UNSET:
            field_dict["personaname"] = personaname
        if name is not UNSET:
            field_dict["name"] = name
        if plus is not UNSET:
            field_dict["plus"] = plus
        if cheese is not UNSET:
            field_dict["cheese"] = cheese
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
        if loccountrycode is not UNSET:
            field_dict["loccountrycode"] = loccountrycode
        if is_contributor is not UNSET:
            field_dict["is_contributor"] = is_contributor
        if is_subscriber is not UNSET:
            field_dict["is_subscriber"] = is_subscriber

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        personaname = d.pop("personaname", UNSET)

        name = d.pop("name", UNSET)

        plus = d.pop("plus", UNSET)

        cheese = d.pop("cheese", UNSET)

        steamid = d.pop("steamid", UNSET)

        avatar = d.pop("avatar", UNSET)

        avatarmedium = d.pop("avatarmedium", UNSET)

        avatarfull = d.pop("avatarfull", UNSET)

        profileurl = d.pop("profileurl", UNSET)

        last_login = d.pop("last_login", UNSET)

        loccountrycode = d.pop("loccountrycode", UNSET)

        is_contributor = d.pop("is_contributor", UNSET)

        is_subscriber = d.pop("is_subscriber", UNSET)

        player_response_profile = cls(
            account_id=account_id,
            personaname=personaname,
            name=name,
            plus=plus,
            cheese=cheese,
            steamid=steamid,
            avatar=avatar,
            avatarmedium=avatarmedium,
            avatarfull=avatarfull,
            profileurl=profileurl,
            last_login=last_login,
            loccountrycode=loccountrycode,
            is_contributor=is_contributor,
            is_subscriber=is_subscriber,
        )

        player_response_profile.additional_properties = d
        return player_response_profile

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
