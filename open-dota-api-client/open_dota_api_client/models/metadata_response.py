from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_response_banner import MetadataResponseBanner


T = TypeVar("T", bound="MetadataResponse")


@_attrs_define
class MetadataResponse:
    """
    Attributes:
        banner (Union[Unset, None, MetadataResponseBanner]): banner
    """

    banner: Union[Unset, None, "MetadataResponseBanner"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        banner: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.banner, Unset):
            banner = self.banner.to_dict() if self.banner else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if banner is not UNSET:
            field_dict["banner"] = banner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metadata_response_banner import MetadataResponseBanner

        d = src_dict.copy()
        _banner = d.pop("banner", UNSET)
        banner: Union[Unset, None, MetadataResponseBanner]
        if _banner is None:
            banner = None
        elif isinstance(_banner, Unset):
            banner = UNSET
        else:
            banner = MetadataResponseBanner.from_dict(_banner)

        metadata_response = cls(
            banner=banner,
        )

        metadata_response.additional_properties = d
        return metadata_response

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
