from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DistributionsResponseMmrFieldsItem")


@_attrs_define
class DistributionsResponseMmrFieldsItem:
    """
    Attributes:
        name (Union[Unset, str]): Field name
        table_id (Union[Unset, int]): tableID
        column_id (Union[Unset, int]): columnID
        data_type_id (Union[Unset, int]): dataTypeID
        data_type_size (Union[Unset, int]): dataTypeSize
        data_type_modifier (Union[Unset, int]): dataTypeModifier
        format_ (Union[Unset, str]): format
    """

    name: Union[Unset, str] = UNSET
    table_id: Union[Unset, int] = UNSET
    column_id: Union[Unset, int] = UNSET
    data_type_id: Union[Unset, int] = UNSET
    data_type_size: Union[Unset, int] = UNSET
    data_type_modifier: Union[Unset, int] = UNSET
    format_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        table_id = self.table_id
        column_id = self.column_id
        data_type_id = self.data_type_id
        data_type_size = self.data_type_size
        data_type_modifier = self.data_type_modifier
        format_ = self.format_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if table_id is not UNSET:
            field_dict["tableID"] = table_id
        if column_id is not UNSET:
            field_dict["columnID"] = column_id
        if data_type_id is not UNSET:
            field_dict["dataTypeID"] = data_type_id
        if data_type_size is not UNSET:
            field_dict["dataTypeSize"] = data_type_size
        if data_type_modifier is not UNSET:
            field_dict["dataTypeModifier"] = data_type_modifier
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        table_id = d.pop("tableID", UNSET)

        column_id = d.pop("columnID", UNSET)

        data_type_id = d.pop("dataTypeID", UNSET)

        data_type_size = d.pop("dataTypeSize", UNSET)

        data_type_modifier = d.pop("dataTypeModifier", UNSET)

        format_ = d.pop("format", UNSET)

        distributions_response_mmr_fields_item = cls(
            name=name,
            table_id=table_id,
            column_id=column_id,
            data_type_id=data_type_id,
            data_type_size=data_type_size,
            data_type_modifier=data_type_modifier,
            format_=format_,
        )

        distributions_response_mmr_fields_item.additional_properties = d
        return distributions_response_mmr_fields_item

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
