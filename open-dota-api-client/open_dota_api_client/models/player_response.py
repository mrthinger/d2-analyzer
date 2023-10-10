from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_response_mmr_estimate import PlayerResponseMmrEstimate
    from ..models.player_response_profile import PlayerResponseProfile


T = TypeVar("T", bound="PlayerResponse")


@_attrs_define
class PlayerResponse:
    """
    Attributes:
        solo_competitive_rank (Union[Unset, None, int]): solo_competitive_rank
        competitive_rank (Union[Unset, None, int]): competitive_rank
        rank_tier (Union[Unset, None, float]): rank_tier
        leaderboard_rank (Union[Unset, None, float]): leaderboard_rank
        mmr_estimate (Union[Unset, PlayerResponseMmrEstimate]): mmr_estimate
        profile (Union[Unset, PlayerResponseProfile]): profile
    """

    solo_competitive_rank: Union[Unset, None, int] = UNSET
    competitive_rank: Union[Unset, None, int] = UNSET
    rank_tier: Union[Unset, None, float] = UNSET
    leaderboard_rank: Union[Unset, None, float] = UNSET
    mmr_estimate: Union[Unset, "PlayerResponseMmrEstimate"] = UNSET
    profile: Union[Unset, "PlayerResponseProfile"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        solo_competitive_rank = self.solo_competitive_rank
        competitive_rank = self.competitive_rank
        rank_tier = self.rank_tier
        leaderboard_rank = self.leaderboard_rank
        mmr_estimate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mmr_estimate, Unset):
            mmr_estimate = self.mmr_estimate.to_dict()

        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if solo_competitive_rank is not UNSET:
            field_dict["solo_competitive_rank"] = solo_competitive_rank
        if competitive_rank is not UNSET:
            field_dict["competitive_rank"] = competitive_rank
        if rank_tier is not UNSET:
            field_dict["rank_tier"] = rank_tier
        if leaderboard_rank is not UNSET:
            field_dict["leaderboard_rank"] = leaderboard_rank
        if mmr_estimate is not UNSET:
            field_dict["mmr_estimate"] = mmr_estimate
        if profile is not UNSET:
            field_dict["profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player_response_mmr_estimate import PlayerResponseMmrEstimate
        from ..models.player_response_profile import PlayerResponseProfile

        d = src_dict.copy()
        solo_competitive_rank = d.pop("solo_competitive_rank", UNSET)

        competitive_rank = d.pop("competitive_rank", UNSET)

        rank_tier = d.pop("rank_tier", UNSET)

        leaderboard_rank = d.pop("leaderboard_rank", UNSET)

        _mmr_estimate = d.pop("mmr_estimate", UNSET)
        mmr_estimate: Union[Unset, PlayerResponseMmrEstimate]
        if isinstance(_mmr_estimate, Unset):
            mmr_estimate = UNSET
        else:
            mmr_estimate = PlayerResponseMmrEstimate.from_dict(_mmr_estimate)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, PlayerResponseProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = PlayerResponseProfile.from_dict(_profile)

        player_response = cls(
            solo_competitive_rank=solo_competitive_rank,
            competitive_rank=competitive_rank,
            rank_tier=rank_tier,
            leaderboard_rank=leaderboard_rank,
            mmr_estimate=mmr_estimate,
            profile=profile,
        )

        player_response.additional_properties = d
        return player_response

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
