from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.base_entity import BaseEntity
from ...models.exception import Exception_
from ...models.upload_file_body import UploadFileBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UploadFileBody | Unset = UNSET,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Realm-ID"] = x_realm_id

    if not isinstance(x_av_privilege, Unset):
        headers["X-AV-Privilege"] = x_av_privilege

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/file/v2",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BaseEntity | Exception_:
    if response.status_code == 201:
        response_201 = BaseEntity.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileBody | Unset = UNSET,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> Response[BaseEntity | Exception_]:
    r"""Uploads a new file to FM and implicitly creates a new Document handler for it. Checksums, mimetypes
    etc. will be calculated automatically. The \"title\", \"parentFolderId\", \"description\" and
    \"metaInfo\" fields of the given document will be respected during the upload process.
    When virus scanning is enabled for the target FM deployment, the file will be scanned for viruses
    and rejected in case a virus is found.
    The virus scan may be bypassed by providing a value for the \"X-AV-Privilege\" header that is found
    in the realm's antiVirusWhitelist. An empty value will always be virus scanned, an unknown value
    will always be rejected.
    When preview conversion is enabled for the target FM deployment, if the file's mimetype is eligible
    for preview conversion (e.g. an MS Office or OpenOffice file), a preview PDF version of the file is
    generated and stored alongside the original

    Args:
        x_realm_id (str):
        x_av_privilege (str | Unset):  Default: ''.
        body (UploadFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BaseEntity | Exception_]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: UploadFileBody | Unset = UNSET,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> BaseEntity | Exception_ | None:
    r"""Uploads a new file to FM and implicitly creates a new Document handler for it. Checksums, mimetypes
    etc. will be calculated automatically. The \"title\", \"parentFolderId\", \"description\" and
    \"metaInfo\" fields of the given document will be respected during the upload process.
    When virus scanning is enabled for the target FM deployment, the file will be scanned for viruses
    and rejected in case a virus is found.
    The virus scan may be bypassed by providing a value for the \"X-AV-Privilege\" header that is found
    in the realm's antiVirusWhitelist. An empty value will always be virus scanned, an unknown value
    will always be rejected.
    When preview conversion is enabled for the target FM deployment, if the file's mimetype is eligible
    for preview conversion (e.g. an MS Office or OpenOffice file), a preview PDF version of the file is
    generated and stored alongside the original

    Args:
        x_realm_id (str):
        x_av_privilege (str | Unset):  Default: ''.
        body (UploadFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BaseEntity | Exception_
    """

    return sync_detailed(
        client=client,
        body=body,
        x_realm_id=x_realm_id,
        x_av_privilege=x_av_privilege,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileBody | Unset = UNSET,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> Response[BaseEntity | Exception_]:
    r"""Uploads a new file to FM and implicitly creates a new Document handler for it. Checksums, mimetypes
    etc. will be calculated automatically. The \"title\", \"parentFolderId\", \"description\" and
    \"metaInfo\" fields of the given document will be respected during the upload process.
    When virus scanning is enabled for the target FM deployment, the file will be scanned for viruses
    and rejected in case a virus is found.
    The virus scan may be bypassed by providing a value for the \"X-AV-Privilege\" header that is found
    in the realm's antiVirusWhitelist. An empty value will always be virus scanned, an unknown value
    will always be rejected.
    When preview conversion is enabled for the target FM deployment, if the file's mimetype is eligible
    for preview conversion (e.g. an MS Office or OpenOffice file), a preview PDF version of the file is
    generated and stored alongside the original

    Args:
        x_realm_id (str):
        x_av_privilege (str | Unset):  Default: ''.
        body (UploadFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BaseEntity | Exception_]
    """

    kwargs = _get_kwargs(
        body=body,
        x_realm_id=x_realm_id,
        x_av_privilege=x_av_privilege,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileBody | Unset = UNSET,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> BaseEntity | Exception_ | None:
    r"""Uploads a new file to FM and implicitly creates a new Document handler for it. Checksums, mimetypes
    etc. will be calculated automatically. The \"title\", \"parentFolderId\", \"description\" and
    \"metaInfo\" fields of the given document will be respected during the upload process.
    When virus scanning is enabled for the target FM deployment, the file will be scanned for viruses
    and rejected in case a virus is found.
    The virus scan may be bypassed by providing a value for the \"X-AV-Privilege\" header that is found
    in the realm's antiVirusWhitelist. An empty value will always be virus scanned, an unknown value
    will always be rejected.
    When preview conversion is enabled for the target FM deployment, if the file's mimetype is eligible
    for preview conversion (e.g. an MS Office or OpenOffice file), a preview PDF version of the file is
    generated and stored alongside the original

    Args:
        x_realm_id (str):
        x_av_privilege (str | Unset):  Default: ''.
        body (UploadFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BaseEntity | Exception_
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_realm_id=x_realm_id,
            x_av_privilege=x_av_privilege,
        )
    ).parsed
