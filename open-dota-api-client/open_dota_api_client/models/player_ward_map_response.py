from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_ward_map_response_obs import PlayerWardMapResponseObs
    from ..models.player_ward_map_response_sen import PlayerWardMapResponseSen


T = TypeVar("T", bound="PlayerWardMapResponse")


@_attrs_define
class PlayerWardMapResponse:
    """
    Attributes:
        obs (Union[Unset, PlayerWardMapResponseObs]): obs
        sen (Union[Unset, PlayerWardMapResponseSen]): sen
    """

    obs: Union[Unset, "PlayerWardMapResponseObs"] = UNSET
    sen: Union[Unset, "PlayerWardMapResponseSen"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        obs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.obs, Unset):
            obs = self.obs.to_dict()

        sen: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sen, Unset):
            sen = self.sen.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if obs is not UNSET:
            field_dict["obs"] = obs
        if sen is not UNSET:
            field_dict["sen"] = sen

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player_ward_map_response_obs import PlayerWardMapResponseObs
        from ..models.player_ward_map_response_sen import PlayerWardMapResponseSen

        d = src_dict.copy()
        _obs = d.pop("obs", UNSET)
        obs: Union[Unset, PlayerWardMapResponseObs]
        if isinstance(_obs, Unset):
            obs = UNSET
        else:
            obs = PlayerWardMapResponseObs.from_dict(_obs)

        _sen = d.pop("sen", UNSET)
        sen: Union[Unset, PlayerWardMapResponseSen]
        if isinstance(_sen, Unset):
            sen = UNSET
        else:
            sen = PlayerWardMapResponseSen.from_dict(_sen)

        player_ward_map_response = cls(
            obs=obs,
            sen=sen,
        )

        player_ward_map_response.additional_properties = d
        return player_ward_map_response

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
