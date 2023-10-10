from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_request_match_id_request_match_response import PostRequestMatchIdRequestMatchResponse
from ...types import Response


def _get_kwargs(
    match_id: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/request/{match_id}".format(
            match_id=match_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostRequestMatchIdRequestMatchResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostRequestMatchIdRequestMatchResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostRequestMatchIdRequestMatchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    match_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PostRequestMatchIdRequestMatchResponse]:
    """POST /request/{match_id}

     Submit a new parse request

    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRequestMatchIdRequestMatchResponse]
    """

    kwargs = _get_kwargs(
        match_id=match_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    match_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PostRequestMatchIdRequestMatchResponse]:
    """POST /request/{match_id}

     Submit a new parse request

    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRequestMatchIdRequestMatchResponse
    """

    return sync_detailed(
        match_id=match_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    match_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PostRequestMatchIdRequestMatchResponse]:
    """POST /request/{match_id}

     Submit a new parse request

    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRequestMatchIdRequestMatchResponse]
    """

    kwargs = _get_kwargs(
        match_id=match_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    match_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PostRequestMatchIdRequestMatchResponse]:
    """POST /request/{match_id}

     Submit a new parse request

    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRequestMatchIdRequestMatchResponse
    """

    return (
        await asyncio_detailed(
            match_id=match_id,
            client=client,
        )
    ).parsed
