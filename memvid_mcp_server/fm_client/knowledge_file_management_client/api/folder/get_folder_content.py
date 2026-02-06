from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.base_entity import BaseEntity
from ...models.exception import Exception_
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    end_id: str | Unset = UNSET,
    x_realm_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Realm-ID"] = x_realm_id

    params: dict[str, Any] = {}

    params["endId"] = end_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/folder/v2/content/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Exception_ | list[BaseEntity]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BaseEntity.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = Exception_.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Exception_ | list[BaseEntity]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    end_id: str | Unset = UNSET,
    x_realm_id: str,
) -> Response[Exception_ | list[BaseEntity]]:
    """Retrieve all contents of a folder, including both folders and documents If the 'endId' parameter is
    provided and the path between the folder identified by endId and the root node contains the folder
    identified by 'folderId', a nested-list representation of all the contents along this path is
    returned by respectively populating the 'children' property of the required folders

    Args:
        id (str):
        end_id (str | Unset):
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | list[BaseEntity]]
    """

    kwargs = _get_kwargs(
        id=id,
        end_id=end_id,
        x_realm_id=x_realm_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    end_id: str | Unset = UNSET,
    x_realm_id: str,
) -> Exception_ | list[BaseEntity] | None:
    """Retrieve all contents of a folder, including both folders and documents If the 'endId' parameter is
    provided and the path between the folder identified by endId and the root node contains the folder
    identified by 'folderId', a nested-list representation of all the contents along this path is
    returned by respectively populating the 'children' property of the required folders

    Args:
        id (str):
        end_id (str | Unset):
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | list[BaseEntity]
    """

    return sync_detailed(
        id=id,
        client=client,
        end_id=end_id,
        x_realm_id=x_realm_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    end_id: str | Unset = UNSET,
    x_realm_id: str,
) -> Response[Exception_ | list[BaseEntity]]:
    """Retrieve all contents of a folder, including both folders and documents If the 'endId' parameter is
    provided and the path between the folder identified by endId and the root node contains the folder
    identified by 'folderId', a nested-list representation of all the contents along this path is
    returned by respectively populating the 'children' property of the required folders

    Args:
        id (str):
        end_id (str | Unset):
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | list[BaseEntity]]
    """

    kwargs = _get_kwargs(
        id=id,
        end_id=end_id,
        x_realm_id=x_realm_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    end_id: str | Unset = UNSET,
    x_realm_id: str,
) -> Exception_ | list[BaseEntity] | None:
    """Retrieve all contents of a folder, including both folders and documents If the 'endId' parameter is
    provided and the path between the folder identified by endId and the root node contains the folder
    identified by 'folderId', a nested-list representation of all the contents along this path is
    returned by respectively populating the 'children' property of the required folders

    Args:
        id (str):
        end_id (str | Unset):
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | list[BaseEntity]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            end_id=end_id,
            x_realm_id=x_realm_id,
        )
    ).parsed
