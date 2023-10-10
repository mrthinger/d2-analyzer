from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeroObjectResponse")


@_attrs_define
class HeroObjectResponse:
    """
    Attributes:
        id (int): The ID value of the hero played
        name (Union[Unset, str]): Dota hero command name Example: npc_dota_hero_antimage.
        localized_name (Union[Unset, str]): Hero name Example: Anti-Mage.
        primary_attr (Union[Unset, str]): Hero primary shorthand attribute name, e.g. 'agi'
        attack_type (Union[Unset, str]): Hero attack type, either 'Melee' or 'Ranged'
        roles (Union[Unset, List[str]]):
    """

    id: int
    name: Union[Unset, str] = UNSET
    localized_name: Union[Unset, str] = UNSET
    primary_attr: Union[Unset, str] = UNSET
    attack_type: Union[Unset, str] = UNSET
    roles: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        localized_name = self.localized_name
        primary_attr = self.primary_attr
        attack_type = self.attack_type
        roles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if localized_name is not UNSET:
            field_dict["localized_name"] = localized_name
        if primary_attr is not UNSET:
            field_dict["primary_attr"] = primary_attr
        if attack_type is not UNSET:
            field_dict["attack_type"] = attack_type
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        localized_name = d.pop("localized_name", UNSET)

        primary_attr = d.pop("primary_attr", UNSET)

        attack_type = d.pop("attack_type", UNSET)

        roles = cast(List[str], d.pop("roles", UNSET))

        hero_object_response = cls(
            id=id,
            name=name,
            localized_name=localized_name,
            primary_attr=primary_attr,
            attack_type=attack_type,
            roles=roles,
        )

        hero_object_response.additional_properties = d
        return hero_object_response

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
