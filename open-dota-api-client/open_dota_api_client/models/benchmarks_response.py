from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.benchmarks_response_result import BenchmarksResponseResult


T = TypeVar("T", bound="BenchmarksResponse")


@_attrs_define
class BenchmarksResponse:
    """
    Attributes:
        hero_id (Union[Unset, int]): The ID value of the hero played
        result (Union[Unset, BenchmarksResponseResult]): result
    """

    hero_id: Union[Unset, int] = UNSET
    result: Union[Unset, "BenchmarksResponseResult"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hero_id = self.hero_id
        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hero_id is not UNSET:
            field_dict["hero_id"] = hero_id
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.benchmarks_response_result import BenchmarksResponseResult

        d = src_dict.copy()
        hero_id = d.pop("hero_id", UNSET)

        _result = d.pop("result", UNSET)
        result: Union[Unset, BenchmarksResponseResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = BenchmarksResponseResult.from_dict(_result)

        benchmarks_response = cls(
            hero_id=hero_id,
            result=result,
        )

        benchmarks_response.additional_properties = d
        return benchmarks_response

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
