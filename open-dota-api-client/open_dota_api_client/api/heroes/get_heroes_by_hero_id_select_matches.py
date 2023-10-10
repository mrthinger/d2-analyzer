from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.match_object_response import MatchObjectResponse
from ...types import Response


def _get_kwargs(
    hero_id: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/heroes/{hero_id}/matches".format(
            hero_id=hero_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["MatchObjectResponse"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MatchObjectResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["MatchObjectResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["MatchObjectResponse"]]:
    """GET /heroes/{hero_id}/matches

     Get recent matches with a hero

    Args:
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['MatchObjectResponse']]
    """

    kwargs = _get_kwargs(
        hero_id=hero_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["MatchObjectResponse"]]:
    """GET /heroes/{hero_id}/matches

     Get recent matches with a hero

    Args:
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['MatchObjectResponse']
    """

    return sync_detailed(
        hero_id=hero_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["MatchObjectResponse"]]:
    """GET /heroes/{hero_id}/matches

     Get recent matches with a hero

    Args:
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['MatchObjectResponse']]
    """

    kwargs = _get_kwargs(
        hero_id=hero_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["MatchObjectResponse"]]:
    """GET /heroes/{hero_id}/matches

     Get recent matches with a hero

    Args:
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['MatchObjectResponse']
    """

    return (
        await asyncio_detailed(
            hero_id=hero_id,
            client=client,
        )
    ).parsed
