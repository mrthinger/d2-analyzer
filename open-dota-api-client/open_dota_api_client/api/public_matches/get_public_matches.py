from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.public_matches_response import PublicMatchesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    less_than_match_id: Union[Unset, None, int] = UNSET,
    min_rank: Union[Unset, None, int] = UNSET,
    max_rank: Union[Unset, None, int] = UNSET,
    mmr_ascending: Union[Unset, None, int] = UNSET,
    mmr_descending: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["less_than_match_id"] = less_than_match_id

    params["min_rank"] = min_rank

    params["max_rank"] = max_rank

    params["mmr_ascending"] = mmr_ascending

    params["mmr_descending"] = mmr_descending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/publicMatches",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["PublicMatchesResponse"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PublicMatchesResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["PublicMatchesResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    less_than_match_id: Union[Unset, None, int] = UNSET,
    min_rank: Union[Unset, None, int] = UNSET,
    max_rank: Union[Unset, None, int] = UNSET,
    mmr_ascending: Union[Unset, None, int] = UNSET,
    mmr_descending: Union[Unset, None, int] = UNSET,
) -> Response[List["PublicMatchesResponse"]]:
    """GET /publicMatches

     Get list of randomly sampled public matches

    Args:
        less_than_match_id (Union[Unset, None, int]):
        min_rank (Union[Unset, None, int]):
        max_rank (Union[Unset, None, int]):
        mmr_ascending (Union[Unset, None, int]):
        mmr_descending (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['PublicMatchesResponse']]
    """

    kwargs = _get_kwargs(
        less_than_match_id=less_than_match_id,
        min_rank=min_rank,
        max_rank=max_rank,
        mmr_ascending=mmr_ascending,
        mmr_descending=mmr_descending,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    less_than_match_id: Union[Unset, None, int] = UNSET,
    min_rank: Union[Unset, None, int] = UNSET,
    max_rank: Union[Unset, None, int] = UNSET,
    mmr_ascending: Union[Unset, None, int] = UNSET,
    mmr_descending: Union[Unset, None, int] = UNSET,
) -> Optional[List["PublicMatchesResponse"]]:
    """GET /publicMatches

     Get list of randomly sampled public matches

    Args:
        less_than_match_id (Union[Unset, None, int]):
        min_rank (Union[Unset, None, int]):
        max_rank (Union[Unset, None, int]):
        mmr_ascending (Union[Unset, None, int]):
        mmr_descending (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['PublicMatchesResponse']
    """

    return sync_detailed(
        client=client,
        less_than_match_id=less_than_match_id,
        min_rank=min_rank,
        max_rank=max_rank,
        mmr_ascending=mmr_ascending,
        mmr_descending=mmr_descending,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    less_than_match_id: Union[Unset, None, int] = UNSET,
    min_rank: Union[Unset, None, int] = UNSET,
    max_rank: Union[Unset, None, int] = UNSET,
    mmr_ascending: Union[Unset, None, int] = UNSET,
    mmr_descending: Union[Unset, None, int] = UNSET,
) -> Response[List["PublicMatchesResponse"]]:
    """GET /publicMatches

     Get list of randomly sampled public matches

    Args:
        less_than_match_id (Union[Unset, None, int]):
        min_rank (Union[Unset, None, int]):
        max_rank (Union[Unset, None, int]):
        mmr_ascending (Union[Unset, None, int]):
        mmr_descending (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['PublicMatchesResponse']]
    """

    kwargs = _get_kwargs(
        less_than_match_id=less_than_match_id,
        min_rank=min_rank,
        max_rank=max_rank,
        mmr_ascending=mmr_ascending,
        mmr_descending=mmr_descending,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    less_than_match_id: Union[Unset, None, int] = UNSET,
    min_rank: Union[Unset, None, int] = UNSET,
    max_rank: Union[Unset, None, int] = UNSET,
    mmr_ascending: Union[Unset, None, int] = UNSET,
    mmr_descending: Union[Unset, None, int] = UNSET,
) -> Optional[List["PublicMatchesResponse"]]:
    """GET /publicMatches

     Get list of randomly sampled public matches

    Args:
        less_than_match_id (Union[Unset, None, int]):
        min_rank (Union[Unset, None, int]):
        max_rank (Union[Unset, None, int]):
        mmr_ascending (Union[Unset, None, int]):
        mmr_descending (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['PublicMatchesResponse']
    """

    return (
        await asyncio_detailed(
            client=client,
            less_than_match_id=less_than_match_id,
            min_rank=min_rank,
            max_rank=max_rank,
            mmr_ascending=mmr_ascending,
            mmr_descending=mmr_descending,
        )
    ).parsed
