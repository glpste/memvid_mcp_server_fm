from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.exception import Exception_
from ...models.file_text_content_mode import FileTextContentMode
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    id: str,
    *,
    mode: FileTextContentMode,
    download: bool | Unset = False,
    x_realm_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Realm-ID"] = x_realm_id

    params: dict[str, Any] = {}

    json_mode = mode.value
    params["mode"] = json_mode

    params["download"] = download

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/file/text/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Exception_ | File:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    response_default = Exception_.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Exception_ | File]:
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
    mode: FileTextContentMode,
    download: bool | Unset = False,
    x_realm_id: str,
) -> Response[Exception_ | File]:
    """Download the extracted text content of a file if available.
    The content type must be one of the supported text content types defined in FileTextContentMode.

    Args:
        id (str):
        mode (FileTextContentMode): The type of file text content to download.
            full: The full text content of the file as a single string.
            summary: A summarized version of the file's text content.
        download (bool | Unset):  Default: False.
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | File]
    """

    kwargs = _get_kwargs(
        id=id,
        mode=mode,
        download=download,
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
    mode: FileTextContentMode,
    download: bool | Unset = False,
    x_realm_id: str,
) -> Exception_ | File | None:
    """Download the extracted text content of a file if available.
    The content type must be one of the supported text content types defined in FileTextContentMode.

    Args:
        id (str):
        mode (FileTextContentMode): The type of file text content to download.
            full: The full text content of the file as a single string.
            summary: A summarized version of the file's text content.
        download (bool | Unset):  Default: False.
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | File
    """

    return sync_detailed(
        id=id,
        client=client,
        mode=mode,
        download=download,
        x_realm_id=x_realm_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    mode: FileTextContentMode,
    download: bool | Unset = False,
    x_realm_id: str,
) -> Response[Exception_ | File]:
    """Download the extracted text content of a file if available.
    The content type must be one of the supported text content types defined in FileTextContentMode.

    Args:
        id (str):
        mode (FileTextContentMode): The type of file text content to download.
            full: The full text content of the file as a single string.
            summary: A summarized version of the file's text content.
        download (bool | Unset):  Default: False.
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | File]
    """

    kwargs = _get_kwargs(
        id=id,
        mode=mode,
        download=download,
        x_realm_id=x_realm_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    mode: FileTextContentMode,
    download: bool | Unset = False,
    x_realm_id: str,
) -> Exception_ | File | None:
    """Download the extracted text content of a file if available.
    The content type must be one of the supported text content types defined in FileTextContentMode.

    Args:
        id (str):
        mode (FileTextContentMode): The type of file text content to download.
            full: The full text content of the file as a single string.
            summary: A summarized version of the file's text content.
        download (bool | Unset):  Default: False.
        x_realm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | File
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            mode=mode,
            download=download,
            x_realm_id=x_realm_id,
        )
    ).parsed
