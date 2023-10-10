from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.team_object_response import TeamObjectResponse
from ...types import Response


def _get_kwargs(
    league_id: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/leagues/{league_id}/teams".format(
            league_id=league_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TeamObjectResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TeamObjectResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TeamObjectResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    league_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[TeamObjectResponse]:
    """GET /leagues/{league_id}/teams

     Get teams for a league

    Args:
        league_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamObjectResponse]
    """

    kwargs = _get_kwargs(
        league_id=league_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    league_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[TeamObjectResponse]:
    """GET /leagues/{league_id}/teams

     Get teams for a league

    Args:
        league_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamObjectResponse
    """

    return sync_detailed(
        league_id=league_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    league_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[TeamObjectResponse]:
    """GET /leagues/{league_id}/teams

     Get teams for a league

    Args:
        league_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamObjectResponse]
    """

    kwargs = _get_kwargs(
        league_id=league_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    league_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[TeamObjectResponse]:
    """GET /leagues/{league_id}/teams

     Get teams for a league

    Args:
        league_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamObjectResponse
    """

    return (
        await asyncio_detailed(
            league_id=league_id,
            client=client,
        )
    ).parsed
