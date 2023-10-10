from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordsResponse")


@_attrs_define
class RecordsResponse:
    """
    Attributes:
        match_id (Union[Unset, int]): The ID number of the match assigned by Valve Example: 3703866531.
        start_time (Union[Unset, int]): The Unix timestamp at which the game started
        hero_id (Union[Unset, int]): The ID value of the hero played
        score (Union[Unset, int]): Record score
    """

    match_id: Union[Unset, int] = UNSET
    start_time: Union[Unset, int] = UNSET
    hero_id: Union[Unset, int] = UNSET
    score: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        match_id = self.match_id
        start_time = self.start_time
        hero_id = self.hero_id
        score = self.score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_id is not UNSET:
            field_dict["match_id"] = match_id
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        match_id = d.pop("match_id", UNSET)

        start_time = d.pop("start_time", UNSET)

        hero_id = d.pop("hero_id", UNSET)

        score = d.pop("score", UNSET)

        records_response = cls(
            match_id=match_id,
            start_time=start_time,
            hero_id=hero_id,
            score=score,
        )

        records_response.additional_properties = d
        return records_response

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
