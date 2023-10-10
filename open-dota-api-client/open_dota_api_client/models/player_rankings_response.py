from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerRankingsResponse")


@_attrs_define
class PlayerRankingsResponse:
    """
    Attributes:
        hero_id (Union[Unset, int]): The ID value of the hero played
        score (Union[Unset, float]): Hero score
        percent_rank (Union[Unset, float]): percent_rank
        card (Union[Unset, int]): numeric_rank
    """

    hero_id: Union[Unset, int] = UNSET
    score: Union[Unset, float] = UNSET
    percent_rank: Union[Unset, float] = UNSET
    card: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hero_id = self.hero_id
        score = self.score
        percent_rank = self.percent_rank
        card = self.card

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if score is not UNSET:
            field_dict["score"] = score
        if percent_rank is not UNSET:
            field_dict["percent_rank"] = percent_rank
        if card is not UNSET:
            field_dict["card"] = card

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hero_id = d.pop("hero_id", UNSET)

        score = d.pop("score", UNSET)

        percent_rank = d.pop("percent_rank", UNSET)

        card = d.pop("card", UNSET)

        player_rankings_response = cls(
            hero_id=hero_id,
            score=score,
            percent_rank=percent_rank,
            card=card,
        )

        player_rankings_response.additional_properties = d
        return player_rankings_response

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
