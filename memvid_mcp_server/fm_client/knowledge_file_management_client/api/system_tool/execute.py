from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.exception import Exception_
from ...models.system_tool import SystemTool
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SystemTool | Unset = UNSET,
    x_realm_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Realm-ID"] = x_realm_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/systool",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json; charset=utf-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Exception_ | SystemTool:
    if response.status_code == 200:
        response_200 = SystemTool.from_dict(response.json())

        return response_200

    response_default = Exception_.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Exception_ | SystemTool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SystemTool | Unset = UNSET,
    x_realm_id: str,
) -> Response[Exception_ | SystemTool]:
    """Execute a system tool

    Args:
        x_realm_id (str):
        body (SystemTool | Unset): A system tool that can be executed to perform a specific task
            for a single realm, e.g. cleanup operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | SystemTool]
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
    body: SystemTool | Unset = UNSET,
    x_realm_id: str,
) -> Exception_ | SystemTool | None:
    """Execute a system tool

    Args:
        x_realm_id (str):
        body (SystemTool | Unset): A system tool that can be executed to perform a specific task
            for a single realm, e.g. cleanup operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | SystemTool
    """

    return sync_detailed(
        client=client,
        body=body,
        x_realm_id=x_realm_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SystemTool | Unset = UNSET,
    x_realm_id: str,
) -> Response[Exception_ | SystemTool]:
    """Execute a system tool

    Args:
        x_realm_id (str):
        body (SystemTool | Unset): A system tool that can be executed to perform a specific task
            for a single realm, e.g. cleanup operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | SystemTool]
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
    body: SystemTool | Unset = UNSET,
    x_realm_id: str,
) -> Exception_ | SystemTool | None:
    """Execute a system tool

    Args:
        x_realm_id (str):
        body (SystemTool | Unset): A system tool that can be executed to perform a specific task
            for a single realm, e.g. cleanup operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | SystemTool
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_realm_id=x_realm_id,
        )
    ).parsed
