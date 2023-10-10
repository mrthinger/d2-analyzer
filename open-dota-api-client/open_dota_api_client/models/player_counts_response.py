from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_counts_response_game_mode import PlayerCountsResponseGameMode
    from ..models.player_counts_response_lane_role import PlayerCountsResponseLaneRole
    from ..models.player_counts_response_leaver_status import PlayerCountsResponseLeaverStatus
    from ..models.player_counts_response_lobby_type import PlayerCountsResponseLobbyType
    from ..models.player_counts_response_patch import PlayerCountsResponsePatch
    from ..models.player_counts_response_region import PlayerCountsResponseRegion


T = TypeVar("T", bound="PlayerCountsResponse")


@_attrs_define
class PlayerCountsResponse:
    """
    Attributes:
        leaver_status (Union[Unset, PlayerCountsResponseLeaverStatus]): Integer describing whether or not the player
            left the game. 0: didn't leave. 1: left safely. 2+: Abandoned
        game_mode (Union[Unset, PlayerCountsResponseGameMode]): Integer corresponding to game mode played. List of
            constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/game_mode.json
        lobby_type (Union[Unset, PlayerCountsResponseLobbyType]): Integer corresponding to lobby type of match. List of
            constants can be found here: https://github.com/odota/dotaconstants/blob/master/json/lobby_type.json
        lane_role (Union[Unset, PlayerCountsResponseLaneRole]): lane_role
        region (Union[Unset, PlayerCountsResponseRegion]): Integer corresponding to the region the game was played on
        patch (Union[Unset, PlayerCountsResponsePatch]): patch
    """

    leaver_status: Union[Unset, "PlayerCountsResponseLeaverStatus"] = UNSET
    game_mode: Union[Unset, "PlayerCountsResponseGameMode"] = UNSET
    lobby_type: Union[Unset, "PlayerCountsResponseLobbyType"] = UNSET
    lane_role: Union[Unset, "PlayerCountsResponseLaneRole"] = UNSET
    region: Union[Unset, "PlayerCountsResponseRegion"] = UNSET
    patch: Union[Unset, "PlayerCountsResponsePatch"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        leaver_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leaver_status, Unset):
            leaver_status = self.leaver_status.to_dict()

        game_mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.game_mode, Unset):
            game_mode = self.game_mode.to_dict()

        lobby_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lobby_type, Unset):
            lobby_type = self.lobby_type.to_dict()

        lane_role: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lane_role, Unset):
            lane_role = self.lane_role.to_dict()

        region: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        patch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patch, Unset):
            patch = self.patch.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if leaver_status is not UNSET:
            field_dict["leaver_status"] = leaver_status
        if game_mode is not UNSET:
            field_dict["game_mode"] = game_mode
        if lobby_type is not UNSET:
            field_dict["lobby_type"] = lobby_type
        if lane_role is not UNSET:
            field_dict["lane_role"] = lane_role
        if region is not UNSET:
            field_dict["region"] = region
        if patch is not UNSET:
            field_dict["patch"] = patch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player_counts_response_game_mode import PlayerCountsResponseGameMode
        from ..models.player_counts_response_lane_role import PlayerCountsResponseLaneRole
        from ..models.player_counts_response_leaver_status import PlayerCountsResponseLeaverStatus
        from ..models.player_counts_response_lobby_type import PlayerCountsResponseLobbyType
        from ..models.player_counts_response_patch import PlayerCountsResponsePatch
        from ..models.player_counts_response_region import PlayerCountsResponseRegion

        d = src_dict.copy()
        _leaver_status = d.pop("leaver_status", UNSET)
        leaver_status: Union[Unset, PlayerCountsResponseLeaverStatus]
        if isinstance(_leaver_status, Unset):
            leaver_status = UNSET
        else:
            leaver_status = PlayerCountsResponseLeaverStatus.from_dict(_leaver_status)

        _game_mode = d.pop("game_mode", UNSET)
        game_mode: Union[Unset, PlayerCountsResponseGameMode]
        if isinstance(_game_mode, Unset):
            game_mode = UNSET
        else:
            game_mode = PlayerCountsResponseGameMode.from_dict(_game_mode)

        _lobby_type = d.pop("lobby_type", UNSET)
        lobby_type: Union[Unset, PlayerCountsResponseLobbyType]
        if isinstance(_lobby_type, Unset):
            lobby_type = UNSET
        else:
            lobby_type = PlayerCountsResponseLobbyType.from_dict(_lobby_type)

        _lane_role = d.pop("lane_role", UNSET)
        lane_role: Union[Unset, PlayerCountsResponseLaneRole]
        if isinstance(_lane_role, Unset):
            lane_role = UNSET
        else:
            lane_role = PlayerCountsResponseLaneRole.from_dict(_lane_role)

        _region = d.pop("region", UNSET)
        region: Union[Unset, PlayerCountsResponseRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = PlayerCountsResponseRegion.from_dict(_region)

        _patch = d.pop("patch", UNSET)
        patch: Union[Unset, PlayerCountsResponsePatch]
        if isinstance(_patch, Unset):
            patch = UNSET
        else:
            patch = PlayerCountsResponsePatch.from_dict(_patch)

        player_counts_response = cls(
            leaver_status=leaver_status,
            game_mode=game_mode,
            lobby_type=lobby_type,
            lane_role=lane_role,
            region=region,
            patch=patch,
        )

        player_counts_response.additional_properties = d
        return player_counts_response

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
