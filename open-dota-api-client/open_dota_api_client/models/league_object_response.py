from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeagueObjectResponse")


@_attrs_define
class LeagueObjectResponse:
    """
    Attributes:
        leagueid (Union[Unset, int]): leagueid
        ticket (Union[Unset, str]): ticket
        banner (Union[Unset, str]): banner
        tier (Union[Unset, str]): tier
        name (Union[Unset, str]): League name Example: ASUS ROG DreamLeague Season 4.
    """

    leagueid: Union[Unset, int] = UNSET
    ticket: Union[Unset, str] = UNSET
    banner: Union[Unset, str] = UNSET
    tier: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        leagueid = self.leagueid
        ticket = self.ticket
        banner = self.banner
        tier = self.tier
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if leagueid is not UNSET:
            field_dict["leagueid"] = leagueid
        if ticket is not UNSET:
            field_dict["ticket"] = ticket
        if banner is not UNSET:
            field_dict["banner"] = banner
        if tier is not UNSET:
            field_dict["tier"] = tier
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        leagueid = d.pop("leagueid", UNSET)

        ticket = d.pop("ticket", UNSET)

        banner = d.pop("banner", UNSET)

        tier = d.pop("tier", UNSET)

        name = d.pop("name", UNSET)

        league_object_response = cls(
            leagueid=leagueid,
            ticket=ticket,
            banner=banner,
            tier=tier,
            name=name,
        )

        league_object_response.additional_properties = d
        return league_object_response

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
