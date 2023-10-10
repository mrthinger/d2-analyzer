from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.distributions_response_country_mmr_fields_item import DistributionsResponseCountryMmrFieldsItem
    from ..models.distributions_response_country_mmr_rows_item import DistributionsResponseCountryMmrRowsItem


T = TypeVar("T", bound="DistributionsResponseCountryMmr")


@_attrs_define
class DistributionsResponseCountryMmr:
    """country_mmr

    Attributes:
        commmand (Union[Unset, str]): command
        row_count (Union[Unset, int]): rowCount
        rows (Union[Unset, List['DistributionsResponseCountryMmrRowsItem']]): rows
        fields (Union[Unset, List['DistributionsResponseCountryMmrFieldsItem']]): fields
        row_as_array (Union[Unset, bool]): rowAsArray
    """

    commmand: Union[Unset, str] = UNSET
    row_count: Union[Unset, int] = UNSET
    rows: Union[Unset, List["DistributionsResponseCountryMmrRowsItem"]] = UNSET
    fields: Union[Unset, List["DistributionsResponseCountryMmrFieldsItem"]] = UNSET
    row_as_array: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commmand = self.commmand
        row_count = self.row_count
        rows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()

                rows.append(rows_item)

        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)

        row_as_array = self.row_as_array

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commmand is not UNSET:
            field_dict["commmand"] = commmand
        if row_count is not UNSET:
            field_dict["rowCount"] = row_count
        if rows is not UNSET:
            field_dict["rows"] = rows
        if fields is not UNSET:
            field_dict["fields"] = fields
        if row_as_array is not UNSET:
            field_dict["rowAsArray"] = row_as_array

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.distributions_response_country_mmr_fields_item import DistributionsResponseCountryMmrFieldsItem
        from ..models.distributions_response_country_mmr_rows_item import DistributionsResponseCountryMmrRowsItem

        d = src_dict.copy()
        commmand = d.pop("commmand", UNSET)

        row_count = d.pop("rowCount", UNSET)

        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = DistributionsResponseCountryMmrRowsItem.from_dict(rows_item_data)

            rows.append(rows_item)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = DistributionsResponseCountryMmrFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        row_as_array = d.pop("rowAsArray", UNSET)

        distributions_response_country_mmr = cls(
            commmand=commmand,
            row_count=row_count,
            rows=rows,
            fields=fields,
            row_as_array=row_as_array,
        )

        distributions_response_country_mmr.additional_properties = d
        return distributions_response_country_mmr

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
