import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchResponsePlayersItemCosmeticsItem")


@_attrs_define
class MatchResponsePlayersItemCosmeticsItem:
    """
    Attributes:
        item_id (Union[Unset, int]):
        name (Union[Unset, None, str]): name
        prefab (Union[Unset, str]):
        creation_date (Union[Unset, None, datetime.datetime]):
        image_inventory (Union[Unset, None, str]):
        image_path (Union[Unset, None, str]):
        item_description (Union[Unset, None, str]):
        item_name (Union[Unset, str]):
        item_rarity (Union[Unset, None, str]):
        item_type_name (Union[Unset, None, str]):
        used_by_heroes (Union[Unset, None, str]):
    """

    item_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    prefab: Union[Unset, str] = UNSET
    creation_date: Union[Unset, None, datetime.datetime] = UNSET
    image_inventory: Union[Unset, None, str] = UNSET
    image_path: Union[Unset, None, str] = UNSET
    item_description: Union[Unset, None, str] = UNSET
    item_name: Union[Unset, str] = UNSET
    item_rarity: Union[Unset, None, str] = UNSET
    item_type_name: Union[Unset, None, str] = UNSET
    used_by_heroes: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_id = self.item_id
        name = self.name
        prefab = self.prefab
        creation_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat() if self.creation_date else None

        image_inventory = self.image_inventory
        image_path = self.image_path
        item_description = self.item_description
        item_name = self.item_name
        item_rarity = self.item_rarity
        item_type_name = self.item_type_name
        used_by_heroes = self.used_by_heroes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_id is not UNSET:
            field_dict["item_id"] = item_id
        if name is not UNSET:
            field_dict["name"] = name
        if prefab is not UNSET:
            field_dict["prefab"] = prefab
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if image_inventory is not UNSET:
            field_dict["image_inventory"] = image_inventory
        if image_path is not UNSET:
            field_dict["image_path"] = image_path
        if item_description is not UNSET:
            field_dict["item_description"] = item_description
        if item_name is not UNSET:
            field_dict["item_name"] = item_name
        if item_rarity is not UNSET:
            field_dict["item_rarity"] = item_rarity
        if item_type_name is not UNSET:
            field_dict["item_type_name"] = item_type_name
        if used_by_heroes is not UNSET:
            field_dict["used_by_heroes"] = used_by_heroes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_id = d.pop("item_id", UNSET)

        name = d.pop("name", UNSET)

        prefab = d.pop("prefab", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, None, datetime.datetime]
        if _creation_date is None:
            creation_date = None
        elif isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        image_inventory = d.pop("image_inventory", UNSET)

        image_path = d.pop("image_path", UNSET)

        item_description = d.pop("item_description", UNSET)

        item_name = d.pop("item_name", UNSET)

        item_rarity = d.pop("item_rarity", UNSET)

        item_type_name = d.pop("item_type_name", UNSET)

        used_by_heroes = d.pop("used_by_heroes", UNSET)

        match_response_players_item_cosmetics_item = cls(
            item_id=item_id,
            name=name,
            prefab=prefab,
            creation_date=creation_date,
            image_inventory=image_inventory,
            image_path=image_path,
            item_description=item_description,
            item_name=item_name,
            item_rarity=item_rarity,
            item_type_name=item_type_name,
            used_by_heroes=used_by_heroes,
        )

        match_response_players_item_cosmetics_item.additional_properties = d
        return match_response_players_item_cosmetics_item

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
