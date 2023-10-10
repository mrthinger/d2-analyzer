from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaResponse")


@_attrs_define
class SchemaResponse:
    """
    Attributes:
        table_name (Union[Unset, str]): table_name
        column_name (Union[Unset, str]): column_name
        data_type (Union[Unset, str]): data_type
    """

    table_name: Union[Unset, str] = UNSET
    column_name: Union[Unset, str] = UNSET
    data_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table_name = self.table_name
        column_name = self.column_name
        data_type = self.data_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if table_name is not UNSET:
            field_dict["table_name"] = table_name
        if column_name is not UNSET:
            field_dict["column_name"] = column_name
        if data_type is not UNSET:
            field_dict["data_type"] = data_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        table_name = d.pop("table_name", UNSET)

        column_name = d.pop("column_name", UNSET)

        data_type = d.pop("data_type", UNSET)

        schema_response = cls(
            table_name=table_name,
            column_name=column_name,
            data_type=data_type,
        )

        schema_response.additional_properties = d
        return schema_response

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
