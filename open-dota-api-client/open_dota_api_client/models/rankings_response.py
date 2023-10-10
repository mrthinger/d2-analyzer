from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rankings_response_rankings_item import RankingsResponseRankingsItem


T = TypeVar("T", bound="RankingsResponse")


@_attrs_define
class RankingsResponse:
    """
    Attributes:
        hero_id (Union[Unset, int]): The ID value of the hero played
        rankings (Union[Unset, List['RankingsResponseRankingsItem']]): rankings
    """

    hero_id: Union[Unset, int] = UNSET
    rankings: Union[Unset, List["RankingsResponseRankingsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hero_id = self.hero_id
        rankings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rankings, Unset):
            rankings = []
            for rankings_item_data in self.rankings:
                rankings_item = rankings_item_data.to_dict()

                rankings.append(rankings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if rankings is not UNSET:
            field_dict["rankings"] = rankings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rankings_response_rankings_item import RankingsResponseRankingsItem

        d = src_dict.copy()
        hero_id = d.pop("hero_id", UNSET)

        rankings = []
        _rankings = d.pop("rankings", UNSET)
        for rankings_item_data in _rankings or []:
            rankings_item = RankingsResponseRankingsItem.from_dict(rankings_item_data)

            rankings.append(rankings_item)

        rankings_response = cls(
            hero_id=hero_id,
            rankings=rankings,
        )

        rankings_response.additional_properties = d
        return rankings_response

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
