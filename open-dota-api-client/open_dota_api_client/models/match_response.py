from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_response_all_word_counts import MatchResponseAllWordCounts
    from ..models.match_response_chat_item import MatchResponseChatItem
    from ..models.match_response_cosmetics import MatchResponseCosmetics
    from ..models.match_response_dire_team import MatchResponseDireTeam
    from ..models.match_response_draft_timings_item import MatchResponseDraftTimingsItem
    from ..models.match_response_league import MatchResponseLeague
    from ..models.match_response_my_word_counts import MatchResponseMyWordCounts
    from ..models.match_response_objectives_item import MatchResponseObjectivesItem
    from ..models.match_response_picks_bans_item import MatchResponsePicksBansItem
    from ..models.match_response_players_item import MatchResponsePlayersItem
    from ..models.match_response_radiant_team import MatchResponseRadiantTeam
    from ..models.match_response_teamfights_item import MatchResponseTeamfightsItem


T = TypeVar("T", bound="MatchResponse")


@_attrs_define
class MatchResponse:
    """
    Attributes:
        match_id (Union[Unset, int]): The ID number of the match assigned by Valve Example: 3703866531.
        barracks_status_dire (Union[Unset, int]): Bitmask. An integer that represents a binary of which barracks are
            still standing. 63 would mean all barracks still stand at the end of the game.
        barracks_status_radiant (Union[Unset, int]): Bitmask. An integer that represents a binary of which barracks are
            still standing. 63 would mean all barracks still stand at the end of the game.
        chat (Union[Unset, List['MatchResponseChatItem']]): Array containing information on the chat of the game
        cluster (Union[Unset, int]): cluster
        cosmetics (Union[Unset, MatchResponseCosmetics]): cosmetics
        dire_score (Union[Unset, int]): Number of kills the Dire team had when the match ended
        draft_timings (Union[Unset, List['MatchResponseDraftTimingsItem']]): draft_timings
        duration (Union[Unset, int]): Duration of the game in seconds
        engine (Union[Unset, int]): engine
        first_blood_time (Union[Unset, int]): Time in seconds at which first blood occurred
        game_mode (Union[Unset, int]): Integer corresponding to game mode played. List of constants can be found here:
            https://github.com/odota/dotaconstants/blob/master/json/game_mode.json
        human_players (Union[Unset, int]): Number of human players in the game
        leagueid (Union[Unset, int]): leagueid
        lobby_type (Union[Unset, int]): Integer corresponding to lobby type of match. List of constants can be found
            here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json
        match_seq_num (Union[Unset, int]): match_seq_num
        negative_votes (Union[Unset, int]): Number of negative votes the replay received in the in-game client
        objectives (Union[Unset, List['MatchResponseObjectivesItem']]): objectives
        picks_bans (Union[Unset, List['MatchResponsePicksBansItem']]): Array containing information on the draft. Each
            item contains a boolean relating to whether the choice is a pick or a ban, the hero ID, the team the picked or
            banned it, and the order.
        positive_votes (Union[Unset, int]): Number of positive votes the replay received in the in-game client
        radiant_gold_adv (Union[Unset, List[float]]): Array of the Radiant gold advantage at each minute in the game. A
            negative number means that Radiant is behind, and thus it is their gold disadvantage.
        radiant_score (Union[Unset, int]): Number of kills the Radiant team had when the match ended
        radiant_win (Union[Unset, None, bool]): Boolean indicating whether Radiant won the match
        radiant_xp_adv (Union[Unset, List[float]]): Array of the Radiant experience advantage at each minute in the
            game. A negative number means that Radiant is behind, and thus it is their experience disadvantage.
        start_time (Union[Unset, int]): The Unix timestamp at which the game started
        teamfights (Union[Unset, None, List['MatchResponseTeamfightsItem']]): teamfights
        tower_status_dire (Union[Unset, int]): Bitmask. An integer that represents a binary of which Dire towers are
            still standing.
        tower_status_radiant (Union[Unset, int]): Bitmask. An integer that represents a binary of which Radiant towers
            are still standing.
        version (Union[Unset, int]): Parse version, used internally by OpenDota
        replay_salt (Union[Unset, int]): replay_salt
        series_id (Union[Unset, int]): series_id
        series_type (Union[Unset, int]): series_type
        radiant_team (Union[Unset, MatchResponseRadiantTeam]): radiant_team
        dire_team (Union[Unset, MatchResponseDireTeam]): dire_team
        league (Union[Unset, MatchResponseLeague]): league
        skill (Union[Unset, None, int]): Skill bracket assigned by Valve (Normal, High, Very High)
        players (Union[Unset, List['MatchResponsePlayersItem']]): Array of information on individual players
        patch (Union[Unset, int]): Information on the patch version the game is played on
        region (Union[Unset, int]): Integer corresponding to the region the game was played on
        all_word_counts (Union[Unset, MatchResponseAllWordCounts]): Word counts of the all chat messages in the player's
            games
        my_word_counts (Union[Unset, MatchResponseMyWordCounts]): Word counts of the player's all chat messages
        throw (Union[Unset, int]): Maximum gold advantage of the player's team if they lost the match
        comeback (Union[Unset, int]): Maximum gold disadvantage of the player's team if they won the match
        loss (Union[Unset, int]): Maximum gold disadvantage of the player's team if they lost the match
        win (Union[Unset, int]): Maximum gold advantage of the player's team if they won the match
        replay_url (Union[Unset, str]): replay_url
    """

    match_id: Union[Unset, int] = UNSET
    barracks_status_dire: Union[Unset, int] = UNSET
    barracks_status_radiant: Union[Unset, int] = UNSET
    chat: Union[Unset, List["MatchResponseChatItem"]] = UNSET
    cluster: Union[Unset, int] = UNSET
    cosmetics: Union[Unset, "MatchResponseCosmetics"] = UNSET
    dire_score: Union[Unset, int] = UNSET
    draft_timings: Union[Unset, List["MatchResponseDraftTimingsItem"]] = UNSET
    duration: Union[Unset, int] = UNSET
    engine: Union[Unset, int] = UNSET
    first_blood_time: Union[Unset, int] = UNSET
    game_mode: Union[Unset, int] = UNSET
    human_players: Union[Unset, int] = UNSET
    leagueid: Union[Unset, int] = UNSET
    lobby_type: Union[Unset, int] = UNSET
    match_seq_num: Union[Unset, int] = UNSET
    negative_votes: Union[Unset, int] = UNSET
    objectives: Union[Unset, List["MatchResponseObjectivesItem"]] = UNSET
    picks_bans: Union[Unset, List["MatchResponsePicksBansItem"]] = UNSET
    positive_votes: Union[Unset, int] = UNSET
    radiant_gold_adv: Union[Unset, List[float]] = UNSET
    radiant_score: Union[Unset, int] = UNSET
    radiant_win: Union[Unset, None, bool] = UNSET
    radiant_xp_adv: Union[Unset, List[float]] = UNSET
    start_time: Union[Unset, int] = UNSET
    teamfights: Union[Unset, None, List["MatchResponseTeamfightsItem"]] = UNSET
    tower_status_dire: Union[Unset, int] = UNSET
    tower_status_radiant: Union[Unset, int] = UNSET
    version: Union[Unset, int] = UNSET
    replay_salt: Union[Unset, int] = UNSET
    series_id: Union[Unset, int] = UNSET
    series_type: Union[Unset, int] = UNSET
    radiant_team: Union[Unset, "MatchResponseRadiantTeam"] = UNSET
    dire_team: Union[Unset, "MatchResponseDireTeam"] = UNSET
    league: Union[Unset, "MatchResponseLeague"] = UNSET
    skill: Union[Unset, None, int] = UNSET
    players: Union[Unset, List["MatchResponsePlayersItem"]] = UNSET
    patch: Union[Unset, int] = UNSET
    region: Union[Unset, int] = UNSET
    all_word_counts: Union[Unset, "MatchResponseAllWordCounts"] = UNSET
    my_word_counts: Union[Unset, "MatchResponseMyWordCounts"] = UNSET
    throw: Union[Unset, int] = UNSET
    comeback: Union[Unset, int] = UNSET
    loss: Union[Unset, int] = UNSET
    win: Union[Unset, int] = UNSET
    replay_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        match_id = self.match_id
        barracks_status_dire = self.barracks_status_dire
        barracks_status_radiant = self.barracks_status_radiant
        chat: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.chat, Unset):
            chat = []
            for chat_item_data in self.chat:
                chat_item = chat_item_data.to_dict()

                chat.append(chat_item)

        cluster = self.cluster
        cosmetics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cosmetics, Unset):
            cosmetics = self.cosmetics.to_dict()

        dire_score = self.dire_score
        draft_timings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.draft_timings, Unset):
            draft_timings = []
            for draft_timings_item_data in self.draft_timings:
                draft_timings_item = draft_timings_item_data.to_dict()

                draft_timings.append(draft_timings_item)

        duration = self.duration
        engine = self.engine
        first_blood_time = self.first_blood_time
        game_mode = self.game_mode
        human_players = self.human_players
        leagueid = self.leagueid
        lobby_type = self.lobby_type
        match_seq_num = self.match_seq_num
        negative_votes = self.negative_votes
        objectives: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.objectives, Unset):
            objectives = []
            for objectives_item_data in self.objectives:
                objectives_item = objectives_item_data.to_dict()

                objectives.append(objectives_item)

        picks_bans: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.picks_bans, Unset):
            picks_bans = []
            for picks_bans_item_data in self.picks_bans:
                picks_bans_item = picks_bans_item_data.to_dict()

                picks_bans.append(picks_bans_item)

        positive_votes = self.positive_votes
        radiant_gold_adv: Union[Unset, List[float]] = UNSET
        if not isinstance(self.radiant_gold_adv, Unset):
            radiant_gold_adv = self.radiant_gold_adv

        radiant_score = self.radiant_score
        radiant_win = self.radiant_win
        radiant_xp_adv: Union[Unset, List[float]] = UNSET
        if not isinstance(self.radiant_xp_adv, Unset):
            radiant_xp_adv = self.radiant_xp_adv

        start_time = self.start_time
        teamfights: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teamfights, Unset):
            if self.teamfights is None:
                teamfights = None
            else:
                teamfights = []
                for teamfights_item_data in self.teamfights:
                    teamfights_item = teamfights_item_data.to_dict()

                    teamfights.append(teamfights_item)

        tower_status_dire = self.tower_status_dire
        tower_status_radiant = self.tower_status_radiant
        version = self.version
        replay_salt = self.replay_salt
        series_id = self.series_id
        series_type = self.series_type
        radiant_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.radiant_team, Unset):
            radiant_team = self.radiant_team.to_dict()

        dire_team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dire_team, Unset):
            dire_team = self.dire_team.to_dict()

        league: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.league, Unset):
            league = self.league.to_dict()

        skill = self.skill
        players: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.players, Unset):
            players = []
            for players_item_data in self.players:
                players_item = players_item_data.to_dict()

                players.append(players_item)

        patch = self.patch
        region = self.region
        all_word_counts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.all_word_counts, Unset):
            all_word_counts = self.all_word_counts.to_dict()

        my_word_counts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.my_word_counts, Unset):
            my_word_counts = self.my_word_counts.to_dict()

        throw = self.throw
        comeback = self.comeback
        loss = self.loss
        win = self.win
        replay_url = self.replay_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_id is not UNSET:
            field_dict["match_id"] = match_id
        if barracks_status_dire is not UNSET:
            field_dict["barracks_status_dire"] = barracks_status_dire
        if barracks_status_radiant is not UNSET:
            field_dict["barracks_status_radiant"] = barracks_status_radiant
        if chat is not UNSET:
            field_dict["chat"] = chat
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if cosmetics is not UNSET:
            field_dict["cosmetics"] = cosmetics
        if dire_score is not UNSET:
            field_dict["dire_score"] = dire_score
        if draft_timings is not UNSET:
            field_dict["draft_timings"] = draft_timings
        if duration is not UNSET:
            field_dict["duration"] = duration
        if engine is not UNSET:
            field_dict["engine"] = engine
        if first_blood_time is not UNSET:
            field_dict["first_blood_time"] = first_blood_time
        if game_mode is not UNSET:
            field_dict["game_mode"] = game_mode
        if human_players is not UNSET:
            field_dict["human_players"] = human_players
        if leagueid is not UNSET:
            field_dict["leagueid"] = leagueid
        if lobby_type is not UNSET:
            field_dict["lobby_type"] = lobby_type
        if match_seq_num is not UNSET:
            field_dict["match_seq_num"] = match_seq_num
        if negative_votes is not UNSET:
            field_dict["negative_votes"] = negative_votes
        if objectives is not UNSET:
            field_dict["objectives"] = objectives
        if picks_bans is not UNSET:
            field_dict["picks_bans"] = picks_bans
        if positive_votes is not UNSET:
            field_dict["positive_votes"] = positive_votes
        if radiant_gold_adv is not UNSET:
            field_dict["radiant_gold_adv"] = radiant_gold_adv
        if radiant_score is not UNSET:
            field_dict["radiant_score"] = radiant_score
        if radiant_win is not UNSET:
            field_dict["radiant_win"] = radiant_win
        if radiant_xp_adv is not UNSET:
            field_dict["radiant_xp_adv"] = radiant_xp_adv
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if teamfights is not UNSET:
            field_dict["teamfights"] = teamfights
        if tower_status_dire is not UNSET:
            field_dict["tower_status_dire"] = tower_status_dire
        if tower_status_radiant is not UNSET:
            field_dict["tower_status_radiant"] = tower_status_radiant
        if version is not UNSET:
            field_dict["version"] = version
        if replay_salt is not UNSET:
            field_dict["replay_salt"] = replay_salt
        if series_id is not UNSET:
            field_dict["series_id"] = series_id
        if series_type is not UNSET:
            field_dict["series_type"] = series_type
        if radiant_team is not UNSET:
            field_dict["radiant_team"] = radiant_team
        if dire_team is not UNSET:
            field_dict["dire_team"] = dire_team
        if league is not UNSET:
            field_dict["league"] = league
        if skill is not UNSET:
            field_dict["skill"] = skill
        if players is not UNSET:
            field_dict["players"] = players
        if patch is not UNSET:
            field_dict["patch"] = patch
        if region is not UNSET:
            field_dict["region"] = region
        if all_word_counts is not UNSET:
            field_dict["all_word_counts"] = all_word_counts
        if my_word_counts is not UNSET:
            field_dict["my_word_counts"] = my_word_counts
        if throw is not UNSET:
            field_dict["throw"] = throw
        if comeback is not UNSET:
            field_dict["comeback"] = comeback
        if loss is not UNSET:
            field_dict["loss"] = loss
        if win is not UNSET:
            field_dict["win"] = win
        if replay_url is not UNSET:
            field_dict["replay_url"] = replay_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.match_response_all_word_counts import MatchResponseAllWordCounts
        from ..models.match_response_chat_item import MatchResponseChatItem
        from ..models.match_response_cosmetics import MatchResponseCosmetics
        from ..models.match_response_dire_team import MatchResponseDireTeam
        from ..models.match_response_draft_timings_item import MatchResponseDraftTimingsItem
        from ..models.match_response_league import MatchResponseLeague
        from ..models.match_response_my_word_counts import MatchResponseMyWordCounts
        from ..models.match_response_objectives_item import MatchResponseObjectivesItem
        from ..models.match_response_picks_bans_item import MatchResponsePicksBansItem
        from ..models.match_response_players_item import MatchResponsePlayersItem
        from ..models.match_response_radiant_team import MatchResponseRadiantTeam
        from ..models.match_response_teamfights_item import MatchResponseTeamfightsItem

        d = src_dict.copy()
        match_id = d.pop("match_id", UNSET)

        barracks_status_dire = d.pop("barracks_status_dire", UNSET)

        barracks_status_radiant = d.pop("barracks_status_radiant", UNSET)

        chat = []
        _chat = d.pop("chat", UNSET)
        for chat_item_data in _chat or []:
            chat_item = MatchResponseChatItem.from_dict(chat_item_data)

            chat.append(chat_item)

        cluster = d.pop("cluster", UNSET)

        _cosmetics = d.pop("cosmetics", UNSET)
        cosmetics: Union[Unset, MatchResponseCosmetics]
        if isinstance(_cosmetics, Unset):
            cosmetics = UNSET
        else:
            cosmetics = MatchResponseCosmetics.from_dict(_cosmetics)

        dire_score = d.pop("dire_score", UNSET)

        draft_timings = []
        _draft_timings = d.pop("draft_timings", UNSET)
        for draft_timings_item_data in _draft_timings or []:
            draft_timings_item = MatchResponseDraftTimingsItem.from_dict(draft_timings_item_data)

            draft_timings.append(draft_timings_item)

        duration = d.pop("duration", UNSET)

        engine = d.pop("engine", UNSET)

        first_blood_time = d.pop("first_blood_time", UNSET)

        game_mode = d.pop("game_mode", UNSET)

        human_players = d.pop("human_players", UNSET)

        leagueid = d.pop("leagueid", UNSET)

        lobby_type = d.pop("lobby_type", UNSET)

        match_seq_num = d.pop("match_seq_num", UNSET)

        negative_votes = d.pop("negative_votes", UNSET)

        objectives = []
        _objectives = d.pop("objectives", UNSET)
        for objectives_item_data in _objectives or []:
            objectives_item = MatchResponseObjectivesItem.from_dict(objectives_item_data)

            objectives.append(objectives_item)

        picks_bans = []
        _picks_bans = d.pop("picks_bans", UNSET)
        for picks_bans_item_data in _picks_bans or []:
            picks_bans_item = MatchResponsePicksBansItem.from_dict(picks_bans_item_data)

            picks_bans.append(picks_bans_item)

        positive_votes = d.pop("positive_votes", UNSET)

        radiant_gold_adv = cast(List[float], d.pop("radiant_gold_adv", UNSET))

        radiant_score = d.pop("radiant_score", UNSET)

        radiant_win = d.pop("radiant_win", UNSET)

        radiant_xp_adv = cast(List[float], d.pop("radiant_xp_adv", UNSET))

        start_time = d.pop("start_time", UNSET)

        teamfights = []
        _teamfights = d.pop("teamfights", UNSET)
        for teamfights_item_data in _teamfights or []:
            teamfights_item = MatchResponseTeamfightsItem.from_dict(teamfights_item_data)

            teamfights.append(teamfights_item)

        tower_status_dire = d.pop("tower_status_dire", UNSET)

        tower_status_radiant = d.pop("tower_status_radiant", UNSET)

        version = d.pop("version", UNSET)

        replay_salt = d.pop("replay_salt", UNSET)

        series_id = d.pop("series_id", UNSET)

        series_type = d.pop("series_type", UNSET)

        _radiant_team = d.pop("radiant_team", UNSET)
        radiant_team: Union[Unset, MatchResponseRadiantTeam]
        if isinstance(_radiant_team, Unset):
            radiant_team = UNSET
        else:
            radiant_team = MatchResponseRadiantTeam.from_dict(_radiant_team)

        _dire_team = d.pop("dire_team", UNSET)
        dire_team: Union[Unset, MatchResponseDireTeam]
        if isinstance(_dire_team, Unset):
            dire_team = UNSET
        else:
            dire_team = MatchResponseDireTeam.from_dict(_dire_team)

        _league = d.pop("league", UNSET)
        league: Union[Unset, MatchResponseLeague]
        if isinstance(_league, Unset):
            league = UNSET
        else:
            league = MatchResponseLeague.from_dict(_league)

        skill = d.pop("skill", UNSET)

        players = []
        _players = d.pop("players", UNSET)
        for players_item_data in _players or []:
            players_item = MatchResponsePlayersItem.from_dict(players_item_data)

            players.append(players_item)

        patch = d.pop("patch", UNSET)

        region = d.pop("region", UNSET)

        _all_word_counts = d.pop("all_word_counts", UNSET)
        all_word_counts: Union[Unset, MatchResponseAllWordCounts]
        if isinstance(_all_word_counts, Unset):
            all_word_counts = UNSET
        else:
            all_word_counts = MatchResponseAllWordCounts.from_dict(_all_word_counts)

        _my_word_counts = d.pop("my_word_counts", UNSET)
        my_word_counts: Union[Unset, MatchResponseMyWordCounts]
        if isinstance(_my_word_counts, Unset):
            my_word_counts = UNSET
        else:
            my_word_counts = MatchResponseMyWordCounts.from_dict(_my_word_counts)

        throw = d.pop("throw", UNSET)

        comeback = d.pop("comeback", UNSET)

        loss = d.pop("loss", UNSET)

        win = d.pop("win", UNSET)

        replay_url = d.pop("replay_url", UNSET)

        match_response = cls(
            match_id=match_id,
            barracks_status_dire=barracks_status_dire,
            barracks_status_radiant=barracks_status_radiant,
            chat=chat,
            cluster=cluster,
            cosmetics=cosmetics,
            dire_score=dire_score,
            draft_timings=draft_timings,
            duration=duration,
            engine=engine,
            first_blood_time=first_blood_time,
            game_mode=game_mode,
            human_players=human_players,
            leagueid=leagueid,
            lobby_type=lobby_type,
            match_seq_num=match_seq_num,
            negative_votes=negative_votes,
            objectives=objectives,
            picks_bans=picks_bans,
            positive_votes=positive_votes,
            radiant_gold_adv=radiant_gold_adv,
            radiant_score=radiant_score,
            radiant_win=radiant_win,
            radiant_xp_adv=radiant_xp_adv,
            start_time=start_time,
            teamfights=teamfights,
            tower_status_dire=tower_status_dire,
            tower_status_radiant=tower_status_radiant,
            version=version,
            replay_salt=replay_salt,
            series_id=series_id,
            series_type=series_type,
            radiant_team=radiant_team,
            dire_team=dire_team,
            league=league,
            skill=skill,
            players=players,
            patch=patch,
            region=region,
            all_word_counts=all_word_counts,
            my_word_counts=my_word_counts,
            throw=throw,
            comeback=comeback,
            loss=loss,
            win=win,
            replay_url=replay_url,
        )

        match_response.additional_properties = d
        return match_response

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
