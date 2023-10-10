from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hero_item_popularity_response import HeroItemPopularityResponse
from ...types import Response


def _get_kwargs(
    hero_id: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/heroes/{hero_id}/itemPopularity".format(
            hero_id=hero_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[HeroItemPopularityResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = HeroItemPopularityResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[HeroItemPopularityResponse]:
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
) -> Response[HeroItemPopularityResponse]:
    """GET /heroes/{hero_id}/itemPopularity

     Get item popularity of hero categoried by start, early, mid and late game, analyzed from
    professional games

    Args:
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HeroItemPopularityResponse]
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
) -> Optional[HeroItemPopularityResponse]:
    """GET /heroes/{hero_id}/itemPopularity

     Get item popularity of hero categoried by start, early, mid and late game, analyzed from
    professional games

    Args:
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HeroItemPopularityResponse
    """

    return sync_detailed(
        hero_id=hero_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[HeroItemPopularityResponse]:
    """GET /heroes/{hero_id}/itemPopularity

     Get item popularity of hero categoried by start, early, mid and late game, analyzed from
    professional games

    Args:
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HeroItemPopularityResponse]
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
) -> Optional[HeroItemPopularityResponse]:
    """GET /heroes/{hero_id}/itemPopularity

     Get item popularity of hero categoried by start, early, mid and late game, analyzed from
    professional games

    Args:
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HeroItemPopularityResponse
    """

    return (
        await asyncio_detailed(
            hero_id=hero_id,
            client=client,
        )
    ).parsed
