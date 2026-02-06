from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.base_entity import BaseEntity
from ...models.exception import Exception_
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    x_realm_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Realm-ID"] = x_realm_id

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/document/v2/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BaseEntity | Exception_:
    if response.status_code == 200:
        response_200 = BaseEntity.from_dict(response.json())

        return response_200

    response_default = Exception_.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BaseEntity | Exception_]:
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
    x_realm_id: str,
) -> Response[BaseEntity | Exception_]:
    """Delete an existing document as well as the associated file

    Args:
        id (str):
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BaseEntity | Exception_]
    """

    kwargs = _get_kwargs(
        id=id,
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
    x_realm_id: str,
) -> BaseEntity | Exception_ | None:
    """Delete an existing document as well as the associated file

    Args:
        id (str):
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BaseEntity | Exception_
    """

    return sync_detailed(
        id=id,
        client=client,
        x_realm_id=x_realm_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    x_realm_id: str,
) -> Response[BaseEntity | Exception_]:
    """Delete an existing document as well as the associated file

    Args:
        id (str):
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BaseEntity | Exception_]
    """

    kwargs = _get_kwargs(
        id=id,
        x_realm_id=x_realm_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    x_realm_id: str,
) -> BaseEntity | Exception_ | None:
    """Delete an existing document as well as the associated file

    Args:
        id (str):
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BaseEntity | Exception_
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            x_realm_id=x_realm_id,
        )
    ).parsed
