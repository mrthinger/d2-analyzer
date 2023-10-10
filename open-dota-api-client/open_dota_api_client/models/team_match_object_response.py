from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamMatchObjectResponse")


@_attrs_define
class TeamMatchObjectResponse:
    """
    Attributes:
        match_id (Union[Unset, int]): The ID number of the match assigned by Valve Example: 3703866531.
        radiant (Union[Unset, bool]): Whether the team/player/hero was on Radiant
        radiant_win (Union[Unset, None, bool]): Boolean indicating whether Radiant won the match
        radiant_score (Union[Unset, int]): Number of kills the Radiant team had when the match ended
        dire_score (Union[Unset, int]): Number of kills the Dire team had when the match ended
        duration (Union[Unset, int]): Duration of the game in seconds
        start_time (Union[Unset, int]): The Unix timestamp at which the game started
        leagueid (Union[Unset, int]): Identifier for the league the match took place in
        league_name (Union[Unset, str]): Name of league the match took place in
        cluster (Union[Unset, int]): cluster
        opposing_team_id (Union[Unset, int]): Opposing team identifier
        opposing_team_name (Union[Unset, None, str]): Opposing team name, e.g. 'Evil Geniuses'
        opposing_team_logo (Union[Unset, str]): Opposing team logo url
    """

    match_id: Union[Unset, int] = UNSET
    radiant: Union[Unset, bool] = UNSET
    radiant_win: Union[Unset, None, bool] = UNSET
    radiant_score: Union[Unset, int] = UNSET
    dire_score: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    start_time: Union[Unset, int] = UNSET
    leagueid: Union[Unset, int] = UNSET
    league_name: Union[Unset, str] = UNSET
    cluster: Union[Unset, int] = UNSET
    opposing_team_id: Union[Unset, int] = UNSET
    opposing_team_name: Union[Unset, None, str] = UNSET
    opposing_team_logo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        match_id = self.match_id
        radiant = self.radiant
        radiant_win = self.radiant_win
        radiant_score = self.radiant_score
        dire_score = self.dire_score
        duration = self.duration
        start_time = self.start_time
        leagueid = self.leagueid
        league_name = self.league_name
        cluster = self.cluster
        opposing_team_id = self.opposing_team_id
        opposing_team_name = self.opposing_team_name
        opposing_team_logo = self.opposing_team_logo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_id is not UNSET:
            field_dict["match_id"] = match_id
        if radiant is not UNSET:
            field_dict["radiant"] = radiant
        if radiant_win is not UNSET:
            field_dict["radiant_win"] = radiant_win
        if radiant_score is not UNSET:
            field_dict["radiant_score"] = radiant_score
        if dire_score is not UNSET:
            field_dict["dire_score"] = dire_score
        if duration is not UNSET:
            field_dict["duration"] = duration
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if leagueid is not UNSET:
            field_dict["leagueid"] = leagueid
        if league_name is not UNSET:
            field_dict["league_name"] = league_name
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if opposing_team_id is not UNSET:
            field_dict["opposing_team_id"] = opposing_team_id
        if opposing_team_name is not UNSET:
            field_dict["opposing_team_name"] = opposing_team_name
        if opposing_team_logo is not UNSET:
            field_dict["opposing_team_logo"] = opposing_team_logo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        match_id = d.pop("match_id", UNSET)

        radiant = d.pop("radiant", UNSET)

        radiant_win = d.pop("radiant_win", UNSET)

        radiant_score = d.pop("radiant_score", UNSET)

        dire_score = d.pop("dire_score", UNSET)

        duration = d.pop("duration", UNSET)

        start_time = d.pop("start_time", UNSET)

        leagueid = d.pop("leagueid", UNSET)

        league_name = d.pop("league_name", UNSET)

        cluster = d.pop("cluster", UNSET)

        opposing_team_id = d.pop("opposing_team_id", UNSET)

        opposing_team_name = d.pop("opposing_team_name", UNSET)

        opposing_team_logo = d.pop("opposing_team_logo", UNSET)

        team_match_object_response = cls(
            match_id=match_id,
            radiant=radiant,
            radiant_win=radiant_win,
            radiant_score=radiant_score,
            dire_score=dire_score,
            duration=duration,
            start_time=start_time,
            leagueid=leagueid,
            league_name=league_name,
            cluster=cluster,
            opposing_team_id=opposing_team_id,
            opposing_team_name=opposing_team_name,
            opposing_team_logo=opposing_team_logo,
        )

        team_match_object_response.additional_properties = d
        return team_match_object_response

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
