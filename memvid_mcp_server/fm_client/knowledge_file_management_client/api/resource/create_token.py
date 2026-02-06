from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.exception import Exception_
from ...models.resource_token import ResourceToken
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    download: bool | Unset = False,
    preview: bool | Unset = False,
    x_realm_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Realm-ID"] = x_realm_id

    params: dict[str, Any] = {}

    params["download"] = download

    params["preview"] = preview

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/resource/token/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Exception_ | ResourceToken:
    if response.status_code == 201:
        response_201 = ResourceToken.from_dict(response.json())

        return response_201

    response_default = Exception_.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Exception_ | ResourceToken]:
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
    download: bool | Unset = False,
    preview: bool | Unset = False,
    x_realm_id: str,
) -> Response[Exception_ | ResourceToken]:
    """Create a isTemporary download token for a resource/file

    Args:
        id (str):
        download (bool | Unset):  Default: False.
        preview (bool | Unset):  Default: False.
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | ResourceToken]
    """

    kwargs = _get_kwargs(
        id=id,
        download=download,
        preview=preview,
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
    download: bool | Unset = False,
    preview: bool | Unset = False,
    x_realm_id: str,
) -> Exception_ | ResourceToken | None:
    """Create a isTemporary download token for a resource/file

    Args:
        id (str):
        download (bool | Unset):  Default: False.
        preview (bool | Unset):  Default: False.
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | ResourceToken
    """

    return sync_detailed(
        id=id,
        client=client,
        download=download,
        preview=preview,
        x_realm_id=x_realm_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    download: bool | Unset = False,
    preview: bool | Unset = False,
    x_realm_id: str,
) -> Response[Exception_ | ResourceToken]:
    """Create a isTemporary download token for a resource/file

    Args:
        id (str):
        download (bool | Unset):  Default: False.
        preview (bool | Unset):  Default: False.
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | ResourceToken]
    """

    kwargs = _get_kwargs(
        id=id,
        download=download,
        preview=preview,
        x_realm_id=x_realm_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    download: bool | Unset = False,
    preview: bool | Unset = False,
    x_realm_id: str,
) -> Exception_ | ResourceToken | None:
    """Create a isTemporary download token for a resource/file

    Args:
        id (str):
        download (bool | Unset):  Default: False.
        preview (bool | Unset):  Default: False.
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | ResourceToken
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            download=download,
            preview=preview,
            x_realm_id=x_realm_id,
        )
    ).parsed
