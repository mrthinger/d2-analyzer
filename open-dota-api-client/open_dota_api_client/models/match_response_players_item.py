import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_response_players_item_ability_targets import MatchResponsePlayersItemAbilityTargets
    from ..models.match_response_players_item_ability_uses import MatchResponsePlayersItemAbilityUses
    from ..models.match_response_players_item_actions import MatchResponsePlayersItemActions
    from ..models.match_response_players_item_additional_units_item import MatchResponsePlayersItemAdditionalUnitsItem
    from ..models.match_response_players_item_benchmarks import MatchResponsePlayersItemBenchmarks
    from ..models.match_response_players_item_buyback_log_item import MatchResponsePlayersItemBuybackLogItem
    from ..models.match_response_players_item_connection_log_item import MatchResponsePlayersItemConnectionLogItem
    from ..models.match_response_players_item_cosmetics_item import MatchResponsePlayersItemCosmeticsItem
    from ..models.match_response_players_item_damage import MatchResponsePlayersItemDamage
    from ..models.match_response_players_item_damage_inflictor import MatchResponsePlayersItemDamageInflictor
    from ..models.match_response_players_item_damage_inflictor_received import (
        MatchResponsePlayersItemDamageInflictorReceived,
    )
    from ..models.match_response_players_item_damage_taken import MatchResponsePlayersItemDamageTaken
    from ..models.match_response_players_item_damage_targets import MatchResponsePlayersItemDamageTargets
    from ..models.match_response_players_item_first_purchase_time import MatchResponsePlayersItemFirstPurchaseTime
    from ..models.match_response_players_item_gold_reasons import MatchResponsePlayersItemGoldReasons
    from ..models.match_response_players_item_hero_hits import MatchResponsePlayersItemHeroHits
    from ..models.match_response_players_item_item_usage import MatchResponsePlayersItemItemUsage
    from ..models.match_response_players_item_item_uses import MatchResponsePlayersItemItemUses
    from ..models.match_response_players_item_item_win import MatchResponsePlayersItemItemWin
    from ..models.match_response_players_item_kill_streaks import MatchResponsePlayersItemKillStreaks
    from ..models.match_response_players_item_killed import MatchResponsePlayersItemKilled
    from ..models.match_response_players_item_killed_by import MatchResponsePlayersItemKilledBy
    from ..models.match_response_players_item_kills_log_item import MatchResponsePlayersItemKillsLogItem
    from ..models.match_response_players_item_lane_pos import MatchResponsePlayersItemLanePos
    from ..models.match_response_players_item_life_state import MatchResponsePlayersItemLifeState
    from ..models.match_response_players_item_max_hero_hit import MatchResponsePlayersItemMaxHeroHit
    from ..models.match_response_players_item_multi_kills import MatchResponsePlayersItemMultiKills
    from ..models.match_response_players_item_obs import MatchResponsePlayersItemObs
    from ..models.match_response_players_item_obs_left_log_item import MatchResponsePlayersItemObsLeftLogItem
    from ..models.match_response_players_item_obs_log_item import MatchResponsePlayersItemObsLogItem
    from ..models.match_response_players_item_permanent_buffs_item import MatchResponsePlayersItemPermanentBuffsItem
    from ..models.match_response_players_item_purchase import MatchResponsePlayersItemPurchase
    from ..models.match_response_players_item_purchase_log_item import MatchResponsePlayersItemPurchaseLogItem
    from ..models.match_response_players_item_purchase_time import MatchResponsePlayersItemPurchaseTime
    from ..models.match_response_players_item_runes import MatchResponsePlayersItemRunes
    from ..models.match_response_players_item_runes_log_item import MatchResponsePlayersItemRunesLogItem
    from ..models.match_response_players_item_sen import MatchResponsePlayersItemSen
    from ..models.match_response_players_item_sen_left_log_item import MatchResponsePlayersItemSenLeftLogItem
    from ..models.match_response_players_item_sen_log_item import MatchResponsePlayersItemSenLogItem
    from ..models.match_response_players_item_xp_reasons import MatchResponsePlayersItemXpReasons


T = TypeVar("T", bound="MatchResponsePlayersItem")


@_attrs_define
class MatchResponsePlayersItem:
    """player

    Attributes:
        match_id (Union[Unset, int]): The ID number of the match assigned by Valve Example: 3703866531.
        player_slot (Union[Unset, None, int]): Which slot the player is in. 0-127 are Radiant, 128-255 are Dire
        ability_upgrades_arr (Union[Unset, List[int]]): An array describing how abilities were upgraded
        ability_uses (Union[Unset, MatchResponsePlayersItemAbilityUses]): Object containing information on how many
            times the played used their abilities
        ability_targets (Union[Unset, MatchResponsePlayersItemAbilityTargets]): Object containing information on who the
            player used their abilities on
        damage_targets (Union[Unset, MatchResponsePlayersItemDamageTargets]): Object containing information on how and
            how much damage the player dealt to other heroes
        account_id (Union[Unset, int]): The player account ID
        actions (Union[Unset, MatchResponsePlayersItemActions]): Object containing information on how many and what type
            of actions the player issued to their hero
        additional_units (Union[Unset, None, List['MatchResponsePlayersItemAdditionalUnitsItem']]): Object containing
            information on additional units the player had under their control
        assists (Union[Unset, int]): Number of assists the player had
        backpack_0 (Union[Unset, int]): Item in backpack slot 0
        backpack_1 (Union[Unset, int]): Item in backpack slot 1
        backpack_2 (Union[Unset, int]): Item in backpack slot 2
        buyback_log (Union[Unset, List['MatchResponsePlayersItemBuybackLogItem']]): Array containing information about
            buybacks
        camps_stacked (Union[Unset, int]): Number of camps stacked
        connection_log (Union[Unset, List['MatchResponsePlayersItemConnectionLogItem']]): Array containing information
            about the player's disconnections and reconnections
        creeps_stacked (Union[Unset, int]): Number of creeps stacked
        damage (Union[Unset, MatchResponsePlayersItemDamage]): Object containing information about damage dealt by the
            player to different units
        damage_inflictor (Union[Unset, MatchResponsePlayersItemDamageInflictor]): Object containing information about
            about the sources of this player's damage to heroes
        damage_inflictor_received (Union[Unset, MatchResponsePlayersItemDamageInflictorReceived]): Object containing
            information about the sources of damage received by this player from heroes
        damage_taken (Union[Unset, MatchResponsePlayersItemDamageTaken]): Object containing information about from whom
            the player took damage
        deaths (Union[Unset, int]): Number of deaths
        denies (Union[Unset, int]): Number of denies
        dn_t (Union[Unset, List[int]]): Array containing number of denies at different times of the match
        gold (Union[Unset, int]): Gold at the end of the game
        gold_per_min (Union[Unset, int]): Gold Per Minute obtained by this player
        gold_reasons (Union[Unset, MatchResponsePlayersItemGoldReasons]): Object containing information on how the
            player gainined gold over the course of the match
        gold_spent (Union[Unset, int]): How much gold the player spent
        gold_t (Union[Unset, List[int]]): Array containing total gold at different times of the match
        hero_damage (Union[Unset, int]): Hero Damage Dealt
        hero_healing (Union[Unset, int]): Hero Healing Done
        hero_hits (Union[Unset, MatchResponsePlayersItemHeroHits]): Object containing information on how many ticks of
            damages the hero inflicted with different spells and damage inflictors
        hero_id (Union[Unset, int]): The ID value of the hero played
        item_0 (Union[Unset, int]): Item in the player's first slot
        item_1 (Union[Unset, int]): Item in the player's second slot
        item_2 (Union[Unset, int]): Item in the player's third slot
        item_3 (Union[Unset, int]): Item in the player's fourth slot
        item_4 (Union[Unset, int]): Item in the player's fifth slot
        item_5 (Union[Unset, int]): Item in the player's sixth slot
        item_uses (Union[Unset, MatchResponsePlayersItemItemUses]): Object containing information about how many times a
            player used items
        kill_streaks (Union[Unset, MatchResponsePlayersItemKillStreaks]): Object containing information about the
            player's killstreaks
        killed (Union[Unset, MatchResponsePlayersItemKilled]): Object containing information about what units the player
            killed
        killed_by (Union[Unset, MatchResponsePlayersItemKilledBy]): Object containing information about who killed the
            player
        kills (Union[Unset, int]): Number of kills
        kills_log (Union[Unset, List['MatchResponsePlayersItemKillsLogItem']]): Array containing information on which
            hero the player killed at what time
        lane_pos (Union[Unset, MatchResponsePlayersItemLanePos]): Object containing information on lane position
        last_hits (Union[Unset, int]): Number of last hits
        leaver_status (Union[Unset, int]): Integer describing whether or not the player left the game. 0: didn't leave.
            1: left safely. 2+: Abandoned
        level (Union[Unset, int]): Level at the end of the game
        lh_t (Union[Unset, List[int]]): Array describing last hits at each minute in the game
        life_state (Union[Unset, MatchResponsePlayersItemLifeState]): life_state
        max_hero_hit (Union[Unset, MatchResponsePlayersItemMaxHeroHit]): Object with information on the highest damage
            instance the player inflicted
        multi_kills (Union[Unset, MatchResponsePlayersItemMultiKills]): Object with information on the number of the
            number of multikills the player had
        obs (Union[Unset, MatchResponsePlayersItemObs]): Object with information on where the player placed observer
            wards. The location takes the form (outer number, inner number) and are from ~64-192.
        obs_left_log (Union[Unset, List['MatchResponsePlayersItemObsLeftLogItem']]): obs_left_log
        obs_log (Union[Unset, List['MatchResponsePlayersItemObsLogItem']]): Object containing information on when and
            where the player placed observer wards
        obs_placed (Union[Unset, int]): Total number of observer wards placed
        party_id (Union[Unset, int]): party_id
        permanent_buffs (Union[Unset, List['MatchResponsePlayersItemPermanentBuffsItem']]): Array describing permanent
            buffs the player had at the end of the game. List of constants can be found here:
            https://github.com/odota/dotaconstants/blob/master/json/permanent_buffs.json
        pings (Union[Unset, int]): Total number of pings
        purchase (Union[Unset, MatchResponsePlayersItemPurchase]): Object containing information on the items the player
            purchased
        purchase_log (Union[Unset, List['MatchResponsePlayersItemPurchaseLogItem']]): Object containing information on
            when items were purchased
        rune_pickups (Union[Unset, int]): Number of runes picked up
        runes (Union[Unset, MatchResponsePlayersItemRunes]): Object with information about which runes the player picked
            up
        runes_log (Union[Unset, List['MatchResponsePlayersItemRunesLogItem']]): Array with information on when runes
            were picked up
        sen (Union[Unset, MatchResponsePlayersItemSen]): Object with information on where sentries were placed. The
            location takes the form (outer number, inner number) and are from ~64-192.
        sen_left_log (Union[Unset, List['MatchResponsePlayersItemSenLeftLogItem']]): Array containing information on
            when and where the player placed sentries
        sen_log (Union[Unset, List['MatchResponsePlayersItemSenLogItem']]): Array with information on when and where
            sentries were placed by the player
        sen_placed (Union[Unset, int]): How many sentries were placed by the player
        stuns (Union[Unset, float]): Total stun duration of all stuns by the player
        times (Union[Unset, List[int]]): Time in seconds corresponding to the time of entries of other arrays in the
            match.
        tower_damage (Union[Unset, int]): Total tower damage done by the player
        xp_per_min (Union[Unset, int]): Experience Per Minute obtained by the player
        xp_reasons (Union[Unset, MatchResponsePlayersItemXpReasons]): Object containing information on the sources of
            this player's experience
        xp_t (Union[Unset, List[int]]): Experience at each minute of the game
        personaname (Union[Unset, None, str]): Player's Steam name Example: 420 booty wizard.
        name (Union[Unset, None, str]): name
        last_login (Union[Unset, None, datetime.datetime]): Time of player's last login
        radiant_win (Union[Unset, None, bool]): Boolean indicating whether Radiant won the match
        start_time (Union[Unset, int]): The Unix timestamp at which the game started
        duration (Union[Unset, int]): Duration of the game in seconds
        cluster (Union[Unset, int]): cluster
        lobby_type (Union[Unset, int]): Integer corresponding to lobby type of match. List of constants can be found
            here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json
        game_mode (Union[Unset, int]): Integer corresponding to game mode played. List of constants can be found here:
            https://github.com/odota/dotaconstants/blob/master/json/game_mode.json
        patch (Union[Unset, int]): Integer representing the patch the game was played on
        region (Union[Unset, int]): Integer corresponding to the region the game was played on
        is_radiant (Union[Unset, bool]): Boolean for whether or not the player is on Radiant
        win (Union[Unset, int]): Binary integer representing whether or not the player won
        lose (Union[Unset, int]): Binary integer representing whether or not the player lost
        total_gold (Union[Unset, int]): Total gold at the end of the game
        total_xp (Union[Unset, int]): Total experience at the end of the game
        kills_per_min (Union[Unset, float]): Number of kills per minute
        kda (Union[Unset, float]): kda
        abandons (Union[Unset, int]): abandons
        neutral_kills (Union[Unset, int]): Total number of neutral creeps killed
        tower_kills (Union[Unset, int]): Total number of tower kills the player had
        courier_kills (Union[Unset, int]): Total number of courier kills the player had
        lane_kills (Union[Unset, int]): Total number of lane creeps killed by the player
        hero_kills (Union[Unset, int]): Total number of heroes killed by the player
        observer_kills (Union[Unset, int]): Total number of observer wards killed by the player
        sentry_kills (Union[Unset, int]): Total number of sentry wards killed by the player
        roshan_kills (Union[Unset, int]): Total number of roshan kills (last hit on roshan) the player had
        necronomicon_kills (Union[Unset, int]): Total number of Necronomicon creeps killed by the player
        ancient_kills (Union[Unset, int]): Total number of Ancient creeps killed by the player
        buyback_count (Union[Unset, int]): Total number of buyback the player used
        observer_uses (Union[Unset, int]): Number of observer wards used
        sentry_uses (Union[Unset, int]): Number of sentry wards used
        lane_efficiency (Union[Unset, float]): lane_efficiency
        lane_efficiency_pct (Union[Unset, float]): lane_efficiency_pct
        lane (Union[Unset, None, int]): Integer referring to which lane the hero laned in
        lane_role (Union[Unset, None, int]): lane_role
        is_roaming (Union[Unset, None, bool]): Boolean referring to whether or not the player roamed
        purchase_time (Union[Unset, MatchResponsePlayersItemPurchaseTime]): Object with information on when the player
            last purchased an item
        first_purchase_time (Union[Unset, MatchResponsePlayersItemFirstPurchaseTime]): Object with information on when
            the player first puchased an item
        item_win (Union[Unset, MatchResponsePlayersItemItemWin]): Object with information on whether or not the item won
        item_usage (Union[Unset, MatchResponsePlayersItemItemUsage]): Object containing binary integers the tell whether
            the item was purchased by the player (note: this is always 1)
        purchase_tpscroll (Union[Unset, int]): Total number of TP scrolls purchased by the player
        actions_per_min (Union[Unset, int]): Actions per minute
        life_state_dead (Union[Unset, int]): life_state_dead
        rank_tier (Union[Unset, int]): The rank tier of the player. Tens place indicates rank, ones place indicates
            stars.
        cosmetics (Union[Unset, List['MatchResponsePlayersItemCosmeticsItem']]): cosmetics
        benchmarks (Union[Unset, MatchResponsePlayersItemBenchmarks]): Object containing information on certain
            benchmarks like GPM, XPM, KDA, tower damage, etc
    """

    match_id: Union[Unset, int] = UNSET
    player_slot: Union[Unset, None, int] = UNSET
    ability_upgrades_arr: Union[Unset, List[int]] = UNSET
    ability_uses: Union[Unset, "MatchResponsePlayersItemAbilityUses"] = UNSET
    ability_targets: Union[Unset, "MatchResponsePlayersItemAbilityTargets"] = UNSET
    damage_targets: Union[Unset, "MatchResponsePlayersItemDamageTargets"] = UNSET
    account_id: Union[Unset, int] = UNSET
    actions: Union[Unset, "MatchResponsePlayersItemActions"] = UNSET
    additional_units: Union[Unset, None, List["MatchResponsePlayersItemAdditionalUnitsItem"]] = UNSET
    assists: Union[Unset, int] = UNSET
    backpack_0: Union[Unset, int] = UNSET
    backpack_1: Union[Unset, int] = UNSET
    backpack_2: Union[Unset, int] = UNSET
    buyback_log: Union[Unset, List["MatchResponsePlayersItemBuybackLogItem"]] = UNSET
    camps_stacked: Union[Unset, int] = UNSET
    connection_log: Union[Unset, List["MatchResponsePlayersItemConnectionLogItem"]] = UNSET
    creeps_stacked: Union[Unset, int] = UNSET
    damage: Union[Unset, "MatchResponsePlayersItemDamage"] = UNSET
    damage_inflictor: Union[Unset, "MatchResponsePlayersItemDamageInflictor"] = UNSET
    damage_inflictor_received: Union[Unset, "MatchResponsePlayersItemDamageInflictorReceived"] = UNSET
    damage_taken: Union[Unset, "MatchResponsePlayersItemDamageTaken"] = UNSET
    deaths: Union[Unset, int] = UNSET
    denies: Union[Unset, int] = UNSET
    dn_t: Union[Unset, List[int]] = UNSET
    gold: Union[Unset, int] = UNSET
    gold_per_min: Union[Unset, int] = UNSET
    gold_reasons: Union[Unset, "MatchResponsePlayersItemGoldReasons"] = UNSET
    gold_spent: Union[Unset, int] = UNSET
    gold_t: Union[Unset, List[int]] = UNSET
    hero_damage: Union[Unset, int] = UNSET
    hero_healing: Union[Unset, int] = UNSET
    hero_hits: Union[Unset, "MatchResponsePlayersItemHeroHits"] = UNSET
    hero_id: Union[Unset, int] = UNSET
    item_0: Union[Unset, int] = UNSET
    item_1: Union[Unset, int] = UNSET
    item_2: Union[Unset, int] = UNSET
    item_3: Union[Unset, int] = UNSET
    item_4: Union[Unset, int] = UNSET
    item_5: Union[Unset, int] = UNSET
    item_uses: Union[Unset, "MatchResponsePlayersItemItemUses"] = UNSET
    kill_streaks: Union[Unset, "MatchResponsePlayersItemKillStreaks"] = UNSET
    killed: Union[Unset, "MatchResponsePlayersItemKilled"] = UNSET
    killed_by: Union[Unset, "MatchResponsePlayersItemKilledBy"] = UNSET
    kills: Union[Unset, int] = UNSET
    kills_log: Union[Unset, List["MatchResponsePlayersItemKillsLogItem"]] = UNSET
    lane_pos: Union[Unset, "MatchResponsePlayersItemLanePos"] = UNSET
    last_hits: Union[Unset, int] = UNSET
    leaver_status: Union[Unset, int] = UNSET
    level: Union[Unset, int] = UNSET
    lh_t: Union[Unset, List[int]] = UNSET
    life_state: Union[Unset, "MatchResponsePlayersItemLifeState"] = UNSET
    max_hero_hit: Union[Unset, "MatchResponsePlayersItemMaxHeroHit"] = UNSET
    multi_kills: Union[Unset, "MatchResponsePlayersItemMultiKills"] = UNSET
    obs: Union[Unset, "MatchResponsePlayersItemObs"] = UNSET
    obs_left_log: Union[Unset, List["MatchResponsePlayersItemObsLeftLogItem"]] = UNSET
    obs_log: Union[Unset, List["MatchResponsePlayersItemObsLogItem"]] = UNSET
    obs_placed: Union[Unset, int] = UNSET
    party_id: Union[Unset, int] = UNSET
    permanent_buffs: Union[Unset, List["MatchResponsePlayersItemPermanentBuffsItem"]] = UNSET
    pings: Union[Unset, int] = UNSET
    purchase: Union[Unset, "MatchResponsePlayersItemPurchase"] = UNSET
    purchase_log: Union[Unset, List["MatchResponsePlayersItemPurchaseLogItem"]] = UNSET
    rune_pickups: Union[Unset, int] = UNSET
    runes: Union[Unset, "MatchResponsePlayersItemRunes"] = UNSET
    runes_log: Union[Unset, List["MatchResponsePlayersItemRunesLogItem"]] = UNSET
    sen: Union[Unset, "MatchResponsePlayersItemSen"] = UNSET
    sen_left_log: Union[Unset, List["MatchResponsePlayersItemSenLeftLogItem"]] = UNSET
    sen_log: Union[Unset, List["MatchResponsePlayersItemSenLogItem"]] = UNSET
    sen_placed: Union[Unset, int] = UNSET
    stuns: Union[Unset, float] = UNSET
    times: Union[Unset, List[int]] = UNSET
    tower_damage: Union[Unset, int] = UNSET
    xp_per_min: Union[Unset, int] = UNSET
    xp_reasons: Union[Unset, "MatchResponsePlayersItemXpReasons"] = UNSET
    xp_t: Union[Unset, List[int]] = UNSET
    personaname: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    last_login: Union[Unset, None, datetime.datetime] = UNSET
    radiant_win: Union[Unset, None, bool] = UNSET
    start_time: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    cluster: Union[Unset, int] = UNSET
    lobby_type: Union[Unset, int] = UNSET
    game_mode: Union[Unset, int] = UNSET
    patch: Union[Unset, int] = UNSET
    region: Union[Unset, int] = UNSET
    is_radiant: Union[Unset, bool] = UNSET
    win: Union[Unset, int] = UNSET
    lose: Union[Unset, int] = UNSET
    total_gold: Union[Unset, int] = UNSET
    total_xp: Union[Unset, int] = UNSET
    kills_per_min: Union[Unset, float] = UNSET
    kda: Union[Unset, float] = UNSET
    abandons: Union[Unset, int] = UNSET
    neutral_kills: Union[Unset, int] = UNSET
    tower_kills: Union[Unset, int] = UNSET
    courier_kills: Union[Unset, int] = UNSET
    lane_kills: Union[Unset, int] = UNSET
    hero_kills: Union[Unset, int] = UNSET
    observer_kills: Union[Unset, int] = UNSET
    sentry_kills: Union[Unset, int] = UNSET
    roshan_kills: Union[Unset, int] = UNSET
    necronomicon_kills: Union[Unset, int] = UNSET
    ancient_kills: Union[Unset, int] = UNSET
    buyback_count: Union[Unset, int] = UNSET
    observer_uses: Union[Unset, int] = UNSET
    sentry_uses: Union[Unset, int] = UNSET
    lane_efficiency: Union[Unset, float] = UNSET
    lane_efficiency_pct: Union[Unset, float] = UNSET
    lane: Union[Unset, None, int] = UNSET
    lane_role: Union[Unset, None, int] = UNSET
    is_roaming: Union[Unset, None, bool] = UNSET
    purchase_time: Union[Unset, "MatchResponsePlayersItemPurchaseTime"] = UNSET
    first_purchase_time: Union[Unset, "MatchResponsePlayersItemFirstPurchaseTime"] = UNSET
    item_win: Union[Unset, "MatchResponsePlayersItemItemWin"] = UNSET
    item_usage: Union[Unset, "MatchResponsePlayersItemItemUsage"] = UNSET
    purchase_tpscroll: Union[Unset, int] = UNSET
    actions_per_min: Union[Unset, int] = UNSET
    life_state_dead: Union[Unset, int] = UNSET
    rank_tier: Union[Unset, int] = UNSET
    cosmetics: Union[Unset, List["MatchResponsePlayersItemCosmeticsItem"]] = UNSET
    benchmarks: Union[Unset, "MatchResponsePlayersItemBenchmarks"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        match_id = self.match_id
        player_slot = self.player_slot
        ability_upgrades_arr: Union[Unset, List[int]] = UNSET
        if not isinstance(self.ability_upgrades_arr, Unset):
            ability_upgrades_arr = self.ability_upgrades_arr

        ability_uses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ability_uses, Unset):
            ability_uses = self.ability_uses.to_dict()

        ability_targets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ability_targets, Unset):
            ability_targets = self.ability_targets.to_dict()

        damage_targets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.damage_targets, Unset):
            damage_targets = self.damage_targets.to_dict()

        account_id = self.account_id
        actions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions.to_dict()

        additional_units: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_units, Unset):
            if self.additional_units is None:
                additional_units = None
            else:
                additional_units = []
                for additional_units_item_data in self.additional_units:
                    additional_units_item = additional_units_item_data.to_dict()

                    additional_units.append(additional_units_item)

        assists = self.assists
        backpack_0 = self.backpack_0
        backpack_1 = self.backpack_1
        backpack_2 = self.backpack_2
        buyback_log: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.buyback_log, Unset):
            buyback_log = []
            for buyback_log_item_data in self.buyback_log:
                buyback_log_item = buyback_log_item_data.to_dict()

                buyback_log.append(buyback_log_item)

        camps_stacked = self.camps_stacked
        connection_log: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.connection_log, Unset):
            connection_log = []
            for connection_log_item_data in self.connection_log:
                connection_log_item = connection_log_item_data.to_dict()

                connection_log.append(connection_log_item)

        creeps_stacked = self.creeps_stacked
        damage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.damage, Unset):
            damage = self.damage.to_dict()

        damage_inflictor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.damage_inflictor, Unset):
            damage_inflictor = self.damage_inflictor.to_dict()

        damage_inflictor_received: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.damage_inflictor_received, Unset):
            damage_inflictor_received = self.damage_inflictor_received.to_dict()

        damage_taken: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.damage_taken, Unset):
            damage_taken = self.damage_taken.to_dict()

        deaths = self.deaths
        denies = self.denies
        dn_t: Union[Unset, List[int]] = UNSET
        if not isinstance(self.dn_t, Unset):
            dn_t = self.dn_t

        gold = self.gold
        gold_per_min = self.gold_per_min
        gold_reasons: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gold_reasons, Unset):
            gold_reasons = self.gold_reasons.to_dict()

        gold_spent = self.gold_spent
        gold_t: Union[Unset, List[int]] = UNSET
        if not isinstance(self.gold_t, Unset):
            gold_t = self.gold_t

        hero_damage = self.hero_damage
        hero_healing = self.hero_healing
        hero_hits: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hero_hits, Unset):
            hero_hits = self.hero_hits.to_dict()

        hero_id = self.hero_id
        item_0 = self.item_0
        item_1 = self.item_1
        item_2 = self.item_2
        item_3 = self.item_3
        item_4 = self.item_4
        item_5 = self.item_5
        item_uses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_uses, Unset):
            item_uses = self.item_uses.to_dict()

        kill_streaks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.kill_streaks, Unset):
            kill_streaks = self.kill_streaks.to_dict()

        killed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.killed, Unset):
            killed = self.killed.to_dict()

        killed_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.killed_by, Unset):
            killed_by = self.killed_by.to_dict()

        kills = self.kills
        kills_log: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.kills_log, Unset):
            kills_log = []
            for kills_log_item_data in self.kills_log:
                kills_log_item = kills_log_item_data.to_dict()

                kills_log.append(kills_log_item)

        lane_pos: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lane_pos, Unset):
            lane_pos = self.lane_pos.to_dict()

        last_hits = self.last_hits
        leaver_status = self.leaver_status
        level = self.level
        lh_t: Union[Unset, List[int]] = UNSET
        if not isinstance(self.lh_t, Unset):
            lh_t = self.lh_t

        life_state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.life_state, Unset):
            life_state = self.life_state.to_dict()

        max_hero_hit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.max_hero_hit, Unset):
            max_hero_hit = self.max_hero_hit.to_dict()

        multi_kills: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.multi_kills, Unset):
            multi_kills = self.multi_kills.to_dict()

        obs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.obs, Unset):
            obs = self.obs.to_dict()

        obs_left_log: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.obs_left_log, Unset):
            obs_left_log = []
            for obs_left_log_item_data in self.obs_left_log:
                obs_left_log_item = obs_left_log_item_data.to_dict()

                obs_left_log.append(obs_left_log_item)

        obs_log: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.obs_log, Unset):
            obs_log = []
            for obs_log_item_data in self.obs_log:
                obs_log_item = obs_log_item_data.to_dict()

                obs_log.append(obs_log_item)

        obs_placed = self.obs_placed
        party_id = self.party_id
        permanent_buffs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permanent_buffs, Unset):
            permanent_buffs = []
            for permanent_buffs_item_data in self.permanent_buffs:
                permanent_buffs_item = permanent_buffs_item_data.to_dict()

                permanent_buffs.append(permanent_buffs_item)

        pings = self.pings
        purchase: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.purchase, Unset):
            purchase = self.purchase.to_dict()

        purchase_log: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.purchase_log, Unset):
            purchase_log = []
            for purchase_log_item_data in self.purchase_log:
                purchase_log_item = purchase_log_item_data.to_dict()

                purchase_log.append(purchase_log_item)

        rune_pickups = self.rune_pickups
        runes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.runes, Unset):
            runes = self.runes.to_dict()

        runes_log: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.runes_log, Unset):
            runes_log = []
            for runes_log_item_data in self.runes_log:
                runes_log_item = runes_log_item_data.to_dict()

                runes_log.append(runes_log_item)

        sen: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sen, Unset):
            sen = self.sen.to_dict()

        sen_left_log: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sen_left_log, Unset):
            sen_left_log = []
            for sen_left_log_item_data in self.sen_left_log:
                sen_left_log_item = sen_left_log_item_data.to_dict()

                sen_left_log.append(sen_left_log_item)

        sen_log: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sen_log, Unset):
            sen_log = []
            for sen_log_item_data in self.sen_log:
                sen_log_item = sen_log_item_data.to_dict()

                sen_log.append(sen_log_item)

        sen_placed = self.sen_placed
        stuns = self.stuns
        times: Union[Unset, List[int]] = UNSET
        if not isinstance(self.times, Unset):
            times = self.times

        tower_damage = self.tower_damage
        xp_per_min = self.xp_per_min
        xp_reasons: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.xp_reasons, Unset):
            xp_reasons = self.xp_reasons.to_dict()

        xp_t: Union[Unset, List[int]] = UNSET
        if not isinstance(self.xp_t, Unset):
            xp_t = self.xp_t

        personaname = self.personaname
        name = self.name
        last_login: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_login, Unset):
            last_login = self.last_login.isoformat() if self.last_login else None

        radiant_win = self.radiant_win
        start_time = self.start_time
        duration = self.duration
        cluster = self.cluster
        lobby_type = self.lobby_type
        game_mode = self.game_mode
        patch = self.patch
        region = self.region
        is_radiant = self.is_radiant
        win = self.win
        lose = self.lose
        total_gold = self.total_gold
        total_xp = self.total_xp
        kills_per_min = self.kills_per_min
        kda = self.kda
        abandons = self.abandons
        neutral_kills = self.neutral_kills
        tower_kills = self.tower_kills
        courier_kills = self.courier_kills
        lane_kills = self.lane_kills
        hero_kills = self.hero_kills
        observer_kills = self.observer_kills
        sentry_kills = self.sentry_kills
        roshan_kills = self.roshan_kills
        necronomicon_kills = self.necronomicon_kills
        ancient_kills = self.ancient_kills
        buyback_count = self.buyback_count
        observer_uses = self.observer_uses
        sentry_uses = self.sentry_uses
        lane_efficiency = self.lane_efficiency
        lane_efficiency_pct = self.lane_efficiency_pct
        lane = self.lane
        lane_role = self.lane_role
        is_roaming = self.is_roaming
        purchase_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.purchase_time, Unset):
            purchase_time = self.purchase_time.to_dict()

        first_purchase_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.first_purchase_time, Unset):
            first_purchase_time = self.first_purchase_time.to_dict()

        item_win: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_win, Unset):
            item_win = self.item_win.to_dict()

        item_usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item_usage, Unset):
            item_usage = self.item_usage.to_dict()

        purchase_tpscroll = self.purchase_tpscroll
        actions_per_min = self.actions_per_min
        life_state_dead = self.life_state_dead
        rank_tier = self.rank_tier
        cosmetics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cosmetics, Unset):
            cosmetics = []
            for cosmetics_item_data in self.cosmetics:
                cosmetics_item = cosmetics_item_data.to_dict()

                cosmetics.append(cosmetics_item)

        benchmarks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.benchmarks, Unset):
            benchmarks = self.benchmarks.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_id is not UNSET:
            field_dict["match_id"] = match_id
        if player_slot is not UNSET:
            field_dict["player_slot"] = player_slot
        if ability_upgrades_arr is not UNSET:
            field_dict["ability_upgrades_arr"] = ability_upgrades_arr
        if ability_uses is not UNSET:
            field_dict["ability_uses"] = ability_uses
        if ability_targets is not UNSET:
            field_dict["ability_targets"] = ability_targets
        if damage_targets is not UNSET:
            field_dict["damage_targets"] = damage_targets
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if actions is not UNSET:
            field_dict["actions"] = actions
        if additional_units is not UNSET:
            field_dict["additional_units"] = additional_units
        if assists is not UNSET:
            field_dict["assists"] = assists
        if backpack_0 is not UNSET:
            field_dict["backpack_0"] = backpack_0
        if backpack_1 is not UNSET:
            field_dict["backpack_1"] = backpack_1
        if backpack_2 is not UNSET:
            field_dict["backpack_2"] = backpack_2
        if buyback_log is not UNSET:
            field_dict["buyback_log"] = buyback_log
        if camps_stacked is not UNSET:
            field_dict["camps_stacked"] = camps_stacked
        if connection_log is not UNSET:
            field_dict["connection_log"] = connection_log
        if creeps_stacked is not UNSET:
            field_dict["creeps_stacked"] = creeps_stacked
        if damage is not UNSET:
            field_dict["damage"] = damage
        if damage_inflictor is not UNSET:
            field_dict["damage_inflictor"] = damage_inflictor
        if damage_inflictor_received is not UNSET:
            field_dict["damage_inflictor_received"] = damage_inflictor_received
        if damage_taken is not UNSET:
            field_dict["damage_taken"] = damage_taken
        if deaths is not UNSET:
            field_dict["deaths"] = deaths
        if denies is not UNSET:
            field_dict["denies"] = denies
        if dn_t is not UNSET:
            field_dict["dn_t"] = dn_t
        if gold is not UNSET:
            field_dict["gold"] = gold
        if gold_per_min is not UNSET:
            field_dict["gold_per_min"] = gold_per_min
        if gold_reasons is not UNSET:
            field_dict["gold_reasons"] = gold_reasons
        if gold_spent is not UNSET:
            field_dict["gold_spent"] = gold_spent
        if gold_t is not UNSET:
            field_dict["gold_t"] = gold_t
        if hero_damage is not UNSET:
            field_dict["hero_damage"] = hero_damage
        if hero_healing is not UNSET:
            field_dict["hero_healing"] = hero_healing
        if hero_hits is not UNSET:
            field_dict["hero_hits"] = hero_hits
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if item_0 is not UNSET:
            field_dict["item_0"] = item_0
        if item_1 is not UNSET:
            field_dict["item_1"] = item_1
        if item_2 is not UNSET:
            field_dict["item_2"] = item_2
        if item_3 is not UNSET:
            field_dict["item_3"] = item_3
        if item_4 is not UNSET:
            field_dict["item_4"] = item_4
        if item_5 is not UNSET:
            field_dict["item_5"] = item_5
        if item_uses is not UNSET:
            field_dict["item_uses"] = item_uses
        if kill_streaks is not UNSET:
            field_dict["kill_streaks"] = kill_streaks
        if killed is not UNSET:
            field_dict["killed"] = killed
        if killed_by is not UNSET:
            field_dict["killed_by"] = killed_by
        if kills is not UNSET:
            field_dict["kills"] = kills
        if kills_log is not UNSET:
            field_dict["kills_log"] = kills_log
        if lane_pos is not UNSET:
            field_dict["lane_pos"] = lane_pos
        if last_hits is not UNSET:
            field_dict["last_hits"] = last_hits
        if leaver_status is not UNSET:
            field_dict["leaver_status"] = leaver_status
        if level is not UNSET:
            field_dict["level"] = level
        if lh_t is not UNSET:
            field_dict["lh_t"] = lh_t
        if life_state is not UNSET:
            field_dict["life_state"] = life_state
        if max_hero_hit is not UNSET:
            field_dict["max_hero_hit"] = max_hero_hit
        if multi_kills is not UNSET:
            field_dict["multi_kills"] = multi_kills
        if obs is not UNSET:
            field_dict["obs"] = obs
        if obs_left_log is not UNSET:
            field_dict["obs_left_log"] = obs_left_log
        if obs_log is not UNSET:
            field_dict["obs_log"] = obs_log
        if obs_placed is not UNSET:
            field_dict["obs_placed"] = obs_placed
        if party_id is not UNSET:
            field_dict["party_id"] = party_id
        if permanent_buffs is not UNSET:
            field_dict["permanent_buffs"] = permanent_buffs
        if pings is not UNSET:
            field_dict["pings"] = pings
        if purchase is not UNSET:
            field_dict["purchase"] = purchase
        if purchase_log is not UNSET:
            field_dict["purchase_log"] = purchase_log
        if rune_pickups is not UNSET:
            field_dict["rune_pickups"] = rune_pickups
        if runes is not UNSET:
            field_dict["runes"] = runes
        if runes_log is not UNSET:
            field_dict["runes_log"] = runes_log
        if sen is not UNSET:
            field_dict["sen"] = sen
        if sen_left_log is not UNSET:
            field_dict["sen_left_log"] = sen_left_log
        if sen_log is not UNSET:
            field_dict["sen_log"] = sen_log
        if sen_placed is not UNSET:
            field_dict["sen_placed"] = sen_placed
        if stuns is not UNSET:
            field_dict["stuns"] = stuns
        if times is not UNSET:
            field_dict["times"] = times
        if tower_damage is not UNSET:
            field_dict["tower_damage"] = tower_damage
        if xp_per_min is not UNSET:
            field_dict["xp_per_min"] = xp_per_min
        if xp_reasons is not UNSET:
            field_dict["xp_reasons"] = xp_reasons
        if xp_t is not UNSET:
            field_dict["xp_t"] = xp_t
        if personaname is not UNSET:
            field_dict["personaname"] = personaname
        if name is not UNSET:
            field_dict["name"] = name
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if radiant_win is not UNSET:
            field_dict["radiant_win"] = radiant_win
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if lobby_type is not UNSET:
            field_dict["lobby_type"] = lobby_type
        if game_mode is not UNSET:
            field_dict["game_mode"] = game_mode
        if patch is not UNSET:
            field_dict["patch"] = patch
        if region is not UNSET:
            field_dict["region"] = region
        if is_radiant is not UNSET:
            field_dict["isRadiant"] = is_radiant
        if win is not UNSET:
            field_dict["win"] = win
        if lose is not UNSET:
            field_dict["lose"] = lose
        if total_gold is not UNSET:
            field_dict["total_gold"] = total_gold
        if total_xp is not UNSET:
            field_dict["total_xp"] = total_xp
        if kills_per_min is not UNSET:
            field_dict["kills_per_min"] = kills_per_min
        if kda is not UNSET:
            field_dict["kda"] = kda
        if abandons is not UNSET:
            field_dict["abandons"] = abandons
        if neutral_kills is not UNSET:
            field_dict["neutral_kills"] = neutral_kills
        if tower_kills is not UNSET:
            field_dict["tower_kills"] = tower_kills
        if courier_kills is not UNSET:
            field_dict["courier_kills"] = courier_kills
        if lane_kills is not UNSET:
            field_dict["lane_kills"] = lane_kills
        if hero_kills is not UNSET:
            field_dict["hero_kills"] = hero_kills
        if observer_kills is not UNSET:
            field_dict["observer_kills"] = observer_kills
        if sentry_kills is not UNSET:
            field_dict["sentry_kills"] = sentry_kills
        if roshan_kills is not UNSET:
            field_dict["roshan_kills"] = roshan_kills
        if necronomicon_kills is not UNSET:
            field_dict["necronomicon_kills"] = necronomicon_kills
        if ancient_kills is not UNSET:
            field_dict["ancient_kills"] = ancient_kills
        if buyback_count is not UNSET:
            field_dict["buyback_count"] = buyback_count
        if observer_uses is not UNSET:
            field_dict["observer_uses"] = observer_uses
        if sentry_uses is not UNSET:
            field_dict["sentry_uses"] = sentry_uses
        if lane_efficiency is not UNSET:
            field_dict["lane_efficiency"] = lane_efficiency
        if lane_efficiency_pct is not UNSET:
            field_dict["lane_efficiency_pct"] = lane_efficiency_pct
        if lane is not UNSET:
            field_dict["lane"] = lane
        if lane_role is not UNSET:
            field_dict["lane_role"] = lane_role
        if is_roaming is not UNSET:
            field_dict["is_roaming"] = is_roaming
        if purchase_time is not UNSET:
            field_dict["purchase_time"] = purchase_time
        if first_purchase_time is not UNSET:
            field_dict["first_purchase_time"] = first_purchase_time
        if item_win is not UNSET:
            field_dict["item_win"] = item_win
        if item_usage is not UNSET:
            field_dict["item_usage"] = item_usage
        if purchase_tpscroll is not UNSET:
            field_dict["purchase_tpscroll"] = purchase_tpscroll
        if actions_per_min is not UNSET:
            field_dict["actions_per_min"] = actions_per_min
        if life_state_dead is not UNSET:
            field_dict["life_state_dead"] = life_state_dead
        if rank_tier is not UNSET:
            field_dict["rank_tier"] = rank_tier
        if cosmetics is not UNSET:
            field_dict["cosmetics"] = cosmetics
        if benchmarks is not UNSET:
            field_dict["benchmarks"] = benchmarks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.match_response_players_item_ability_targets import MatchResponsePlayersItemAbilityTargets
        from ..models.match_response_players_item_ability_uses import MatchResponsePlayersItemAbilityUses
        from ..models.match_response_players_item_actions import MatchResponsePlayersItemActions
        from ..models.match_response_players_item_additional_units_item import (
            MatchResponsePlayersItemAdditionalUnitsItem,
        )
        from ..models.match_response_players_item_benchmarks import MatchResponsePlayersItemBenchmarks
        from ..models.match_response_players_item_buyback_log_item import MatchResponsePlayersItemBuybackLogItem
        from ..models.match_response_players_item_connection_log_item import MatchResponsePlayersItemConnectionLogItem
        from ..models.match_response_players_item_cosmetics_item import MatchResponsePlayersItemCosmeticsItem
        from ..models.match_response_players_item_damage import MatchResponsePlayersItemDamage
        from ..models.match_response_players_item_damage_inflictor import MatchResponsePlayersItemDamageInflictor
        from ..models.match_response_players_item_damage_inflictor_received import (
            MatchResponsePlayersItemDamageInflictorReceived,
        )
        from ..models.match_response_players_item_damage_taken import MatchResponsePlayersItemDamageTaken
        from ..models.match_response_players_item_damage_targets import MatchResponsePlayersItemDamageTargets
        from ..models.match_response_players_item_first_purchase_time import MatchResponsePlayersItemFirstPurchaseTime
        from ..models.match_response_players_item_gold_reasons import MatchResponsePlayersItemGoldReasons
        from ..models.match_response_players_item_hero_hits import MatchResponsePlayersItemHeroHits
        from ..models.match_response_players_item_item_usage import MatchResponsePlayersItemItemUsage
        from ..models.match_response_players_item_item_uses import MatchResponsePlayersItemItemUses
        from ..models.match_response_players_item_item_win import MatchResponsePlayersItemItemWin
        from ..models.match_response_players_item_kill_streaks import MatchResponsePlayersItemKillStreaks
        from ..models.match_response_players_item_killed import MatchResponsePlayersItemKilled
        from ..models.match_response_players_item_killed_by import MatchResponsePlayersItemKilledBy
        from ..models.match_response_players_item_kills_log_item import MatchResponsePlayersItemKillsLogItem
        from ..models.match_response_players_item_lane_pos import MatchResponsePlayersItemLanePos
        from ..models.match_response_players_item_life_state import MatchResponsePlayersItemLifeState
        from ..models.match_response_players_item_max_hero_hit import MatchResponsePlayersItemMaxHeroHit
        from ..models.match_response_players_item_multi_kills import MatchResponsePlayersItemMultiKills
        from ..models.match_response_players_item_obs import MatchResponsePlayersItemObs
        from ..models.match_response_players_item_obs_left_log_item import MatchResponsePlayersItemObsLeftLogItem
        from ..models.match_response_players_item_obs_log_item import MatchResponsePlayersItemObsLogItem
        from ..models.match_response_players_item_permanent_buffs_item import MatchResponsePlayersItemPermanentBuffsItem
        from ..models.match_response_players_item_purchase import MatchResponsePlayersItemPurchase
        from ..models.match_response_players_item_purchase_log_item import MatchResponsePlayersItemPurchaseLogItem
        from ..models.match_response_players_item_purchase_time import MatchResponsePlayersItemPurchaseTime
        from ..models.match_response_players_item_runes import MatchResponsePlayersItemRunes
        from ..models.match_response_players_item_runes_log_item import MatchResponsePlayersItemRunesLogItem
        from ..models.match_response_players_item_sen import MatchResponsePlayersItemSen
        from ..models.match_response_players_item_sen_left_log_item import MatchResponsePlayersItemSenLeftLogItem
        from ..models.match_response_players_item_sen_log_item import MatchResponsePlayersItemSenLogItem
        from ..models.match_response_players_item_xp_reasons import MatchResponsePlayersItemXpReasons

        d = src_dict.copy()
        match_id = d.pop("match_id", UNSET)

        player_slot = d.pop("player_slot", UNSET)

        ability_upgrades_arr = cast(List[int], d.pop("ability_upgrades_arr", UNSET))

        _ability_uses = d.pop("ability_uses", UNSET)
        ability_uses: Union[Unset, MatchResponsePlayersItemAbilityUses]
        if isinstance(_ability_uses, Unset):
            ability_uses = UNSET
        else:
            ability_uses = MatchResponsePlayersItemAbilityUses.from_dict(_ability_uses)

        _ability_targets = d.pop("ability_targets", UNSET)
        ability_targets: Union[Unset, MatchResponsePlayersItemAbilityTargets]
        if isinstance(_ability_targets, Unset):
            ability_targets = UNSET
        else:
            ability_targets = MatchResponsePlayersItemAbilityTargets.from_dict(_ability_targets)

        _damage_targets = d.pop("damage_targets", UNSET)
        damage_targets: Union[Unset, MatchResponsePlayersItemDamageTargets]
        if isinstance(_damage_targets, Unset):
            damage_targets = UNSET
        else:
            damage_targets = MatchResponsePlayersItemDamageTargets.from_dict(_damage_targets)

        account_id = d.pop("account_id", UNSET)

        _actions = d.pop("actions", UNSET)
        actions: Union[Unset, MatchResponsePlayersItemActions]
        if isinstance(_actions, Unset):
            actions = UNSET
        else:
            actions = MatchResponsePlayersItemActions.from_dict(_actions)

        additional_units = []
        _additional_units = d.pop("additional_units", UNSET)
        for additional_units_item_data in _additional_units or []:
            additional_units_item = MatchResponsePlayersItemAdditionalUnitsItem.from_dict(additional_units_item_data)

            additional_units.append(additional_units_item)

        assists = d.pop("assists", UNSET)

        backpack_0 = d.pop("backpack_0", UNSET)

        backpack_1 = d.pop("backpack_1", UNSET)

        backpack_2 = d.pop("backpack_2", UNSET)

        buyback_log = []
        _buyback_log = d.pop("buyback_log", UNSET)
        for buyback_log_item_data in _buyback_log or []:
            buyback_log_item = MatchResponsePlayersItemBuybackLogItem.from_dict(buyback_log_item_data)

            buyback_log.append(buyback_log_item)

        camps_stacked = d.pop("camps_stacked", UNSET)

        connection_log = []
        _connection_log = d.pop("connection_log", UNSET)
        for connection_log_item_data in _connection_log or []:
            connection_log_item = MatchResponsePlayersItemConnectionLogItem.from_dict(connection_log_item_data)

            connection_log.append(connection_log_item)

        creeps_stacked = d.pop("creeps_stacked", UNSET)

        _damage = d.pop("damage", UNSET)
        damage: Union[Unset, MatchResponsePlayersItemDamage]
        if isinstance(_damage, Unset):
            damage = UNSET
        else:
            damage = MatchResponsePlayersItemDamage.from_dict(_damage)

        _damage_inflictor = d.pop("damage_inflictor", UNSET)
        damage_inflictor: Union[Unset, MatchResponsePlayersItemDamageInflictor]
        if isinstance(_damage_inflictor, Unset):
            damage_inflictor = UNSET
        else:
            damage_inflictor = MatchResponsePlayersItemDamageInflictor.from_dict(_damage_inflictor)

        _damage_inflictor_received = d.pop("damage_inflictor_received", UNSET)
        damage_inflictor_received: Union[Unset, MatchResponsePlayersItemDamageInflictorReceived]
        if isinstance(_damage_inflictor_received, Unset):
            damage_inflictor_received = UNSET
        else:
            damage_inflictor_received = MatchResponsePlayersItemDamageInflictorReceived.from_dict(
                _damage_inflictor_received
            )

        _damage_taken = d.pop("damage_taken", UNSET)
        damage_taken: Union[Unset, MatchResponsePlayersItemDamageTaken]
        if isinstance(_damage_taken, Unset):
            damage_taken = UNSET
        else:
            damage_taken = MatchResponsePlayersItemDamageTaken.from_dict(_damage_taken)

        deaths = d.pop("deaths", UNSET)

        denies = d.pop("denies", UNSET)

        dn_t = cast(List[int], d.pop("dn_t", UNSET))

        gold = d.pop("gold", UNSET)

        gold_per_min = d.pop("gold_per_min", UNSET)

        _gold_reasons = d.pop("gold_reasons", UNSET)
        gold_reasons: Union[Unset, MatchResponsePlayersItemGoldReasons]
        if isinstance(_gold_reasons, Unset):
            gold_reasons = UNSET
        else:
            gold_reasons = MatchResponsePlayersItemGoldReasons.from_dict(_gold_reasons)

        gold_spent = d.pop("gold_spent", UNSET)

        gold_t = cast(List[int], d.pop("gold_t", UNSET))

        hero_damage = d.pop("hero_damage", UNSET)

        hero_healing = d.pop("hero_healing", UNSET)

        _hero_hits = d.pop("hero_hits", UNSET)
        hero_hits: Union[Unset, MatchResponsePlayersItemHeroHits]
        if isinstance(_hero_hits, Unset):
            hero_hits = UNSET
        else:
            hero_hits = MatchResponsePlayersItemHeroHits.from_dict(_hero_hits)

        hero_id = d.pop("hero_id", UNSET)

        item_0 = d.pop("item_0", UNSET)

        item_1 = d.pop("item_1", UNSET)

        item_2 = d.pop("item_2", UNSET)

        item_3 = d.pop("item_3", UNSET)

        item_4 = d.pop("item_4", UNSET)

        item_5 = d.pop("item_5", UNSET)

        _item_uses = d.pop("item_uses", UNSET)
        item_uses: Union[Unset, MatchResponsePlayersItemItemUses]
        if isinstance(_item_uses, Unset):
            item_uses = UNSET
        else:
            item_uses = MatchResponsePlayersItemItemUses.from_dict(_item_uses)

        _kill_streaks = d.pop("kill_streaks", UNSET)
        kill_streaks: Union[Unset, MatchResponsePlayersItemKillStreaks]
        if isinstance(_kill_streaks, Unset):
            kill_streaks = UNSET
        else:
            kill_streaks = MatchResponsePlayersItemKillStreaks.from_dict(_kill_streaks)

        _killed = d.pop("killed", UNSET)
        killed: Union[Unset, MatchResponsePlayersItemKilled]
        if isinstance(_killed, Unset):
            killed = UNSET
        else:
            killed = MatchResponsePlayersItemKilled.from_dict(_killed)

        _killed_by = d.pop("killed_by", UNSET)
        killed_by: Union[Unset, MatchResponsePlayersItemKilledBy]
        if isinstance(_killed_by, Unset):
            killed_by = UNSET
        else:
            killed_by = MatchResponsePlayersItemKilledBy.from_dict(_killed_by)

        kills = d.pop("kills", UNSET)

        kills_log = []
        _kills_log = d.pop("kills_log", UNSET)
        for kills_log_item_data in _kills_log or []:
            kills_log_item = MatchResponsePlayersItemKillsLogItem.from_dict(kills_log_item_data)

            kills_log.append(kills_log_item)

        _lane_pos = d.pop("lane_pos", UNSET)
        lane_pos: Union[Unset, MatchResponsePlayersItemLanePos]
        if isinstance(_lane_pos, Unset):
            lane_pos = UNSET
        else:
            lane_pos = MatchResponsePlayersItemLanePos.from_dict(_lane_pos)

        last_hits = d.pop("last_hits", UNSET)

        leaver_status = d.pop("leaver_status", UNSET)

        level = d.pop("level", UNSET)

        lh_t = cast(List[int], d.pop("lh_t", UNSET))

        _life_state = d.pop("life_state", UNSET)
        life_state: Union[Unset, MatchResponsePlayersItemLifeState]
        if isinstance(_life_state, Unset):
            life_state = UNSET
        else:
            life_state = MatchResponsePlayersItemLifeState.from_dict(_life_state)

        _max_hero_hit = d.pop("max_hero_hit", UNSET)
        max_hero_hit: Union[Unset, MatchResponsePlayersItemMaxHeroHit]
        if isinstance(_max_hero_hit, Unset):
            max_hero_hit = UNSET
        else:
            max_hero_hit = MatchResponsePlayersItemMaxHeroHit.from_dict(_max_hero_hit)

        _multi_kills = d.pop("multi_kills", UNSET)
        multi_kills: Union[Unset, MatchResponsePlayersItemMultiKills]
        if isinstance(_multi_kills, Unset):
            multi_kills = UNSET
        else:
            multi_kills = MatchResponsePlayersItemMultiKills.from_dict(_multi_kills)

        _obs = d.pop("obs", UNSET)
        obs: Union[Unset, MatchResponsePlayersItemObs]
        if isinstance(_obs, Unset):
            obs = UNSET
        else:
            obs = MatchResponsePlayersItemObs.from_dict(_obs)

        obs_left_log = []
        _obs_left_log = d.pop("obs_left_log", UNSET)
        for obs_left_log_item_data in _obs_left_log or []:
            obs_left_log_item = MatchResponsePlayersItemObsLeftLogItem.from_dict(obs_left_log_item_data)

            obs_left_log.append(obs_left_log_item)

        obs_log = []
        _obs_log = d.pop("obs_log", UNSET)
        for obs_log_item_data in _obs_log or []:
            obs_log_item = MatchResponsePlayersItemObsLogItem.from_dict(obs_log_item_data)

            obs_log.append(obs_log_item)

        obs_placed = d.pop("obs_placed", UNSET)

        party_id = d.pop("party_id", UNSET)

        permanent_buffs = []
        _permanent_buffs = d.pop("permanent_buffs", UNSET)
        for permanent_buffs_item_data in _permanent_buffs or []:
            permanent_buffs_item = MatchResponsePlayersItemPermanentBuffsItem.from_dict(permanent_buffs_item_data)

            permanent_buffs.append(permanent_buffs_item)

        pings = d.pop("pings", UNSET)

        _purchase = d.pop("purchase", UNSET)
        purchase: Union[Unset, MatchResponsePlayersItemPurchase]
        if isinstance(_purchase, Unset):
            purchase = UNSET
        else:
            purchase = MatchResponsePlayersItemPurchase.from_dict(_purchase)

        purchase_log = []
        _purchase_log = d.pop("purchase_log", UNSET)
        for purchase_log_item_data in _purchase_log or []:
            purchase_log_item = MatchResponsePlayersItemPurchaseLogItem.from_dict(purchase_log_item_data)

            purchase_log.append(purchase_log_item)

        rune_pickups = d.pop("rune_pickups", UNSET)

        _runes = d.pop("runes", UNSET)
        runes: Union[Unset, MatchResponsePlayersItemRunes]
        if isinstance(_runes, Unset):
            runes = UNSET
        else:
            runes = MatchResponsePlayersItemRunes.from_dict(_runes)

        runes_log = []
        _runes_log = d.pop("runes_log", UNSET)
        for runes_log_item_data in _runes_log or []:
            runes_log_item = MatchResponsePlayersItemRunesLogItem.from_dict(runes_log_item_data)

            runes_log.append(runes_log_item)

        _sen = d.pop("sen", UNSET)
        sen: Union[Unset, MatchResponsePlayersItemSen]
        if isinstance(_sen, Unset):
            sen = UNSET
        else:
            sen = MatchResponsePlayersItemSen.from_dict(_sen)

        sen_left_log = []
        _sen_left_log = d.pop("sen_left_log", UNSET)
        for sen_left_log_item_data in _sen_left_log or []:
            sen_left_log_item = MatchResponsePlayersItemSenLeftLogItem.from_dict(sen_left_log_item_data)

            sen_left_log.append(sen_left_log_item)

        sen_log = []
        _sen_log = d.pop("sen_log", UNSET)
        for sen_log_item_data in _sen_log or []:
            sen_log_item = MatchResponsePlayersItemSenLogItem.from_dict(sen_log_item_data)

            sen_log.append(sen_log_item)

        sen_placed = d.pop("sen_placed", UNSET)

        stuns = d.pop("stuns", UNSET)

        times = cast(List[int], d.pop("times", UNSET))

        tower_damage = d.pop("tower_damage", UNSET)

        xp_per_min = d.pop("xp_per_min", UNSET)

        _xp_reasons = d.pop("xp_reasons", UNSET)
        xp_reasons: Union[Unset, MatchResponsePlayersItemXpReasons]
        if isinstance(_xp_reasons, Unset):
            xp_reasons = UNSET
        else:
            xp_reasons = MatchResponsePlayersItemXpReasons.from_dict(_xp_reasons)

        xp_t = cast(List[int], d.pop("xp_t", UNSET))

        personaname = d.pop("personaname", UNSET)

        name = d.pop("name", UNSET)

        _last_login = d.pop("last_login", UNSET)
        last_login: Union[Unset, None, datetime.datetime]
        if _last_login is None:
            last_login = None
        elif isinstance(_last_login, Unset):
            last_login = UNSET
        else:
            last_login = isoparse(_last_login)

        radiant_win = d.pop("radiant_win", UNSET)

        start_time = d.pop("start_time", UNSET)

        duration = d.pop("duration", UNSET)

        cluster = d.pop("cluster", UNSET)

        lobby_type = d.pop("lobby_type", UNSET)

        game_mode = d.pop("game_mode", UNSET)

        patch = d.pop("patch", UNSET)

        region = d.pop("region", UNSET)

        is_radiant = d.pop("isRadiant", UNSET)

        win = d.pop("win", UNSET)

        lose = d.pop("lose", UNSET)

        total_gold = d.pop("total_gold", UNSET)

        total_xp = d.pop("total_xp", UNSET)

        kills_per_min = d.pop("kills_per_min", UNSET)

        kda = d.pop("kda", UNSET)

        abandons = d.pop("abandons", UNSET)

        neutral_kills = d.pop("neutral_kills", UNSET)

        tower_kills = d.pop("tower_kills", UNSET)

        courier_kills = d.pop("courier_kills", UNSET)

        lane_kills = d.pop("lane_kills", UNSET)

        hero_kills = d.pop("hero_kills", UNSET)

        observer_kills = d.pop("observer_kills", UNSET)

        sentry_kills = d.pop("sentry_kills", UNSET)

        roshan_kills = d.pop("roshan_kills", UNSET)

        necronomicon_kills = d.pop("necronomicon_kills", UNSET)

        ancient_kills = d.pop("ancient_kills", UNSET)

        buyback_count = d.pop("buyback_count", UNSET)

        observer_uses = d.pop("observer_uses", UNSET)

        sentry_uses = d.pop("sentry_uses", UNSET)

        lane_efficiency = d.pop("lane_efficiency", UNSET)

        lane_efficiency_pct = d.pop("lane_efficiency_pct", UNSET)

        lane = d.pop("lane", UNSET)

        lane_role = d.pop("lane_role", UNSET)

        is_roaming = d.pop("is_roaming", UNSET)

        _purchase_time = d.pop("purchase_time", UNSET)
        purchase_time: Union[Unset, MatchResponsePlayersItemPurchaseTime]
        if isinstance(_purchase_time, Unset):
            purchase_time = UNSET
        else:
            purchase_time = MatchResponsePlayersItemPurchaseTime.from_dict(_purchase_time)

        _first_purchase_time = d.pop("first_purchase_time", UNSET)
        first_purchase_time: Union[Unset, MatchResponsePlayersItemFirstPurchaseTime]
        if isinstance(_first_purchase_time, Unset):
            first_purchase_time = UNSET
        else:
            first_purchase_time = MatchResponsePlayersItemFirstPurchaseTime.from_dict(_first_purchase_time)

        _item_win = d.pop("item_win", UNSET)
        item_win: Union[Unset, MatchResponsePlayersItemItemWin]
        if isinstance(_item_win, Unset):
            item_win = UNSET
        else:
            item_win = MatchResponsePlayersItemItemWin.from_dict(_item_win)

        _item_usage = d.pop("item_usage", UNSET)
        item_usage: Union[Unset, MatchResponsePlayersItemItemUsage]
        if isinstance(_item_usage, Unset):
            item_usage = UNSET
        else:
            item_usage = MatchResponsePlayersItemItemUsage.from_dict(_item_usage)

        purchase_tpscroll = d.pop("purchase_tpscroll", UNSET)

        actions_per_min = d.pop("actions_per_min", UNSET)

        life_state_dead = d.pop("life_state_dead", UNSET)

        rank_tier = d.pop("rank_tier", UNSET)

        cosmetics = []
        _cosmetics = d.pop("cosmetics", UNSET)
        for cosmetics_item_data in _cosmetics or []:
            cosmetics_item = MatchResponsePlayersItemCosmeticsItem.from_dict(cosmetics_item_data)

            cosmetics.append(cosmetics_item)

        _benchmarks = d.pop("benchmarks", UNSET)
        benchmarks: Union[Unset, MatchResponsePlayersItemBenchmarks]
        if isinstance(_benchmarks, Unset):
            benchmarks = UNSET
        else:
            benchmarks = MatchResponsePlayersItemBenchmarks.from_dict(_benchmarks)

        match_response_players_item = cls(
            match_id=match_id,
            player_slot=player_slot,
            ability_upgrades_arr=ability_upgrades_arr,
            ability_uses=ability_uses,
            ability_targets=ability_targets,
            damage_targets=damage_targets,
            account_id=account_id,
            actions=actions,
            additional_units=additional_units,
            assists=assists,
            backpack_0=backpack_0,
            backpack_1=backpack_1,
            backpack_2=backpack_2,
            buyback_log=buyback_log,
            camps_stacked=camps_stacked,
            connection_log=connection_log,
            creeps_stacked=creeps_stacked,
            damage=damage,
            damage_inflictor=damage_inflictor,
            damage_inflictor_received=damage_inflictor_received,
            damage_taken=damage_taken,
            deaths=deaths,
            denies=denies,
            dn_t=dn_t,
            gold=gold,
            gold_per_min=gold_per_min,
            gold_reasons=gold_reasons,
            gold_spent=gold_spent,
            gold_t=gold_t,
            hero_damage=hero_damage,
            hero_healing=hero_healing,
            hero_hits=hero_hits,
            hero_id=hero_id,
            item_0=item_0,
            item_1=item_1,
            item_2=item_2,
            item_3=item_3,
            item_4=item_4,
            item_5=item_5,
            item_uses=item_uses,
            kill_streaks=kill_streaks,
            killed=killed,
            killed_by=killed_by,
            kills=kills,
            kills_log=kills_log,
            lane_pos=lane_pos,
            last_hits=last_hits,
            leaver_status=leaver_status,
            level=level,
            lh_t=lh_t,
            life_state=life_state,
            max_hero_hit=max_hero_hit,
            multi_kills=multi_kills,
            obs=obs,
            obs_left_log=obs_left_log,
            obs_log=obs_log,
            obs_placed=obs_placed,
            party_id=party_id,
            permanent_buffs=permanent_buffs,
            pings=pings,
            purchase=purchase,
            purchase_log=purchase_log,
            rune_pickups=rune_pickups,
            runes=runes,
            runes_log=runes_log,
            sen=sen,
            sen_left_log=sen_left_log,
            sen_log=sen_log,
            sen_placed=sen_placed,
            stuns=stuns,
            times=times,
            tower_damage=tower_damage,
            xp_per_min=xp_per_min,
            xp_reasons=xp_reasons,
            xp_t=xp_t,
            personaname=personaname,
            name=name,
            last_login=last_login,
            radiant_win=radiant_win,
            start_time=start_time,
            duration=duration,
            cluster=cluster,
            lobby_type=lobby_type,
            game_mode=game_mode,
            patch=patch,
            region=region,
            is_radiant=is_radiant,
            win=win,
            lose=lose,
            total_gold=total_gold,
            total_xp=total_xp,
            kills_per_min=kills_per_min,
            kda=kda,
            abandons=abandons,
            neutral_kills=neutral_kills,
            tower_kills=tower_kills,
            courier_kills=courier_kills,
            lane_kills=lane_kills,
            hero_kills=hero_kills,
            observer_kills=observer_kills,
            sentry_kills=sentry_kills,
            roshan_kills=roshan_kills,
            necronomicon_kills=necronomicon_kills,
            ancient_kills=ancient_kills,
            buyback_count=buyback_count,
            observer_uses=observer_uses,
            sentry_uses=sentry_uses,
            lane_efficiency=lane_efficiency,
            lane_efficiency_pct=lane_efficiency_pct,
            lane=lane,
            lane_role=lane_role,
            is_roaming=is_roaming,
            purchase_time=purchase_time,
            first_purchase_time=first_purchase_time,
            item_win=item_win,
            item_usage=item_usage,
            purchase_tpscroll=purchase_tpscroll,
            actions_per_min=actions_per_min,
            life_state_dead=life_state_dead,
            rank_tier=rank_tier,
            cosmetics=cosmetics,
            benchmarks=benchmarks,
        )

        match_response_players_item.additional_properties = d
        return match_response_players_item

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
