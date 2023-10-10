from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayersByRankResponseItem")


@_attrs_define
class PlayersByRankResponseItem:
    """
    Attributes:
        account_id (Union[Unset, int]): The player account ID
        rank_tier (Union[Unset, float]): Integer indicating the rank/medal of the player
        fh_unavailable (Union[Unset, None, bool]): Indicates if we were unable to fetch full history for this player due
            to privacy settings
    """

    account_id: Union[Unset, int] = UNSET
    rank_tier: Union[Unset, float] = UNSET
    fh_unavailable: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        rank_tier = self.rank_tier
        fh_unavailable = self.fh_unavailable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if rank_tier is not UNSET:
            field_dict["rank_tier"] = rank_tier
        if fh_unavailable is not UNSET:
            field_dict["fh_unavailable"] = fh_unavailable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        rank_tier = d.pop("rank_tier", UNSET)

        fh_unavailable = d.pop("fh_unavailable", UNSET)

        players_by_rank_response_item = cls(
            account_id=account_id,
            rank_tier=rank_tier,
            fh_unavailable=fh_unavailable,
        )

        players_by_rank_response_item.additional_properties = d
        return players_by_rank_response_item

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
