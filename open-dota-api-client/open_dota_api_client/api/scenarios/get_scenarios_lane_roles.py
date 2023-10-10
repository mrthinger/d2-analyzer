from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.scenario_lane_roles_response import ScenarioLaneRolesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lane_role: Union[Unset, None, str] = UNSET,
    hero_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["lane_role"] = lane_role

    params["hero_id"] = hero_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/scenarios/laneRoles",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["ScenarioLaneRolesResponse"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ScenarioLaneRolesResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["ScenarioLaneRolesResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    lane_role: Union[Unset, None, str] = UNSET,
    hero_id: Union[Unset, None, int] = UNSET,
) -> Response[List["ScenarioLaneRolesResponse"]]:
    """GET /scenarios/laneRoles

     Win rates for heroes in certain lane roles

    Args:
        lane_role (Union[Unset, None, str]):
        hero_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ScenarioLaneRolesResponse']]
    """

    kwargs = _get_kwargs(
        lane_role=lane_role,
        hero_id=hero_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    lane_role: Union[Unset, None, str] = UNSET,
    hero_id: Union[Unset, None, int] = UNSET,
) -> Optional[List["ScenarioLaneRolesResponse"]]:
    """GET /scenarios/laneRoles

     Win rates for heroes in certain lane roles

    Args:
        lane_role (Union[Unset, None, str]):
        hero_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ScenarioLaneRolesResponse']
    """

    return sync_detailed(
        client=client,
        lane_role=lane_role,
        hero_id=hero_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    lane_role: Union[Unset, None, str] = UNSET,
    hero_id: Union[Unset, None, int] = UNSET,
) -> Response[List["ScenarioLaneRolesResponse"]]:
    """GET /scenarios/laneRoles

     Win rates for heroes in certain lane roles

    Args:
        lane_role (Union[Unset, None, str]):
        hero_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ScenarioLaneRolesResponse']]
    """

    kwargs = _get_kwargs(
        lane_role=lane_role,
        hero_id=hero_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    lane_role: Union[Unset, None, str] = UNSET,
    hero_id: Union[Unset, None, int] = UNSET,
) -> Optional[List["ScenarioLaneRolesResponse"]]:
    """GET /scenarios/laneRoles

     Win rates for heroes in certain lane roles

    Args:
        lane_role (Union[Unset, None, str]):
        hero_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ScenarioLaneRolesResponse']
    """

    return (
        await asyncio_detailed(
            client=client,
            lane_role=lane_role,
            hero_id=hero_id,
        )
    ).parsed
