from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerRatingsResponse")


@_attrs_define
class PlayerRatingsResponse:
    """
    Attributes:
        account_id (Union[Unset, int]): The player account ID
        match_id (Union[Unset, int]): The ID number of the match assigned by Valve Example: 3703866531.
        solo_competitive_rank (Union[Unset, None, int]): solo_competitive_rank
        competitive_rank (Union[Unset, int]): competitive_rank
        time (Union[Unset, int]): time
    """

    account_id: Union[Unset, int] = UNSET
    match_id: Union[Unset, int] = UNSET
    solo_competitive_rank: Union[Unset, None, int] = UNSET
    competitive_rank: Union[Unset, int] = UNSET
    time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        match_id = self.match_id
        solo_competitive_rank = self.solo_competitive_rank
        competitive_rank = self.competitive_rank
        time = self.time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if match_id is not UNSET:
            field_dict["match_id"] = match_id
        if solo_competitive_rank is not UNSET:
            field_dict["solo_competitive_rank"] = solo_competitive_rank
        if competitive_rank is not UNSET:
            field_dict["competitive_rank"] = competitive_rank
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        match_id = d.pop("match_id", UNSET)

        solo_competitive_rank = d.pop("solo_competitive_rank", UNSET)

        competitive_rank = d.pop("competitive_rank", UNSET)

        time = d.pop("time", UNSET)

        player_ratings_response = cls(
            account_id=account_id,
            match_id=match_id,
            solo_competitive_rank=solo_competitive_rank,
            competitive_rank=competitive_rank,
            time=time,
        )

        player_ratings_response.additional_properties = d
        return player_ratings_response

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
