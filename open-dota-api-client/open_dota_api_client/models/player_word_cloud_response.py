from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_word_cloud_response_all_word_counts import PlayerWordCloudResponseAllWordCounts
    from ..models.player_word_cloud_response_my_word_counts import PlayerWordCloudResponseMyWordCounts


T = TypeVar("T", bound="PlayerWordCloudResponse")


@_attrs_define
class PlayerWordCloudResponse:
    """
    Attributes:
        my_word_counts (Union[Unset, PlayerWordCloudResponseMyWordCounts]): my_word_counts
        all_word_counts (Union[Unset, PlayerWordCloudResponseAllWordCounts]): all_word_counts
    """

    my_word_counts: Union[Unset, "PlayerWordCloudResponseMyWordCounts"] = UNSET
    all_word_counts: Union[Unset, "PlayerWordCloudResponseAllWordCounts"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        my_word_counts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.my_word_counts, Unset):
            my_word_counts = self.my_word_counts.to_dict()

        all_word_counts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.all_word_counts, Unset):
            all_word_counts = self.all_word_counts.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if my_word_counts is not UNSET:
            field_dict["my_word_counts"] = my_word_counts
        if all_word_counts is not UNSET:
            field_dict["all_word_counts"] = all_word_counts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player_word_cloud_response_all_word_counts import PlayerWordCloudResponseAllWordCounts
        from ..models.player_word_cloud_response_my_word_counts import PlayerWordCloudResponseMyWordCounts

        d = src_dict.copy()
        _my_word_counts = d.pop("my_word_counts", UNSET)
        my_word_counts: Union[Unset, PlayerWordCloudResponseMyWordCounts]
        if isinstance(_my_word_counts, Unset):
            my_word_counts = UNSET
        else:
            my_word_counts = PlayerWordCloudResponseMyWordCounts.from_dict(_my_word_counts)

        _all_word_counts = d.pop("all_word_counts", UNSET)
        all_word_counts: Union[Unset, PlayerWordCloudResponseAllWordCounts]
        if isinstance(_all_word_counts, Unset):
            all_word_counts = UNSET
        else:
            all_word_counts = PlayerWordCloudResponseAllWordCounts.from_dict(_all_word_counts)

        player_word_cloud_response = cls(
            my_word_counts=my_word_counts,
            all_word_counts=all_word_counts,
        )

        player_word_cloud_response.additional_properties = d
        return player_word_cloud_response

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
