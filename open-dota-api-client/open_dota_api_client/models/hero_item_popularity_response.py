from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hero_item_popularity_response_early_game_items import HeroItemPopularityResponseEarlyGameItems
    from ..models.hero_item_popularity_response_late_game_items import HeroItemPopularityResponseLateGameItems
    from ..models.hero_item_popularity_response_mid_game_items import HeroItemPopularityResponseMidGameItems
    from ..models.hero_item_popularity_response_start_game_items import HeroItemPopularityResponseStartGameItems


T = TypeVar("T", bound="HeroItemPopularityResponse")


@_attrs_define
class HeroItemPopularityResponse:
    """
    Attributes:
        start_game_items (Union[Unset, HeroItemPopularityResponseStartGameItems]): Items bought before game started
        early_game_items (Union[Unset, HeroItemPopularityResponseEarlyGameItems]): Items bought in the first 10 min of
            the game, with cost at least 700
        mid_game_items (Union[Unset, HeroItemPopularityResponseMidGameItems]): Items bought between 10 and 25 min of the
            game, with cost at least 2000
        late_game_items (Union[Unset, HeroItemPopularityResponseLateGameItems]): Items bought at least 25 min after game
            started, with cost at least 4000
    """

    start_game_items: Union[Unset, "HeroItemPopularityResponseStartGameItems"] = UNSET
    early_game_items: Union[Unset, "HeroItemPopularityResponseEarlyGameItems"] = UNSET
    mid_game_items: Union[Unset, "HeroItemPopularityResponseMidGameItems"] = UNSET
    late_game_items: Union[Unset, "HeroItemPopularityResponseLateGameItems"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_game_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start_game_items, Unset):
            start_game_items = self.start_game_items.to_dict()

        early_game_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.early_game_items, Unset):
            early_game_items = self.early_game_items.to_dict()

        mid_game_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mid_game_items, Unset):
            mid_game_items = self.mid_game_items.to_dict()

        late_game_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.late_game_items, Unset):
            late_game_items = self.late_game_items.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_game_items is not UNSET:
            field_dict["start_game_items"] = start_game_items
        if early_game_items is not UNSET:
            field_dict["early_game_items"] = early_game_items
        if mid_game_items is not UNSET:
            field_dict["mid_game_items"] = mid_game_items
        if late_game_items is not UNSET:
            field_dict["late_game_items"] = late_game_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hero_item_popularity_response_early_game_items import HeroItemPopularityResponseEarlyGameItems
        from ..models.hero_item_popularity_response_late_game_items import HeroItemPopularityResponseLateGameItems
        from ..models.hero_item_popularity_response_mid_game_items import HeroItemPopularityResponseMidGameItems
        from ..models.hero_item_popularity_response_start_game_items import HeroItemPopularityResponseStartGameItems

        d = src_dict.copy()
        _start_game_items = d.pop("start_game_items", UNSET)
        start_game_items: Union[Unset, HeroItemPopularityResponseStartGameItems]
        if isinstance(_start_game_items, Unset):
            start_game_items = UNSET
        else:
            start_game_items = HeroItemPopularityResponseStartGameItems.from_dict(_start_game_items)

        _early_game_items = d.pop("early_game_items", UNSET)
        early_game_items: Union[Unset, HeroItemPopularityResponseEarlyGameItems]
        if isinstance(_early_game_items, Unset):
            early_game_items = UNSET
        else:
            early_game_items = HeroItemPopularityResponseEarlyGameItems.from_dict(_early_game_items)

        _mid_game_items = d.pop("mid_game_items", UNSET)
        mid_game_items: Union[Unset, HeroItemPopularityResponseMidGameItems]
        if isinstance(_mid_game_items, Unset):
            mid_game_items = UNSET
        else:
            mid_game_items = HeroItemPopularityResponseMidGameItems.from_dict(_mid_game_items)

        _late_game_items = d.pop("late_game_items", UNSET)
        late_game_items: Union[Unset, HeroItemPopularityResponseLateGameItems]
        if isinstance(_late_game_items, Unset):
            late_game_items = UNSET
        else:
            late_game_items = HeroItemPopularityResponseLateGameItems.from_dict(_late_game_items)

        hero_item_popularity_response = cls(
            start_game_items=start_game_items,
            early_game_items=early_game_items,
            mid_game_items=mid_game_items,
            late_game_items=late_game_items,
        )

        hero_item_popularity_response.additional_properties = d
        return hero_item_popularity_response

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
