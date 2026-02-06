from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.exception import Exception_
from ...models.resource_token import ResourceToken
from ...models.upload_temp_file_body import UploadTempFileBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UploadTempFileBody | Unset = UNSET,
    download: bool | Unset = True,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Realm-ID"] = x_realm_id

    if not isinstance(x_av_privilege, Unset):
        headers["X-AV-Privilege"] = x_av_privilege

    params: dict[str, Any] = {}

    params["download"] = download

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/file/v2/temp",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

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
    *,
    client: AuthenticatedClient | Client,
    body: UploadTempFileBody | Unset = UNSET,
    download: bool | Unset = True,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> Response[Exception_ | ResourceToken]:
    r"""Uploads a new isTemporary file to FM. The file will not be associated with any document or folder
    and will be deleted automatically after 10 minutes.
    When virus scanning is enabled for the target FM deployment, the file will be scanned for viruses
    and rejected in case a virus is found.
    The virus scan may be bypassed by providing a value for the \"X-AV-Privilege\" header that is found
    in the realm's antiVirusWhitelist. An empty value will always be virus scanned, an unknown value
    will always be rejected.

    Args:
        download (bool | Unset):  Default: True.
        x_realm_id (str):
        x_av_privilege (str | Unset):  Default: ''.
        body (UploadTempFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | ResourceToken]
    """

    kwargs = _get_kwargs(
        body=body,
        download=download,
        x_realm_id=x_realm_id,
        x_av_privilege=x_av_privilege,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UploadTempFileBody | Unset = UNSET,
    download: bool | Unset = True,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> Exception_ | ResourceToken | None:
    r"""Uploads a new isTemporary file to FM. The file will not be associated with any document or folder
    and will be deleted automatically after 10 minutes.
    When virus scanning is enabled for the target FM deployment, the file will be scanned for viruses
    and rejected in case a virus is found.
    The virus scan may be bypassed by providing a value for the \"X-AV-Privilege\" header that is found
    in the realm's antiVirusWhitelist. An empty value will always be virus scanned, an unknown value
    will always be rejected.

    Args:
        download (bool | Unset):  Default: True.
        x_realm_id (str):
        x_av_privilege (str | Unset):  Default: ''.
        body (UploadTempFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | ResourceToken
    """

    return sync_detailed(
        client=client,
        body=body,
        download=download,
        x_realm_id=x_realm_id,
        x_av_privilege=x_av_privilege,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadTempFileBody | Unset = UNSET,
    download: bool | Unset = True,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> Response[Exception_ | ResourceToken]:
    r"""Uploads a new isTemporary file to FM. The file will not be associated with any document or folder
    and will be deleted automatically after 10 minutes.
    When virus scanning is enabled for the target FM deployment, the file will be scanned for viruses
    and rejected in case a virus is found.
    The virus scan may be bypassed by providing a value for the \"X-AV-Privilege\" header that is found
    in the realm's antiVirusWhitelist. An empty value will always be virus scanned, an unknown value
    will always be rejected.

    Args:
        download (bool | Unset):  Default: True.
        x_realm_id (str):
        x_av_privilege (str | Unset):  Default: ''.
        body (UploadTempFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Exception_ | ResourceToken]
    """

    kwargs = _get_kwargs(
        body=body,
        download=download,
        x_realm_id=x_realm_id,
        x_av_privilege=x_av_privilege,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UploadTempFileBody | Unset = UNSET,
    download: bool | Unset = True,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> Exception_ | ResourceToken | None:
    r"""Uploads a new isTemporary file to FM. The file will not be associated with any document or folder
    and will be deleted automatically after 10 minutes.
    When virus scanning is enabled for the target FM deployment, the file will be scanned for viruses
    and rejected in case a virus is found.
    The virus scan may be bypassed by providing a value for the \"X-AV-Privilege\" header that is found
    in the realm's antiVirusWhitelist. An empty value will always be virus scanned, an unknown value
    will always be rejected.

    Args:
        download (bool | Unset):  Default: True.
        x_realm_id (str):
        x_av_privilege (str | Unset):  Default: ''.
        body (UploadTempFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Exception_ | ResourceToken
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            download=download,
            x_realm_id=x_realm_id,
            x_av_privilege=x_av_privilege,
        )
    ).parsed
