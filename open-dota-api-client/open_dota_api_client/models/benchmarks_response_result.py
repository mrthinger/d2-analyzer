from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.benchmarks_response_result_gold_per_min_item import BenchmarksResponseResultGoldPerMinItem
    from ..models.benchmarks_response_result_hero_damage_per_min_item import (
        BenchmarksResponseResultHeroDamagePerMinItem,
    )
    from ..models.benchmarks_response_result_hero_healing_per_min_item import (
        BenchmarksResponseResultHeroHealingPerMinItem,
    )
    from ..models.benchmarks_response_result_kills_per_min_item import BenchmarksResponseResultKillsPerMinItem
    from ..models.benchmarks_response_result_last_hits_per_min_item import BenchmarksResponseResultLastHitsPerMinItem
    from ..models.benchmarks_response_result_tower_damage_item import BenchmarksResponseResultTowerDamageItem
    from ..models.benchmarks_response_result_xp_per_min_item import BenchmarksResponseResultXpPerMinItem


T = TypeVar("T", bound="BenchmarksResponseResult")


@_attrs_define
class BenchmarksResponseResult:
    """result

    Attributes:
        gold_per_min (Union[Unset, List['BenchmarksResponseResultGoldPerMinItem']]):
        xp_per_min (Union[Unset, List['BenchmarksResponseResultXpPerMinItem']]):
        kills_per_min (Union[Unset, List['BenchmarksResponseResultKillsPerMinItem']]):
        last_hits_per_min (Union[Unset, List['BenchmarksResponseResultLastHitsPerMinItem']]):
        hero_damage_per_min (Union[Unset, List['BenchmarksResponseResultHeroDamagePerMinItem']]):
        hero_healing_per_min (Union[Unset, List['BenchmarksResponseResultHeroHealingPerMinItem']]):
        tower_damage (Union[Unset, List['BenchmarksResponseResultTowerDamageItem']]):
    """

    gold_per_min: Union[Unset, List["BenchmarksResponseResultGoldPerMinItem"]] = UNSET
    xp_per_min: Union[Unset, List["BenchmarksResponseResultXpPerMinItem"]] = UNSET
    kills_per_min: Union[Unset, List["BenchmarksResponseResultKillsPerMinItem"]] = UNSET
    last_hits_per_min: Union[Unset, List["BenchmarksResponseResultLastHitsPerMinItem"]] = UNSET
    hero_damage_per_min: Union[Unset, List["BenchmarksResponseResultHeroDamagePerMinItem"]] = UNSET
    hero_healing_per_min: Union[Unset, List["BenchmarksResponseResultHeroHealingPerMinItem"]] = UNSET
    tower_damage: Union[Unset, List["BenchmarksResponseResultTowerDamageItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gold_per_min: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.gold_per_min, Unset):
            gold_per_min = []
            for gold_per_min_item_data in self.gold_per_min:
                gold_per_min_item = gold_per_min_item_data.to_dict()

                gold_per_min.append(gold_per_min_item)

        xp_per_min: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.xp_per_min, Unset):
            xp_per_min = []
            for xp_per_min_item_data in self.xp_per_min:
                xp_per_min_item = xp_per_min_item_data.to_dict()

                xp_per_min.append(xp_per_min_item)

        kills_per_min: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.kills_per_min, Unset):
            kills_per_min = []
            for kills_per_min_item_data in self.kills_per_min:
                kills_per_min_item = kills_per_min_item_data.to_dict()

                kills_per_min.append(kills_per_min_item)

        last_hits_per_min: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.last_hits_per_min, Unset):
            last_hits_per_min = []
            for last_hits_per_min_item_data in self.last_hits_per_min:
                last_hits_per_min_item = last_hits_per_min_item_data.to_dict()

                last_hits_per_min.append(last_hits_per_min_item)

        hero_damage_per_min: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hero_damage_per_min, Unset):
            hero_damage_per_min = []
            for hero_damage_per_min_item_data in self.hero_damage_per_min:
                hero_damage_per_min_item = hero_damage_per_min_item_data.to_dict()

                hero_damage_per_min.append(hero_damage_per_min_item)

        hero_healing_per_min: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hero_healing_per_min, Unset):
            hero_healing_per_min = []
            for hero_healing_per_min_item_data in self.hero_healing_per_min:
                hero_healing_per_min_item = hero_healing_per_min_item_data.to_dict()

                hero_healing_per_min.append(hero_healing_per_min_item)

        tower_damage: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tower_damage, Unset):
            tower_damage = []
            for tower_damage_item_data in self.tower_damage:
                tower_damage_item = tower_damage_item_data.to_dict()

                tower_damage.append(tower_damage_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gold_per_min is not UNSET:
            field_dict["gold_per_min"] = gold_per_min
        if xp_per_min is not UNSET:
            field_dict["xp_per_min"] = xp_per_min
        if kills_per_min is not UNSET:
            field_dict["kills_per_min"] = kills_per_min
        if last_hits_per_min is not UNSET:
            field_dict["last_hits_per_min"] = last_hits_per_min
        if hero_damage_per_min is not UNSET:
            field_dict["hero_damage_per_min"] = hero_damage_per_min
        if hero_healing_per_min is not UNSET:
            field_dict["hero_healing_per_min"] = hero_healing_per_min
        if tower_damage is not UNSET:
            field_dict["tower_damage"] = tower_damage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.benchmarks_response_result_gold_per_min_item import BenchmarksResponseResultGoldPerMinItem
        from ..models.benchmarks_response_result_hero_damage_per_min_item import (
            BenchmarksResponseResultHeroDamagePerMinItem,
        )
        from ..models.benchmarks_response_result_hero_healing_per_min_item import (
            BenchmarksResponseResultHeroHealingPerMinItem,
        )
        from ..models.benchmarks_response_result_kills_per_min_item import BenchmarksResponseResultKillsPerMinItem
        from ..models.benchmarks_response_result_last_hits_per_min_item import (
            BenchmarksResponseResultLastHitsPerMinItem,
        )
        from ..models.benchmarks_response_result_tower_damage_item import BenchmarksResponseResultTowerDamageItem
        from ..models.benchmarks_response_result_xp_per_min_item import BenchmarksResponseResultXpPerMinItem

        d = src_dict.copy()
        gold_per_min = []
        _gold_per_min = d.pop("gold_per_min", UNSET)
        for gold_per_min_item_data in _gold_per_min or []:
            gold_per_min_item = BenchmarksResponseResultGoldPerMinItem.from_dict(gold_per_min_item_data)

            gold_per_min.append(gold_per_min_item)

        xp_per_min = []
        _xp_per_min = d.pop("xp_per_min", UNSET)
        for xp_per_min_item_data in _xp_per_min or []:
            xp_per_min_item = BenchmarksResponseResultXpPerMinItem.from_dict(xp_per_min_item_data)

            xp_per_min.append(xp_per_min_item)

        kills_per_min = []
        _kills_per_min = d.pop("kills_per_min", UNSET)
        for kills_per_min_item_data in _kills_per_min or []:
            kills_per_min_item = BenchmarksResponseResultKillsPerMinItem.from_dict(kills_per_min_item_data)

            kills_per_min.append(kills_per_min_item)

        last_hits_per_min = []
        _last_hits_per_min = d.pop("last_hits_per_min", UNSET)
        for last_hits_per_min_item_data in _last_hits_per_min or []:
            last_hits_per_min_item = BenchmarksResponseResultLastHitsPerMinItem.from_dict(last_hits_per_min_item_data)

            last_hits_per_min.append(last_hits_per_min_item)

        hero_damage_per_min = []
        _hero_damage_per_min = d.pop("hero_damage_per_min", UNSET)
        for hero_damage_per_min_item_data in _hero_damage_per_min or []:
            hero_damage_per_min_item = BenchmarksResponseResultHeroDamagePerMinItem.from_dict(
                hero_damage_per_min_item_data
            )

            hero_damage_per_min.append(hero_damage_per_min_item)

        hero_healing_per_min = []
        _hero_healing_per_min = d.pop("hero_healing_per_min", UNSET)
        for hero_healing_per_min_item_data in _hero_healing_per_min or []:
            hero_healing_per_min_item = BenchmarksResponseResultHeroHealingPerMinItem.from_dict(
                hero_healing_per_min_item_data
            )

            hero_healing_per_min.append(hero_healing_per_min_item)

        tower_damage = []
        _tower_damage = d.pop("tower_damage", UNSET)
        for tower_damage_item_data in _tower_damage or []:
            tower_damage_item = BenchmarksResponseResultTowerDamageItem.from_dict(tower_damage_item_data)

            tower_damage.append(tower_damage_item)

        benchmarks_response_result = cls(
            gold_per_min=gold_per_min,
            xp_per_min=xp_per_min,
            kills_per_min=kills_per_min,
            last_hits_per_min=last_hits_per_min,
            hero_damage_per_min=hero_damage_per_min,
            hero_healing_per_min=hero_healing_per_min,
            tower_damage=tower_damage,
        )

        benchmarks_response_result.additional_properties = d
        return benchmarks_response_result

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
