from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_players_account_id_refresh_player_refresh_response import (
    PostPlayersAccountIdRefreshPlayerRefreshResponse,
)
from ...types import Response


def _get_kwargs(
    account_id: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/players/{account_id}/refresh".format(
            account_id=account_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostPlayersAccountIdRefreshPlayerRefreshResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostPlayersAccountIdRefreshPlayerRefreshResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostPlayersAccountIdRefreshPlayerRefreshResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PostPlayersAccountIdRefreshPlayerRefreshResponse]:
    """POST /players/{account_id}/refresh

     Refresh player match history

    Args:
        account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPlayersAccountIdRefreshPlayerRefreshResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PostPlayersAccountIdRefreshPlayerRefreshResponse]:
    """POST /players/{account_id}/refresh

     Refresh player match history

    Args:
        account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPlayersAccountIdRefreshPlayerRefreshResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PostPlayersAccountIdRefreshPlayerRefreshResponse]:
    """POST /players/{account_id}/refresh

     Refresh player match history

    Args:
        account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPlayersAccountIdRefreshPlayerRefreshResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PostPlayersAccountIdRefreshPlayerRefreshResponse]:
    """POST /players/{account_id}/refresh

     Refresh player match history

    Args:
        account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPlayersAccountIdRefreshPlayerRefreshResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
