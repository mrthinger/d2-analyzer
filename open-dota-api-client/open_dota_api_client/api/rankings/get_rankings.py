from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rankings_response import RankingsResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    hero_id: str,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["hero_id"] = hero_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/rankings",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RankingsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RankingsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RankingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    hero_id: str,
) -> Response[RankingsResponse]:
    """GET /rankings

     Top players by hero

    Args:
        hero_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RankingsResponse]
    """

    kwargs = _get_kwargs(
        hero_id=hero_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    hero_id: str,
) -> Optional[RankingsResponse]:
    """GET /rankings

     Top players by hero

    Args:
        hero_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RankingsResponse
    """

    return sync_detailed(
        client=client,
        hero_id=hero_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    hero_id: str,
) -> Response[RankingsResponse]:
    """GET /rankings

     Top players by hero

    Args:
        hero_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RankingsResponse]
    """

    kwargs = _get_kwargs(
        hero_id=hero_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    hero_id: str,
) -> Optional[RankingsResponse]:
    """GET /rankings

     Top players by hero

    Args:
        hero_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RankingsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            hero_id=hero_id,
        )
    ).parsed
