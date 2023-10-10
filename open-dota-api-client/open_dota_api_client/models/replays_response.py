from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplaysResponse")


@_attrs_define
class ReplaysResponse:
    """
    Attributes:
        match_id (Union[Unset, int]): The ID number of the match assigned by Valve Example: 3703866531.
        cluster (Union[Unset, int]): cluster
        replay_salt (Union[Unset, int]): replay_salt
    """

    match_id: Union[Unset, int] = UNSET
    cluster: Union[Unset, int] = UNSET
    replay_salt: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        match_id = self.match_id
        cluster = self.cluster
        replay_salt = self.replay_salt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_id is not UNSET:
            field_dict["match_id"] = match_id
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if replay_salt is not UNSET:
            field_dict["replay_salt"] = replay_salt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        match_id = d.pop("match_id", UNSET)

        cluster = d.pop("cluster", UNSET)

        replay_salt = d.pop("replay_salt", UNSET)

        replays_response = cls(
            match_id=match_id,
            cluster=cluster,
            replay_salt=replay_salt,
        )

        replays_response.additional_properties = d
        return replays_response

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
