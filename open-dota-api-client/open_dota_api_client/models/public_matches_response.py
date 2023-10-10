from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicMatchesResponse")


@_attrs_define
class PublicMatchesResponse:
    """
    Attributes:
        match_id (Union[Unset, int]): The ID number of the match assigned by Valve Example: 3703866531.
        match_seq_num (Union[Unset, int]): match_seq_num
        radiant_win (Union[Unset, None, bool]): Boolean indicating whether Radiant won the match
        start_time (Union[Unset, int]): The Unix timestamp at which the game started
        duration (Union[Unset, int]): Duration of the game in seconds
        avg_mmr (Union[Unset, int]):
        num_mmr (Union[Unset, int]):
        lobby_type (Union[Unset, int]):
        game_mode (Union[Unset, int]):
        avg_rank_tier (Union[Unset, int]):
        num_rank_tier (Union[Unset, int]):
        cluster (Union[Unset, int]):
        radiant_team (Union[Unset, str]): radiant_team
        dire_team (Union[Unset, str]): dire_team
    """

    match_id: Union[Unset, int] = UNSET
    match_seq_num: Union[Unset, int] = UNSET
    radiant_win: Union[Unset, None, bool] = UNSET
    start_time: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    avg_mmr: Union[Unset, int] = UNSET
    num_mmr: Union[Unset, int] = UNSET
    lobby_type: Union[Unset, int] = UNSET
    game_mode: Union[Unset, int] = UNSET
    avg_rank_tier: Union[Unset, int] = UNSET
    num_rank_tier: Union[Unset, int] = UNSET
    cluster: Union[Unset, int] = UNSET
    radiant_team: Union[Unset, str] = UNSET
    dire_team: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        match_id = self.match_id
        match_seq_num = self.match_seq_num
        radiant_win = self.radiant_win
        start_time = self.start_time
        duration = self.duration
        avg_mmr = self.avg_mmr
        num_mmr = self.num_mmr
        lobby_type = self.lobby_type
        game_mode = self.game_mode
        avg_rank_tier = self.avg_rank_tier
        num_rank_tier = self.num_rank_tier
        cluster = self.cluster
        radiant_team = self.radiant_team
        dire_team = self.dire_team

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_id is not UNSET:
            field_dict["match_id"] = match_id
        if match_seq_num is not UNSET:
            field_dict["match_seq_num"] = match_seq_num
        if radiant_win is not UNSET:
            field_dict["radiant_win"] = radiant_win
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if avg_mmr is not UNSET:
            field_dict["avg_mmr"] = avg_mmr
        if num_mmr is not UNSET:
            field_dict["num_mmr"] = num_mmr
        if lobby_type is not UNSET:
            field_dict["lobby_type"] = lobby_type
        if game_mode is not UNSET:
            field_dict["game_mode"] = game_mode
        if avg_rank_tier is not UNSET:
            field_dict["avg_rank_tier"] = avg_rank_tier
        if num_rank_tier is not UNSET:
            field_dict["num_rank_tier"] = num_rank_tier
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if radiant_team is not UNSET:
            field_dict["radiant_team"] = radiant_team
        if dire_team is not UNSET:
            field_dict["dire_team"] = dire_team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        match_id = d.pop("match_id", UNSET)

        match_seq_num = d.pop("match_seq_num", UNSET)

        radiant_win = d.pop("radiant_win", UNSET)

        start_time = d.pop("start_time", UNSET)

        duration = d.pop("duration", UNSET)

        avg_mmr = d.pop("avg_mmr", UNSET)

        num_mmr = d.pop("num_mmr", UNSET)

        lobby_type = d.pop("lobby_type", UNSET)

        game_mode = d.pop("game_mode", UNSET)

        avg_rank_tier = d.pop("avg_rank_tier", UNSET)

        num_rank_tier = d.pop("num_rank_tier", UNSET)

        cluster = d.pop("cluster", UNSET)

        radiant_team = d.pop("radiant_team", UNSET)

        dire_team = d.pop("dire_team", UNSET)

        public_matches_response = cls(
            match_id=match_id,
            match_seq_num=match_seq_num,
            radiant_win=radiant_win,
            start_time=start_time,
            duration=duration,
            avg_mmr=avg_mmr,
            num_mmr=num_mmr,
            lobby_type=lobby_type,
            game_mode=game_mode,
            avg_rank_tier=avg_rank_tier,
            num_rank_tier=num_rank_tier,
            cluster=cluster,
            radiant_team=radiant_team,
            dire_team=dire_team,
        )

        public_matches_response.additional_properties = d
        return public_matches_response

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
