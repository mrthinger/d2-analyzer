from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeroStatsResponse")


@_attrs_define
class HeroStatsResponse:
    """
    Attributes:
        id (Union[Unset, int]): The ID value of the hero played
        name (Union[Unset, str]): Dota hero command name Example: npc_dota_hero_antimage.
        localized_name (Union[Unset, str]): Hero name Example: Anti-Mage.
        primary_attr (Union[Unset, str]): primary_attr
        attack_type (Union[Unset, str]): attack_type
        roles (Union[Unset, List[str]]): roles
        img (Union[Unset, str]): img
        icon (Union[Unset, str]): icon
        base_health (Union[Unset, int]): base_health
        base_health_regen (Union[Unset, float]): base_health_regen
        base_mana (Union[Unset, int]): base_mana
        base_mana_regen (Union[Unset, int]): base_mana_regen
        base_armor (Union[Unset, int]): base_armor
        base_mr (Union[Unset, int]): base_mr
        base_attack_min (Union[Unset, int]): base_attack_min
        base_attack_max (Union[Unset, int]): base_attack_max
        base_str (Union[Unset, int]): base_str
        base_agi (Union[Unset, int]): base_agi
        base_int (Union[Unset, int]): base_int
        str_gain (Union[Unset, float]): str_gain
        agi_gain (Union[Unset, float]): agi_gain
        int_gain (Union[Unset, float]): int_gain
        attack_range (Union[Unset, int]): attack_range
        projectile_speed (Union[Unset, int]): projectile_speed
        attack_rate (Union[Unset, float]): attack_rate
        base_attack_time (Union[Unset, int]): base_attack_time
        attack_point (Union[Unset, float]): attack_point
        move_speed (Union[Unset, int]): move_speed
        turn_rate (Union[Unset, float]): turn_rate
        cm_enabled (Union[Unset, bool]): cm_enabled
        legs (Union[Unset, int]): legs
        day_vision (Union[Unset, int]): day_vision
        night_vision (Union[Unset, int]): night_vision
        hero_id (Union[Unset, int]): The ID value of the hero played
        turbo_picks (Union[Unset, int]): Picks in Turbo mode this month
        turbo_wins (Union[Unset, int]): Wins in Turbo mode this month
        pro_ban (Union[Unset, int]): pro_ban
        pro_win (Union[Unset, int]): pro_win
        pro_pick (Union[Unset, int]): pro_pick
        field_1_pick (Union[Unset, int]): Herald picks
        field_1_win (Union[Unset, int]): Herald wins
        field_2_pick (Union[Unset, int]): Guardian picks
        field_2_win (Union[Unset, int]): Guardian wins
        field_3_pick (Union[Unset, int]): Crusader picks
        field_3_win (Union[Unset, int]): Crusader wins
        field_4_pick (Union[Unset, int]): Archon picks
        field_4_win (Union[Unset, int]): Archon wins
        field_5_pick (Union[Unset, int]): Legend picks
        field_5_win (Union[Unset, int]): Legend wins
        field_6_pick (Union[Unset, int]): Ancient picks
        field_6_win (Union[Unset, int]): Ancient wins
        field_7_pick (Union[Unset, int]): Divine picks
        field_7_win (Union[Unset, int]): Divine wins
        field_8_pick (Union[Unset, int]): Immortal picks
        field_8_win (Union[Unset, int]): Immortal wins
        null_pick (Union[Unset, int]): null_pick
        null_win (Union[Unset, int]): null_win
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    localized_name: Union[Unset, str] = UNSET
    primary_attr: Union[Unset, str] = UNSET
    attack_type: Union[Unset, str] = UNSET
    roles: Union[Unset, List[str]] = UNSET
    img: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    base_health: Union[Unset, int] = UNSET
    base_health_regen: Union[Unset, float] = UNSET
    base_mana: Union[Unset, int] = UNSET
    base_mana_regen: Union[Unset, int] = UNSET
    base_armor: Union[Unset, int] = UNSET
    base_mr: Union[Unset, int] = UNSET
    base_attack_min: Union[Unset, int] = UNSET
    base_attack_max: Union[Unset, int] = UNSET
    base_str: Union[Unset, int] = UNSET
    base_agi: Union[Unset, int] = UNSET
    base_int: Union[Unset, int] = UNSET
    str_gain: Union[Unset, float] = UNSET
    agi_gain: Union[Unset, float] = UNSET
    int_gain: Union[Unset, float] = UNSET
    attack_range: Union[Unset, int] = UNSET
    projectile_speed: Union[Unset, int] = UNSET
    attack_rate: Union[Unset, float] = UNSET
    base_attack_time: Union[Unset, int] = UNSET
    attack_point: Union[Unset, float] = UNSET
    move_speed: Union[Unset, int] = UNSET
    turn_rate: Union[Unset, float] = UNSET
    cm_enabled: Union[Unset, bool] = UNSET
    legs: Union[Unset, int] = UNSET
    day_vision: Union[Unset, int] = UNSET
    night_vision: Union[Unset, int] = UNSET
    hero_id: Union[Unset, int] = UNSET
    turbo_picks: Union[Unset, int] = UNSET
    turbo_wins: Union[Unset, int] = UNSET
    pro_ban: Union[Unset, int] = UNSET
    pro_win: Union[Unset, int] = UNSET
    pro_pick: Union[Unset, int] = UNSET
    field_1_pick: Union[Unset, int] = UNSET
    field_1_win: Union[Unset, int] = UNSET
    field_2_pick: Union[Unset, int] = UNSET
    field_2_win: Union[Unset, int] = UNSET
    field_3_pick: Union[Unset, int] = UNSET
    field_3_win: Union[Unset, int] = UNSET
    field_4_pick: Union[Unset, int] = UNSET
    field_4_win: Union[Unset, int] = UNSET
    field_5_pick: Union[Unset, int] = UNSET
    field_5_win: Union[Unset, int] = UNSET
    field_6_pick: Union[Unset, int] = UNSET
    field_6_win: Union[Unset, int] = UNSET
    field_7_pick: Union[Unset, int] = UNSET
    field_7_win: Union[Unset, int] = UNSET
    field_8_pick: Union[Unset, int] = UNSET
    field_8_win: Union[Unset, int] = UNSET
    null_pick: Union[Unset, int] = UNSET
    null_win: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        localized_name = self.localized_name
        primary_attr = self.primary_attr
        attack_type = self.attack_type
        roles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        img = self.img
        icon = self.icon
        base_health = self.base_health
        base_health_regen = self.base_health_regen
        base_mana = self.base_mana
        base_mana_regen = self.base_mana_regen
        base_armor = self.base_armor
        base_mr = self.base_mr
        base_attack_min = self.base_attack_min
        base_attack_max = self.base_attack_max
        base_str = self.base_str
        base_agi = self.base_agi
        base_int = self.base_int
        str_gain = self.str_gain
        agi_gain = self.agi_gain
        int_gain = self.int_gain
        attack_range = self.attack_range
        projectile_speed = self.projectile_speed
        attack_rate = self.attack_rate
        base_attack_time = self.base_attack_time
        attack_point = self.attack_point
        move_speed = self.move_speed
        turn_rate = self.turn_rate
        cm_enabled = self.cm_enabled
        legs = self.legs
        day_vision = self.day_vision
        night_vision = self.night_vision
        hero_id = self.hero_id
        turbo_picks = self.turbo_picks
        turbo_wins = self.turbo_wins
        pro_ban = self.pro_ban
        pro_win = self.pro_win
        pro_pick = self.pro_pick
        field_1_pick = self.field_1_pick
        field_1_win = self.field_1_win
        field_2_pick = self.field_2_pick
        field_2_win = self.field_2_win
        field_3_pick = self.field_3_pick
        field_3_win = self.field_3_win
        field_4_pick = self.field_4_pick
        field_4_win = self.field_4_win
        field_5_pick = self.field_5_pick
        field_5_win = self.field_5_win
        field_6_pick = self.field_6_pick
        field_6_win = self.field_6_win
        field_7_pick = self.field_7_pick
        field_7_win = self.field_7_win
        field_8_pick = self.field_8_pick
        field_8_win = self.field_8_win
        null_pick = self.null_pick
        null_win = self.null_win

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if localized_name is not UNSET:
            field_dict["localized_name"] = localized_name
        if primary_attr is not UNSET:
            field_dict["primary_attr"] = primary_attr
        if attack_type is not UNSET:
            field_dict["attack_type"] = attack_type
        if roles is not UNSET:
            field_dict["roles"] = roles
        if img is not UNSET:
            field_dict["img"] = img
        if icon is not UNSET:
            field_dict["icon"] = icon
        if base_health is not UNSET:
            field_dict["base_health"] = base_health
        if base_health_regen is not UNSET:
            field_dict["base_health_regen"] = base_health_regen
        if base_mana is not UNSET:
            field_dict["base_mana"] = base_mana
        if base_mana_regen is not UNSET:
            field_dict["base_mana_regen"] = base_mana_regen
        if base_armor is not UNSET:
            field_dict["base_armor"] = base_armor
        if base_mr is not UNSET:
            field_dict["base_mr"] = base_mr
        if base_attack_min is not UNSET:
            field_dict["base_attack_min"] = base_attack_min
        if base_attack_max is not UNSET:
            field_dict["base_attack_max"] = base_attack_max
        if base_str is not UNSET:
            field_dict["base_str"] = base_str
        if base_agi is not UNSET:
            field_dict["base_agi"] = base_agi
        if base_int is not UNSET:
            field_dict["base_int"] = base_int
        if str_gain is not UNSET:
            field_dict["str_gain"] = str_gain
        if agi_gain is not UNSET:
            field_dict["agi_gain"] = agi_gain
        if int_gain is not UNSET:
            field_dict["int_gain"] = int_gain
        if attack_range is not UNSET:
            field_dict["attack_range"] = attack_range
        if projectile_speed is not UNSET:
            field_dict["projectile_speed"] = projectile_speed
        if attack_rate is not UNSET:
            field_dict["attack_rate"] = attack_rate
        if base_attack_time is not UNSET:
            field_dict["base_attack_time"] = base_attack_time
        if attack_point is not UNSET:
            field_dict["attack_point"] = attack_point
        if move_speed is not UNSET:
            field_dict["move_speed"] = move_speed
        if turn_rate is not UNSET:
            field_dict["turn_rate"] = turn_rate
        if cm_enabled is not UNSET:
            field_dict["cm_enabled"] = cm_enabled
        if legs is not UNSET:
            field_dict["legs"] = legs
        if day_vision is not UNSET:
            field_dict["day_vision"] = day_vision
        if night_vision is not UNSET:
            field_dict["night_vision"] = night_vision
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if turbo_picks is not UNSET:
            field_dict["turbo_picks"] = turbo_picks
        if turbo_wins is not UNSET:
            field_dict["turbo_wins"] = turbo_wins
        if pro_ban is not UNSET:
            field_dict["pro_ban"] = pro_ban
        if pro_win is not UNSET:
            field_dict["pro_win"] = pro_win
        if pro_pick is not UNSET:
            field_dict["pro_pick"] = pro_pick
        if field_1_pick is not UNSET:
            field_dict["1_pick"] = field_1_pick
        if field_1_win is not UNSET:
            field_dict["1_win"] = field_1_win
        if field_2_pick is not UNSET:
            field_dict["2_pick"] = field_2_pick
        if field_2_win is not UNSET:
            field_dict["2_win"] = field_2_win
        if field_3_pick is not UNSET:
            field_dict["3_pick"] = field_3_pick
        if field_3_win is not UNSET:
            field_dict["3_win"] = field_3_win
        if field_4_pick is not UNSET:
            field_dict["4_pick"] = field_4_pick
        if field_4_win is not UNSET:
            field_dict["4_win"] = field_4_win
        if field_5_pick is not UNSET:
            field_dict["5_pick"] = field_5_pick
        if field_5_win is not UNSET:
            field_dict["5_win"] = field_5_win
        if field_6_pick is not UNSET:
            field_dict["6_pick"] = field_6_pick
        if field_6_win is not UNSET:
            field_dict["6_win"] = field_6_win
        if field_7_pick is not UNSET:
            field_dict["7_pick"] = field_7_pick
        if field_7_win is not UNSET:
            field_dict["7_win"] = field_7_win
        if field_8_pick is not UNSET:
            field_dict["8_pick"] = field_8_pick
        if field_8_win is not UNSET:
            field_dict["8_win"] = field_8_win
        if null_pick is not UNSET:
            field_dict["null_pick"] = null_pick
        if null_win is not UNSET:
            field_dict["null_win"] = null_win

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        localized_name = d.pop("localized_name", UNSET)

        primary_attr = d.pop("primary_attr", UNSET)

        attack_type = d.pop("attack_type", UNSET)

        roles = cast(List[str], d.pop("roles", UNSET))

        img = d.pop("img", UNSET)

        icon = d.pop("icon", UNSET)

        base_health = d.pop("base_health", UNSET)

        base_health_regen = d.pop("base_health_regen", UNSET)

        base_mana = d.pop("base_mana", UNSET)

        base_mana_regen = d.pop("base_mana_regen", UNSET)

        base_armor = d.pop("base_armor", UNSET)

        base_mr = d.pop("base_mr", UNSET)

        base_attack_min = d.pop("base_attack_min", UNSET)

        base_attack_max = d.pop("base_attack_max", UNSET)

        base_str = d.pop("base_str", UNSET)

        base_agi = d.pop("base_agi", UNSET)

        base_int = d.pop("base_int", UNSET)

        str_gain = d.pop("str_gain", UNSET)

        agi_gain = d.pop("agi_gain", UNSET)

        int_gain = d.pop("int_gain", UNSET)

        attack_range = d.pop("attack_range", UNSET)

        projectile_speed = d.pop("projectile_speed", UNSET)

        attack_rate = d.pop("attack_rate", UNSET)

        base_attack_time = d.pop("base_attack_time", UNSET)

        attack_point = d.pop("attack_point", UNSET)

        move_speed = d.pop("move_speed", UNSET)

        turn_rate = d.pop("turn_rate", UNSET)

        cm_enabled = d.pop("cm_enabled", UNSET)

        legs = d.pop("legs", UNSET)

        day_vision = d.pop("day_vision", UNSET)

        night_vision = d.pop("night_vision", UNSET)

        hero_id = d.pop("hero_id", UNSET)

        turbo_picks = d.pop("turbo_picks", UNSET)

        turbo_wins = d.pop("turbo_wins", UNSET)

        pro_ban = d.pop("pro_ban", UNSET)

        pro_win = d.pop("pro_win", UNSET)

        pro_pick = d.pop("pro_pick", UNSET)

        field_1_pick = d.pop("1_pick", UNSET)

        field_1_win = d.pop("1_win", UNSET)

        field_2_pick = d.pop("2_pick", UNSET)

        field_2_win = d.pop("2_win", UNSET)

        field_3_pick = d.pop("3_pick", UNSET)

        field_3_win = d.pop("3_win", UNSET)

        field_4_pick = d.pop("4_pick", UNSET)

        field_4_win = d.pop("4_win", UNSET)

        field_5_pick = d.pop("5_pick", UNSET)

        field_5_win = d.pop("5_win", UNSET)

        field_6_pick = d.pop("6_pick", UNSET)

        field_6_win = d.pop("6_win", UNSET)

        field_7_pick = d.pop("7_pick", UNSET)

        field_7_win = d.pop("7_win", UNSET)

        field_8_pick = d.pop("8_pick", UNSET)

        field_8_win = d.pop("8_win", UNSET)

        null_pick = d.pop("null_pick", UNSET)

        null_win = d.pop("null_win", UNSET)

        hero_stats_response = cls(
            id=id,
            name=name,
            localized_name=localized_name,
            primary_attr=primary_attr,
            attack_type=attack_type,
            roles=roles,
            img=img,
            icon=icon,
            base_health=base_health,
            base_health_regen=base_health_regen,
            base_mana=base_mana,
            base_mana_regen=base_mana_regen,
            base_armor=base_armor,
            base_mr=base_mr,
            base_attack_min=base_attack_min,
            base_attack_max=base_attack_max,
            base_str=base_str,
            base_agi=base_agi,
            base_int=base_int,
            str_gain=str_gain,
            agi_gain=agi_gain,
            int_gain=int_gain,
            attack_range=attack_range,
            projectile_speed=projectile_speed,
            attack_rate=attack_rate,
            base_attack_time=base_attack_time,
            attack_point=attack_point,
            move_speed=move_speed,
            turn_rate=turn_rate,
            cm_enabled=cm_enabled,
            legs=legs,
            day_vision=day_vision,
            night_vision=night_vision,
            hero_id=hero_id,
            turbo_picks=turbo_picks,
            turbo_wins=turbo_wins,
            pro_ban=pro_ban,
            pro_win=pro_win,
            pro_pick=pro_pick,
            field_1_pick=field_1_pick,
            field_1_win=field_1_win,
            field_2_pick=field_2_pick,
            field_2_win=field_2_win,
            field_3_pick=field_3_pick,
            field_3_win=field_3_win,
            field_4_pick=field_4_pick,
            field_4_win=field_4_win,
            field_5_pick=field_5_pick,
            field_5_win=field_5_win,
            field_6_pick=field_6_pick,
            field_6_win=field_6_win,
            field_7_pick=field_7_pick,
            field_7_win=field_7_win,
            field_8_pick=field_8_pick,
            field_8_win=field_8_win,
            null_pick=null_pick,
            null_win=null_win,
        )

        hero_stats_response.additional_properties = d
        return hero_stats_response

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
