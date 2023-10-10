from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_players_by_account_id_histograms_by_field_player_histograms_response import (
    GetPlayersByAccountIdHistogramsByFieldPlayerHistogramsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: int,
    field: str,
    *,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    win: Union[Unset, None, int] = UNSET,
    patch: Union[Unset, None, int] = UNSET,
    game_mode: Union[Unset, None, int] = UNSET,
    lobby_type: Union[Unset, None, int] = UNSET,
    region: Union[Unset, None, int] = UNSET,
    date: Union[Unset, None, int] = UNSET,
    lane_role: Union[Unset, None, int] = UNSET,
    hero_id: Union[Unset, None, int] = UNSET,
    is_radiant: Union[Unset, None, int] = UNSET,
    included_account_id: Union[Unset, None, int] = UNSET,
    excluded_account_id: Union[Unset, None, int] = UNSET,
    with_hero_id: Union[Unset, None, int] = UNSET,
    against_hero_id: Union[Unset, None, int] = UNSET,
    significant: Union[Unset, None, int] = UNSET,
    having: Union[Unset, None, int] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["offset"] = offset

    params["win"] = win

    params["patch"] = patch

    params["game_mode"] = game_mode

    params["lobby_type"] = lobby_type

    params["region"] = region

    params["date"] = date

    params["lane_role"] = lane_role

    params["hero_id"] = hero_id

    params["is_radiant"] = is_radiant

    params["included_account_id"] = included_account_id

    params["excluded_account_id"] = excluded_account_id

    params["with_hero_id"] = with_hero_id

    params["against_hero_id"] = against_hero_id

    params["significant"] = significant

    params["having"] = having

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/players/{account_id}/histograms/{field}".format(
            account_id=account_id,
            field=field,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["GetPlayersByAccountIdHistogramsByFieldPlayerHistogramsResponse"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetPlayersByAccountIdHistogramsByFieldPlayerHistogramsResponse.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["GetPlayersByAccountIdHistogramsByFieldPlayerHistogramsResponse"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: int,
    field: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    win: Union[Unset, None, int] = UNSET,
    patch: Union[Unset, None, int] = UNSET,
    game_mode: Union[Unset, None, int] = UNSET,
    lobby_type: Union[Unset, None, int] = UNSET,
    region: Union[Unset, None, int] = UNSET,
    date: Union[Unset, None, int] = UNSET,
    lane_role: Union[Unset, None, int] = UNSET,
    hero_id: Union[Unset, None, int] = UNSET,
    is_radiant: Union[Unset, None, int] = UNSET,
    included_account_id: Union[Unset, None, int] = UNSET,
    excluded_account_id: Union[Unset, None, int] = UNSET,
    with_hero_id: Union[Unset, None, int] = UNSET,
    against_hero_id: Union[Unset, None, int] = UNSET,
    significant: Union[Unset, None, int] = UNSET,
    having: Union[Unset, None, int] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[List["GetPlayersByAccountIdHistogramsByFieldPlayerHistogramsResponse"]]:
    """GET /players/{account_id}/histograms

     Distribution of matches in a single stat

    Args:
        account_id (int):
        field (str):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        win (Union[Unset, None, int]):
        patch (Union[Unset, None, int]):
        game_mode (Union[Unset, None, int]):
        lobby_type (Union[Unset, None, int]):
        region (Union[Unset, None, int]):
        date (Union[Unset, None, int]):
        lane_role (Union[Unset, None, int]):
        hero_id (Union[Unset, None, int]):
        is_radiant (Union[Unset, None, int]):
        included_account_id (Union[Unset, None, int]):
        excluded_account_id (Union[Unset, None, int]):
        with_hero_id (Union[Unset, None, int]):
        against_hero_id (Union[Unset, None, int]):
        significant (Union[Unset, None, int]):
        having (Union[Unset, None, int]):
        sort (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GetPlayersByAccountIdHistogramsByFieldPlayerHistogramsResponse']]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        field=field,
        limit=limit,
        offset=offset,
        win=win,
        patch=patch,
        game_mode=game_mode,
        lobby_type=lobby_type,
        region=region,
        date=date,
        lane_role=lane_role,
        hero_id=hero_id,
        is_radiant=is_radiant,
        included_account_id=included_account_id,
        excluded_account_id=excluded_account_id,
        with_hero_id=with_hero_id,
        against_hero_id=against_hero_id,
        significant=significant,
        having=having,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: int,
    field: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    win: Union[Unset, None, int] = UNSET,
    patch: Union[Unset, None, int] = UNSET,
    game_mode: Union[Unset, None, int] = UNSET,
    lobby_type: Union[Unset, None, int] = UNSET,
    region: Union[Unset, None, int] = UNSET,
    date: Union[Unset, None, int] = UNSET,
    lane_role: Union[Unset, None, int] = UNSET,
    hero_id: Union[Unset, None, int] = UNSET,
    is_radiant: Union[Unset, None, int] = UNSET,
    included_account_id: Union[Unset, None, int] = UNSET,
    excluded_account_id: Union[Unset, None, int] = UNSET,
    with_hero_id: Union[Unset, None, int] = UNSET,
    against_hero_id: Union[Unset, None, int] = UNSET,
    significant: Union[Unset, None, int] = UNSET,
    having: Union[Unset, None, int] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[List["GetPlayersByAccountIdHistogramsByFieldPlayerHistogramsResponse"]]:
    """GET /players/{account_id}/histograms

     Distribution of matches in a single stat

    Args:
        account_id (int):
        field (str):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        win (Union[Unset, None, int]):
        patch (Union[Unset, None, int]):
        game_mode (Union[Unset, None, int]):
        lobby_type (Union[Unset, None, int]):
        region (Union[Unset, None, int]):
        date (Union[Unset, None, int]):
        lane_role (Union[Unset, None, int]):
        hero_id (Union[Unset, None, int]):
        is_radiant (Union[Unset, None, int]):
        included_account_id (Union[Unset, None, int]):
        excluded_account_id (Union[Unset, None, int]):
        with_hero_id (Union[Unset, None, int]):
        against_hero_id (Union[Unset, None, int]):
        significant (Union[Unset, None, int]):
        having (Union[Unset, None, int]):
        sort (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GetPlayersByAccountIdHistogramsByFieldPlayerHistogramsResponse']
    """

    return sync_detailed(
        account_id=account_id,
        field=field,
        client=client,
        limit=limit,
        offset=offset,
        win=win,
        patch=patch,
        game_mode=game_mode,
        lobby_type=lobby_type,
        region=region,
        date=date,
        lane_role=lane_role,
        hero_id=hero_id,
        is_radiant=is_radiant,
        included_account_id=included_account_id,
        excluded_account_id=excluded_account_id,
        with_hero_id=with_hero_id,
        against_hero_id=against_hero_id,
        significant=significant,
        having=having,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    account_id: int,
    field: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    win: Union[Unset, None, int] = UNSET,
    patch: Union[Unset, None, int] = UNSET,
    game_mode: Union[Unset, None, int] = UNSET,
    lobby_type: Union[Unset, None, int] = UNSET,
    region: Union[Unset, None, int] = UNSET,
    date: Union[Unset, None, int] = UNSET,
    lane_role: Union[Unset, None, int] = UNSET,
    hero_id: Union[Unset, None, int] = UNSET,
    is_radiant: Union[Unset, None, int] = UNSET,
    included_account_id: Union[Unset, None, int] = UNSET,
    excluded_account_id: Union[Unset, None, int] = UNSET,
    with_hero_id: Union[Unset, None, int] = UNSET,
    against_hero_id: Union[Unset, None, int] = UNSET,
    significant: Union[Unset, None, int] = UNSET,
    having: Union[Unset, None, int] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[List["GetPlayersByAccountIdHistogramsByFieldPlayerHistogramsResponse"]]:
    """GET /players/{account_id}/histograms

     Distribution of matches in a single stat

    Args:
        account_id (int):
        field (str):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        win (Union[Unset, None, int]):
        patch (Union[Unset, None, int]):
        game_mode (Union[Unset, None, int]):
        lobby_type (Union[Unset, None, int]):
        region (Union[Unset, None, int]):
        date (Union[Unset, None, int]):
        lane_role (Union[Unset, None, int]):
        hero_id (Union[Unset, None, int]):
        is_radiant (Union[Unset, None, int]):
        included_account_id (Union[Unset, None, int]):
        excluded_account_id (Union[Unset, None, int]):
        with_hero_id (Union[Unset, None, int]):
        against_hero_id (Union[Unset, None, int]):
        significant (Union[Unset, None, int]):
        having (Union[Unset, None, int]):
        sort (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GetPlayersByAccountIdHistogramsByFieldPlayerHistogramsResponse']]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        field=field,
        limit=limit,
        offset=offset,
        win=win,
        patch=patch,
        game_mode=game_mode,
        lobby_type=lobby_type,
        region=region,
        date=date,
        lane_role=lane_role,
        hero_id=hero_id,
        is_radiant=is_radiant,
        included_account_id=included_account_id,
        excluded_account_id=excluded_account_id,
        with_hero_id=with_hero_id,
        against_hero_id=against_hero_id,
        significant=significant,
        having=having,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: int,
    field: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    win: Union[Unset, None, int] = UNSET,
    patch: Union[Unset, None, int] = UNSET,
    game_mode: Union[Unset, None, int] = UNSET,
    lobby_type: Union[Unset, None, int] = UNSET,
    region: Union[Unset, None, int] = UNSET,
    date: Union[Unset, None, int] = UNSET,
    lane_role: Union[Unset, None, int] = UNSET,
    hero_id: Union[Unset, None, int] = UNSET,
    is_radiant: Union[Unset, None, int] = UNSET,
    included_account_id: Union[Unset, None, int] = UNSET,
    excluded_account_id: Union[Unset, None, int] = UNSET,
    with_hero_id: Union[Unset, None, int] = UNSET,
    against_hero_id: Union[Unset, None, int] = UNSET,
    significant: Union[Unset, None, int] = UNSET,
    having: Union[Unset, None, int] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[List["GetPlayersByAccountIdHistogramsByFieldPlayerHistogramsResponse"]]:
    """GET /players/{account_id}/histograms

     Distribution of matches in a single stat

    Args:
        account_id (int):
        field (str):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        win (Union[Unset, None, int]):
        patch (Union[Unset, None, int]):
        game_mode (Union[Unset, None, int]):
        lobby_type (Union[Unset, None, int]):
        region (Union[Unset, None, int]):
        date (Union[Unset, None, int]):
        lane_role (Union[Unset, None, int]):
        hero_id (Union[Unset, None, int]):
        is_radiant (Union[Unset, None, int]):
        included_account_id (Union[Unset, None, int]):
        excluded_account_id (Union[Unset, None, int]):
        with_hero_id (Union[Unset, None, int]):
        against_hero_id (Union[Unset, None, int]):
        significant (Union[Unset, None, int]):
        having (Union[Unset, None, int]):
        sort (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GetPlayersByAccountIdHistogramsByFieldPlayerHistogramsResponse']
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            field=field,
            client=client,
            limit=limit,
            offset=offset,
            win=win,
            patch=patch,
            game_mode=game_mode,
            lobby_type=lobby_type,
            region=region,
            date=date,
            lane_role=lane_role,
            hero_id=hero_id,
            is_radiant=is_radiant,
            included_account_id=included_account_id,
            excluded_account_id=excluded_account_id,
            with_hero_id=with_hero_id,
            against_hero_id=against_hero_id,
            significant=significant,
            having=having,
            sort=sort,
        )
    ).parsed
