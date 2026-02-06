from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.exception import Exception_
from ...models.realm import Realm
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: Realm | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/realm/v2/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json; charset=utf-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Exception_ | Realm:
    if response.status_code == 200:
        response_200 = Realm.from_dict(response.json())

        return response_200

    response_default = Exception_.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Exception_ | Realm]:
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
    body: Realm | Unset = UNSET,
) -> Response[Exception_ | Realm]:
    """Update the settings of a realm. Provide null or an empty dictionary for the given Realm's settings
    to reset to default settings.

    Args:
        id (str):
        body (Realm | Unset): External representation of a realm entity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | Realm]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Realm | Unset = UNSET,
) -> Exception_ | Realm | None:
    """Update the settings of a realm. Provide null or an empty dictionary for the given Realm's settings
    to reset to default settings.

    Args:
        id (str):
        body (Realm | Unset): External representation of a realm entity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | Realm
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Realm | Unset = UNSET,
) -> Response[Exception_ | Realm]:
    """Update the settings of a realm. Provide null or an empty dictionary for the given Realm's settings
    to reset to default settings.

    Args:
        id (str):
        body (Realm | Unset): External representation of a realm entity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | Realm]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Realm | Unset = UNSET,
) -> Exception_ | Realm | None:
    """Update the settings of a realm. Provide null or an empty dictionary for the given Realm's settings
    to reset to default settings.

    Args:
        id (str):
        body (Realm | Unset): External representation of a realm entity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | Realm
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
