from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.distributions_response_country_mmr import DistributionsResponseCountryMmr
    from ..models.distributions_response_mmr import DistributionsResponseMmr
    from ..models.distributions_response_ranks import DistributionsResponseRanks


T = TypeVar("T", bound="DistributionsResponse")


@_attrs_define
class DistributionsResponse:
    """
    Attributes:
        ranks (Union[Unset, DistributionsResponseRanks]): ranks
        mmr (Union[Unset, DistributionsResponseMmr]): mmr
        country_mmr (Union[Unset, DistributionsResponseCountryMmr]): country_mmr
    """

    ranks: Union[Unset, "DistributionsResponseRanks"] = UNSET
    mmr: Union[Unset, "DistributionsResponseMmr"] = UNSET
    country_mmr: Union[Unset, "DistributionsResponseCountryMmr"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ranks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ranks, Unset):
            ranks = self.ranks.to_dict()

        mmr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mmr, Unset):
            mmr = self.mmr.to_dict()

        country_mmr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.country_mmr, Unset):
            country_mmr = self.country_mmr.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ranks is not UNSET:
            field_dict["ranks"] = ranks
        if mmr is not UNSET:
            field_dict["mmr"] = mmr
        if country_mmr is not UNSET:
            field_dict["country_mmr"] = country_mmr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.distributions_response_country_mmr import DistributionsResponseCountryMmr
        from ..models.distributions_response_mmr import DistributionsResponseMmr
        from ..models.distributions_response_ranks import DistributionsResponseRanks

        d = src_dict.copy()
        _ranks = d.pop("ranks", UNSET)
        ranks: Union[Unset, DistributionsResponseRanks]
        if isinstance(_ranks, Unset):
            ranks = UNSET
        else:
            ranks = DistributionsResponseRanks.from_dict(_ranks)

        _mmr = d.pop("mmr", UNSET)
        mmr: Union[Unset, DistributionsResponseMmr]
        if isinstance(_mmr, Unset):
            mmr = UNSET
        else:
            mmr = DistributionsResponseMmr.from_dict(_mmr)

        _country_mmr = d.pop("country_mmr", UNSET)
        country_mmr: Union[Unset, DistributionsResponseCountryMmr]
        if isinstance(_country_mmr, Unset):
            country_mmr = UNSET
        else:
            country_mmr = DistributionsResponseCountryMmr.from_dict(_country_mmr)

        distributions_response = cls(
            ranks=ranks,
            mmr=mmr,
            country_mmr=country_mmr,
        )

        distributions_response.additional_properties = d
        return distributions_response

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
