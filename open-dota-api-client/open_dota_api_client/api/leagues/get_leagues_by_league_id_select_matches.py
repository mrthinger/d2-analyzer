from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.match_object_response import MatchObjectResponse
from ...types import Response


def _get_kwargs(
    league_id: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/leagues/{league_id}/matches".format(
            league_id=league_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MatchObjectResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MatchObjectResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MatchObjectResponse]:
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
) -> Response[MatchObjectResponse]:
    """GET /leagues/{league_id}/matches

     Get matches for a team

    Args:
        league_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MatchObjectResponse]
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
) -> Optional[MatchObjectResponse]:
    """GET /leagues/{league_id}/matches

     Get matches for a team

    Args:
        league_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MatchObjectResponse
    """

    return sync_detailed(
        league_id=league_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    league_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MatchObjectResponse]:
    """GET /leagues/{league_id}/matches

     Get matches for a team

    Args:
        league_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MatchObjectResponse]
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
) -> Optional[MatchObjectResponse]:
    """GET /leagues/{league_id}/matches

     Get matches for a team

    Args:
        league_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MatchObjectResponse
    """

    return (
        await asyncio_detailed(
            league_id=league_id,
            client=client,
        )
    ).parsed
