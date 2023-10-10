from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResponse")


@_attrs_define
class SearchResponse:
    """
    Attributes:
        account_id (Union[Unset, int]): The player account ID
        avatarfull (Union[Unset, None, str]): avatarfull
        personaname (Union[Unset, None, str]): Player's Steam name Example: 420 booty wizard.
        last_match_time (Union[Unset, str]): last_match_time. May not be present or null.
        similarity (Union[Unset, float]): similarity
    """

    account_id: Union[Unset, int] = UNSET
    avatarfull: Union[Unset, None, str] = UNSET
    personaname: Union[Unset, None, str] = UNSET
    last_match_time: Union[Unset, str] = UNSET
    similarity: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        avatarfull = self.avatarfull
        personaname = self.personaname
        last_match_time = self.last_match_time
        similarity = self.similarity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if avatarfull is not UNSET:
            field_dict["avatarfull"] = avatarfull
        if personaname is not UNSET:
            field_dict["personaname"] = personaname
        if last_match_time is not UNSET:
            field_dict["last_match_time"] = last_match_time
        if similarity is not UNSET:
            field_dict["similarity"] = similarity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        avatarfull = d.pop("avatarfull", UNSET)

        personaname = d.pop("personaname", UNSET)

        last_match_time = d.pop("last_match_time", UNSET)

        similarity = d.pop("similarity", UNSET)

        search_response = cls(
            account_id=account_id,
            avatarfull=avatarfull,
            personaname=personaname,
            last_match_time=last_match_time,
            similarity=similarity,
        )

        search_response.additional_properties = d
        return search_response

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
