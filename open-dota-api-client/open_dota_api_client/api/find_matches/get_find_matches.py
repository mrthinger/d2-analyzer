from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_find_matches_response_200_item import GetFindMatchesResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    team_a: Union[Unset, None, List[int]] = UNSET,
    team_b: Union[Unset, None, List[int]] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_team_a: Union[Unset, None, List[int]] = UNSET
    if not isinstance(team_a, Unset):
        if team_a is None:
            json_team_a = None
        else:
            json_team_a = team_a

    params["teamA"] = json_team_a

    json_team_b: Union[Unset, None, List[int]] = UNSET
    if not isinstance(team_b, Unset):
        if team_b is None:
            json_team_b = None
        else:
            json_team_b = team_b

    params["teamB"] = json_team_b

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/findMatches",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["GetFindMatchesResponse200Item"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetFindMatchesResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["GetFindMatchesResponse200Item"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    team_a: Union[Unset, None, List[int]] = UNSET,
    team_b: Union[Unset, None, List[int]] = UNSET,
) -> Response[List["GetFindMatchesResponse200Item"]]:
    """GET /

     Finds recent matches by heroes played

    Args:
        team_a (Union[Unset, None, List[int]]):
        team_b (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GetFindMatchesResponse200Item']]
    """

    kwargs = _get_kwargs(
        team_a=team_a,
        team_b=team_b,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    team_a: Union[Unset, None, List[int]] = UNSET,
    team_b: Union[Unset, None, List[int]] = UNSET,
) -> Optional[List["GetFindMatchesResponse200Item"]]:
    """GET /

     Finds recent matches by heroes played

    Args:
        team_a (Union[Unset, None, List[int]]):
        team_b (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GetFindMatchesResponse200Item']
    """

    return sync_detailed(
        client=client,
        team_a=team_a,
        team_b=team_b,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    team_a: Union[Unset, None, List[int]] = UNSET,
    team_b: Union[Unset, None, List[int]] = UNSET,
) -> Response[List["GetFindMatchesResponse200Item"]]:
    """GET /

     Finds recent matches by heroes played

    Args:
        team_a (Union[Unset, None, List[int]]):
        team_b (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GetFindMatchesResponse200Item']]
    """

    kwargs = _get_kwargs(
        team_a=team_a,
        team_b=team_b,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    team_a: Union[Unset, None, List[int]] = UNSET,
    team_b: Union[Unset, None, List[int]] = UNSET,
) -> Optional[List["GetFindMatchesResponse200Item"]]:
    """GET /

     Finds recent matches by heroes played

    Args:
        team_a (Union[Unset, None, List[int]]):
        team_b (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GetFindMatchesResponse200Item']
    """

    return (
        await asyncio_detailed(
            client=client,
            team_a=team_a,
            team_b=team_b,
        )
    ).parsed
