from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerWinLossResponse")


@_attrs_define
class PlayerWinLossResponse:
    """
    Attributes:
        win (Union[Unset, int]): Number of wins
        lose (Union[Unset, int]): Number of loses
    """

    win: Union[Unset, int] = UNSET
    lose: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        win = self.win
        lose = self.lose

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if win is not UNSET:
            field_dict["win"] = win
        if lose is not UNSET:
            field_dict["lose"] = lose

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        win = d.pop("win", UNSET)

        lose = d.pop("lose", UNSET)

        player_win_loss_response = cls(
            win=win,
            lose=lose,
        )

        player_win_loss_response.additional_properties = d
        return player_win_loss_response

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
