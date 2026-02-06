from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.base_entity import BaseEntity
from ...models.duplicates_request import DuplicatesRequest
from ...models.exception import Exception_
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DuplicatesRequest | Unset = UNSET,
    x_realm_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Realm-ID"] = x_realm_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/document/v2/duplicates",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json; charset=utf-8"

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
    *,
    client: AuthenticatedClient | Client,
    body: DuplicatesRequest | Unset = UNSET,
    x_realm_id: str,
) -> Response[Exception_ | list[BaseEntity]]:
    """Retrieve all possible duplicates of given sets of CRC32 and MD5 checksums

    Args:
        x_realm_id (str):
        body (DuplicatesRequest | Unset): A request to retrieve all possible duplicates of given
            sets of CRC32 and MD5 checksums

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | list[BaseEntity]]
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
    body: DuplicatesRequest | Unset = UNSET,
    x_realm_id: str,
) -> Exception_ | list[BaseEntity] | None:
    """Retrieve all possible duplicates of given sets of CRC32 and MD5 checksums

    Args:
        x_realm_id (str):
        body (DuplicatesRequest | Unset): A request to retrieve all possible duplicates of given
            sets of CRC32 and MD5 checksums

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | list[BaseEntity]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_realm_id=x_realm_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DuplicatesRequest | Unset = UNSET,
    x_realm_id: str,
) -> Response[Exception_ | list[BaseEntity]]:
    """Retrieve all possible duplicates of given sets of CRC32 and MD5 checksums

    Args:
        x_realm_id (str):
        body (DuplicatesRequest | Unset): A request to retrieve all possible duplicates of given
            sets of CRC32 and MD5 checksums

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | list[BaseEntity]]
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
    body: DuplicatesRequest | Unset = UNSET,
    x_realm_id: str,
) -> Exception_ | list[BaseEntity] | None:
    """Retrieve all possible duplicates of given sets of CRC32 and MD5 checksums

    Args:
        x_realm_id (str):
        body (DuplicatesRequest | Unset): A request to retrieve all possible duplicates of given
            sets of CRC32 and MD5 checksums

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | list[BaseEntity]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_realm_id=x_realm_id,
        )
    ).parsed
