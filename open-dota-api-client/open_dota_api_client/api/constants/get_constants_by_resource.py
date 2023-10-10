from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_constants_by_resource_response_200_type_0 import GetConstantsByResourceResponse200Type0
from ...models.get_constants_by_resource_response_200_type_1_item_type_0 import (
    GetConstantsByResourceResponse200Type1ItemType0,
)
from ...types import UNSET, Response


def _get_kwargs(
    resource: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/constants/{resource}".format(
            resource=resource,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        "GetConstantsByResourceResponse200Type0",
        List[Union["GetConstantsByResourceResponse200Type1ItemType0", int]],
        None,
    ]
]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "GetConstantsByResourceResponse200Type0",
            List[Union["GetConstantsByResourceResponse200Type1ItemType0", int]],
            None,
        ]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GetConstantsByResourceResponse200Type0.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            response_200_type_1 = UNSET
            _response_200_type_1 = data
            for response_200_type_1_item_data in _response_200_type_1:

                def _parse_response_200_type_1_item(
                    data: object,
                ) -> Union["GetConstantsByResourceResponse200Type1ItemType0", int]:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        response_200_type_1_item_type_0 = GetConstantsByResourceResponse200Type1ItemType0.from_dict(
                            data
                        )

                        return response_200_type_1_item_type_0
                    except:  # noqa: E722
                        pass
                    return cast(Union["GetConstantsByResourceResponse200Type1ItemType0", int], data)

                response_200_type_1_item = _parse_response_200_type_1_item(response_200_type_1_item_data)

                response_200_type_1.append(response_200_type_1_item)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        "GetConstantsByResourceResponse200Type0",
        List[Union["GetConstantsByResourceResponse200Type1ItemType0", int]],
        None,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        "GetConstantsByResourceResponse200Type0",
        List[Union["GetConstantsByResourceResponse200Type1ItemType0", int]],
        None,
    ]
]:
    """GET /constants

     Get static game data mirrored from the dotaconstants repository.

    Args:
        resource (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['GetConstantsByResourceResponse200Type0', List[Union['GetConstantsByResourceResponse200Type1ItemType0', int]], None]]
    """

    kwargs = _get_kwargs(
        resource=resource,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        "GetConstantsByResourceResponse200Type0",
        List[Union["GetConstantsByResourceResponse200Type1ItemType0", int]],
        None,
    ]
]:
    """GET /constants

     Get static game data mirrored from the dotaconstants repository.

    Args:
        resource (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['GetConstantsByResourceResponse200Type0', List[Union['GetConstantsByResourceResponse200Type1ItemType0', int]], None]
    """

    return sync_detailed(
        resource=resource,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        "GetConstantsByResourceResponse200Type0",
        List[Union["GetConstantsByResourceResponse200Type1ItemType0", int]],
        None,
    ]
]:
    """GET /constants

     Get static game data mirrored from the dotaconstants repository.

    Args:
        resource (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['GetConstantsByResourceResponse200Type0', List[Union['GetConstantsByResourceResponse200Type1ItemType0', int]], None]]
    """

    kwargs = _get_kwargs(
        resource=resource,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        "GetConstantsByResourceResponse200Type0",
        List[Union["GetConstantsByResourceResponse200Type1ItemType0", int]],
        None,
    ]
]:
    """GET /constants

     Get static game data mirrored from the dotaconstants repository.

    Args:
        resource (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['GetConstantsByResourceResponse200Type0', List[Union['GetConstantsByResourceResponse200Type1ItemType0', int]], None]
    """

    return (
        await asyncio_detailed(
            resource=resource,
            client=client,
        )
    ).parsed
