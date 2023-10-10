from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerMatchesResponse")


@_attrs_define
class PlayerMatchesResponse:
    """Object containing information on the match

    Attributes:
        match_id (Union[Unset, int]): The ID number of the match assigned by Valve Example: 3703866531.
        player_slot (Union[Unset, None, int]): Which slot the player is in. 0-127 are Radiant, 128-255 are Dire
        radiant_win (Union[Unset, None, bool]): Boolean indicating whether Radiant won the match
        duration (Union[Unset, int]): Duration of the game in seconds
        game_mode (Union[Unset, int]): Integer corresponding to game mode played. List of constants can be found here:
            https://github.com/odota/dotaconstants/blob/master/json/game_mode.json
        lobby_type (Union[Unset, int]): Integer corresponding to lobby type of match. List of constants can be found
            here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json
        hero_id (Union[Unset, int]): The ID value of the hero played
        start_time (Union[Unset, int]): The Unix timestamp at which the game started
        version (Union[Unset, None, int]): version
        kills (Union[Unset, int]): Total kills the player had at the end of the game
        deaths (Union[Unset, int]): Total deaths the player had at the end of the game
        assists (Union[Unset, int]): Total assists the player had at the end of the game
        skill (Union[Unset, None, int]): Skill bracket assigned by Valve (Normal, High, Very High)
        average_rank (Union[Unset, None, int]): Average rank of players with public match data
        leaver_status (Union[Unset, int]): Integer describing whether or not the player left the game. 0: didn't leave.
            1: left safely. 2+: Abandoned
        party_size (Union[Unset, None, int]): Size of the player's party
    """

    match_id: Union[Unset, int] = UNSET
    player_slot: Union[Unset, None, int] = UNSET
    radiant_win: Union[Unset, None, bool] = UNSET
    duration: Union[Unset, int] = UNSET
    game_mode: Union[Unset, int] = UNSET
    lobby_type: Union[Unset, int] = UNSET
    hero_id: Union[Unset, int] = UNSET
    start_time: Union[Unset, int] = UNSET
    version: Union[Unset, None, int] = UNSET
    kills: Union[Unset, int] = UNSET
    deaths: Union[Unset, int] = UNSET
    assists: Union[Unset, int] = UNSET
    skill: Union[Unset, None, int] = UNSET
    average_rank: Union[Unset, None, int] = UNSET
    leaver_status: Union[Unset, int] = UNSET
    party_size: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        match_id = self.match_id
        player_slot = self.player_slot
        radiant_win = self.radiant_win
        duration = self.duration
        game_mode = self.game_mode
        lobby_type = self.lobby_type
        hero_id = self.hero_id
        start_time = self.start_time
        version = self.version
        kills = self.kills
        deaths = self.deaths
        assists = self.assists
        skill = self.skill
        average_rank = self.average_rank
        leaver_status = self.leaver_status
        party_size = self.party_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_id is not UNSET:
            field_dict["match_id"] = match_id
        if player_slot is not UNSET:
            field_dict["player_slot"] = player_slot
        if radiant_win is not UNSET:
            field_dict["radiant_win"] = radiant_win
        if duration is not UNSET:
            field_dict["duration"] = duration
        if game_mode is not UNSET:
            field_dict["game_mode"] = game_mode
        if lobby_type is not UNSET:
            field_dict["lobby_type"] = lobby_type
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if version is not UNSET:
            field_dict["version"] = version
        if kills is not UNSET:
            field_dict["kills"] = kills
        if deaths is not UNSET:
            field_dict["deaths"] = deaths
        if assists is not UNSET:
            field_dict["assists"] = assists
        if skill is not UNSET:
            field_dict["skill"] = skill
        if average_rank is not UNSET:
            field_dict["average_rank"] = average_rank
        if leaver_status is not UNSET:
            field_dict["leaver_status"] = leaver_status
        if party_size is not UNSET:
            field_dict["party_size"] = party_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        match_id = d.pop("match_id", UNSET)

        player_slot = d.pop("player_slot", UNSET)

        radiant_win = d.pop("radiant_win", UNSET)

        duration = d.pop("duration", UNSET)

        game_mode = d.pop("game_mode", UNSET)

        lobby_type = d.pop("lobby_type", UNSET)

        hero_id = d.pop("hero_id", UNSET)

        start_time = d.pop("start_time", UNSET)

        version = d.pop("version", UNSET)

        kills = d.pop("kills", UNSET)

        deaths = d.pop("deaths", UNSET)

        assists = d.pop("assists", UNSET)

        skill = d.pop("skill", UNSET)

        average_rank = d.pop("average_rank", UNSET)

        leaver_status = d.pop("leaver_status", UNSET)

        party_size = d.pop("party_size", UNSET)

        player_matches_response = cls(
            match_id=match_id,
            player_slot=player_slot,
            radiant_win=radiant_win,
            duration=duration,
            game_mode=game_mode,
            lobby_type=lobby_type,
            hero_id=hero_id,
            start_time=start_time,
            version=version,
            kills=kills,
            deaths=deaths,
            assists=assists,
            skill=skill,
            average_rank=average_rank,
            leaver_status=leaver_status,
            party_size=party_size,
        )

        player_matches_response.additional_properties = d
        return player_matches_response

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
