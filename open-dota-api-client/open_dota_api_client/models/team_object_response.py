from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamObjectResponse")


@_attrs_define
class TeamObjectResponse:
    """
    Attributes:
        team_id (Union[Unset, int]): Team's identifier
        rating (Union[Unset, float]): The Elo rating of the team
        wins (Union[Unset, int]): The number of games won by this team
        losses (Union[Unset, int]): The number of losses by this team
        last_match_time (Union[Unset, int]): The Unix timestamp of the last match played by this team
        name (Union[Unset, None, str]): Team name Example: Newbee.
        tag (Union[Unset, str]): The team tag/abbreviation
    """

    team_id: Union[Unset, int] = UNSET
    rating: Union[Unset, float] = UNSET
    wins: Union[Unset, int] = UNSET
    losses: Union[Unset, int] = UNSET
    last_match_time: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    tag: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_id = self.team_id
        rating = self.rating
        wins = self.wins
        losses = self.losses
        last_match_time = self.last_match_time
        name = self.name
        tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if rating is not UNSET:
            field_dict["rating"] = rating
        if wins is not UNSET:
            field_dict["wins"] = wins
        if losses is not UNSET:
            field_dict["losses"] = losses
        if last_match_time is not UNSET:
            field_dict["last_match_time"] = last_match_time
        if name is not UNSET:
            field_dict["name"] = name
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        team_id = d.pop("team_id", UNSET)

        rating = d.pop("rating", UNSET)

        wins = d.pop("wins", UNSET)

        losses = d.pop("losses", UNSET)

        last_match_time = d.pop("last_match_time", UNSET)

        name = d.pop("name", UNSET)

        tag = d.pop("tag", UNSET)

        team_object_response = cls(
            team_id=team_id,
            rating=rating,
            wins=wins,
            losses=losses,
            last_match_time=last_match_time,
            name=name,
            tag=tag,
        )

        team_object_response.additional_properties = d
        return team_object_response

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
