from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.exception import Exception_
from ...models.page import Page
from ...models.search_body import SearchBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchBody | Unset = UNSET,
    x_realm_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Realm-ID"] = x_realm_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/document/v2/search",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json; charset=utf-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Exception_ | Page:
    if response.status_code == 200:
        response_200 = Page.from_dict(response.json())

        return response_200

    response_default = Exception_.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Exception_ | Page]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchBody | Unset = UNSET,
    x_realm_id: str,
) -> Response[Exception_ | Page]:
    """Perform a basic search over the titles, descriptions and filenames of all documents of a realm

    Args:
        x_realm_id (str):
        body (SearchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | Page]
    """

    kwargs = _get_kwargs(
        body=body,
        x_realm_id=x_realm_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchBody | Unset = UNSET,
    x_realm_id: str,
) -> Exception_ | Page | None:
    """Perform a basic search over the titles, descriptions and filenames of all documents of a realm

    Args:
        x_realm_id (str):
        body (SearchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | Page
    """

    return sync_detailed(
        client=client,
        body=body,
        x_realm_id=x_realm_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchBody | Unset = UNSET,
    x_realm_id: str,
) -> Response[Exception_ | Page]:
    """Perform a basic search over the titles, descriptions and filenames of all documents of a realm

    Args:
        x_realm_id (str):
        body (SearchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | Page]
    """

    kwargs = _get_kwargs(
        body=body,
        x_realm_id=x_realm_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchBody | Unset = UNSET,
    x_realm_id: str,
) -> Exception_ | Page | None:
    """Perform a basic search over the titles, descriptions and filenames of all documents of a realm

    Args:
        x_realm_id (str):
        body (SearchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | Page
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_realm_id=x_realm_id,
        )
    ).parsed
