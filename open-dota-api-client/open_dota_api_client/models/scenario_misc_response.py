from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScenarioMiscResponse")


@_attrs_define
class ScenarioMiscResponse:
    """
    Attributes:
        scenario (Union[Unset, str]): The scenario's name or description
        is_radiant (Union[Unset, bool]): Boolean indicating whether Radiant executed this scenario
        region (Union[Unset, int]): Region the game was played in
        games (Union[Unset, str]): The number of games where this scenario occurred
        wins (Union[Unset, str]): The number of games won where this scenario occured
    """

    scenario: Union[Unset, str] = UNSET
    is_radiant: Union[Unset, bool] = UNSET
    region: Union[Unset, int] = UNSET
    games: Union[Unset, str] = UNSET
    wins: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scenario = self.scenario
        is_radiant = self.is_radiant
        region = self.region
        games = self.games
        wins = self.wins

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scenario is not UNSET:
            field_dict["scenario"] = scenario
        if is_radiant is not UNSET:
            field_dict["is_radiant"] = is_radiant
        if region is not UNSET:
            field_dict["region"] = region
        if games is not UNSET:
            field_dict["games"] = games
        if wins is not UNSET:
            field_dict["wins"] = wins

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scenario = d.pop("scenario", UNSET)

        is_radiant = d.pop("is_radiant", UNSET)

        region = d.pop("region", UNSET)

        games = d.pop("games", UNSET)

        wins = d.pop("wins", UNSET)

        scenario_misc_response = cls(
            scenario=scenario,
            is_radiant=is_radiant,
            region=region,
            games=games,
            wins=wins,
        )

        scenario_misc_response.additional_properties = d
        return scenario_misc_response

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
