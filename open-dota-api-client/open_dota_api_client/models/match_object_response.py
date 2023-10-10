from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchObjectResponse")


@_attrs_define
class MatchObjectResponse:
    """
    Attributes:
        match_id (Union[Unset, int]): The ID number of the match assigned by Valve Example: 3703866531.
        duration (Union[Unset, int]): Duration of the game in seconds
        start_time (Union[Unset, int]): The Unix timestamp at which the game started
        radiant_team_id (Union[Unset, int]): The Radiant's team_id
        radiant_name (Union[Unset, str]): The Radiant's team name
        dire_team_id (Union[Unset, int]): The Dire's team_id
        dire_name (Union[Unset, str]): The Dire's team name
        leagueid (Union[Unset, int]): Identifier for the league the match took place in
        league_name (Union[Unset, str]): Name of league the match took place in
        series_id (Union[Unset, int]): Identifier for the series of the match
        series_type (Union[Unset, int]): Type of series the match was
        radiant_score (Union[Unset, int]): Number of kills the Radiant team had when the match ended
        dire_score (Union[Unset, int]): Number of kills the Dire team had when the match ended
        radiant_win (Union[Unset, None, bool]): Boolean indicating whether Radiant won the match
        radiant (Union[Unset, bool]): Whether the team/player/hero was on Radiant
    """

    match_id: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    start_time: Union[Unset, int] = UNSET
    radiant_team_id: Union[Unset, int] = UNSET
    radiant_name: Union[Unset, str] = UNSET
    dire_team_id: Union[Unset, int] = UNSET
    dire_name: Union[Unset, str] = UNSET
    leagueid: Union[Unset, int] = UNSET
    league_name: Union[Unset, str] = UNSET
    series_id: Union[Unset, int] = UNSET
    series_type: Union[Unset, int] = UNSET
    radiant_score: Union[Unset, int] = UNSET
    dire_score: Union[Unset, int] = UNSET
    radiant_win: Union[Unset, None, bool] = UNSET
    radiant: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        match_id = self.match_id
        duration = self.duration
        start_time = self.start_time
        radiant_team_id = self.radiant_team_id
        radiant_name = self.radiant_name
        dire_team_id = self.dire_team_id
        dire_name = self.dire_name
        leagueid = self.leagueid
        league_name = self.league_name
        series_id = self.series_id
        series_type = self.series_type
        radiant_score = self.radiant_score
        dire_score = self.dire_score
        radiant_win = self.radiant_win
        radiant = self.radiant

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_id is not UNSET:
            field_dict["match_id"] = match_id
        if duration is not UNSET:
            field_dict["duration"] = duration
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if radiant_team_id is not UNSET:
            field_dict["radiant_team_id"] = radiant_team_id
        if radiant_name is not UNSET:
            field_dict["radiant_name"] = radiant_name
        if dire_team_id is not UNSET:
            field_dict["dire_team_id"] = dire_team_id
        if dire_name is not UNSET:
            field_dict["dire_name"] = dire_name
        if leagueid is not UNSET:
            field_dict["leagueid"] = leagueid
        if league_name is not UNSET:
            field_dict["league_name"] = league_name
        if series_id is not UNSET:
            field_dict["series_id"] = series_id
        if series_type is not UNSET:
            field_dict["series_type"] = series_type
        if radiant_score is not UNSET:
            field_dict["radiant_score"] = radiant_score
        if dire_score is not UNSET:
            field_dict["dire_score"] = dire_score
        if radiant_win is not UNSET:
            field_dict["radiant_win"] = radiant_win
        if radiant is not UNSET:
            field_dict["radiant"] = radiant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        match_id = d.pop("match_id", UNSET)

        duration = d.pop("duration", UNSET)

        start_time = d.pop("start_time", UNSET)

        radiant_team_id = d.pop("radiant_team_id", UNSET)

        radiant_name = d.pop("radiant_name", UNSET)

        dire_team_id = d.pop("dire_team_id", UNSET)

        dire_name = d.pop("dire_name", UNSET)

        leagueid = d.pop("leagueid", UNSET)

        league_name = d.pop("league_name", UNSET)

        series_id = d.pop("series_id", UNSET)

        series_type = d.pop("series_type", UNSET)

        radiant_score = d.pop("radiant_score", UNSET)

        dire_score = d.pop("dire_score", UNSET)

        radiant_win = d.pop("radiant_win", UNSET)

        radiant = d.pop("radiant", UNSET)

        match_object_response = cls(
            match_id=match_id,
            duration=duration,
            start_time=start_time,
            radiant_team_id=radiant_team_id,
            radiant_name=radiant_name,
            dire_team_id=dire_team_id,
            dire_name=dire_name,
            leagueid=leagueid,
            league_name=league_name,
            series_id=series_id,
            series_type=series_type,
            radiant_score=radiant_score,
            dire_score=dire_score,
            radiant_win=radiant_win,
            radiant=radiant,
        )

        match_object_response.additional_properties = d
        return match_object_response

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
