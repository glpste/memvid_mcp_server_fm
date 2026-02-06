from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.base_entity import BaseEntity
from ...models.exception import Exception_
from ...models.update_file_body import UpdateFileBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: UpdateFileBody | Unset = UNSET,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Realm-ID"] = x_realm_id

    if not isinstance(x_av_privilege, Unset):
        headers["X-AV-Privilege"] = x_av_privilege

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/file/v2/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

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
    body: UpdateFileBody | Unset = UNSET,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> Response[BaseEntity | Exception_]:
    r"""Updates and existing file and associated document. The existing file associated with the given ID
    will be replaced by the given file. The \"title\", \"parentFolderId\", \"description\" and
    \"metaInfo\" fields of the given document will be respected during the update process.

    Args:
        id (str):
        x_realm_id (str):
        x_av_privilege (str | Unset):  Default: ''.
        body (UpdateFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BaseEntity | Exception_]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        x_realm_id=x_realm_id,
        x_av_privilege=x_av_privilege,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateFileBody | Unset = UNSET,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> BaseEntity | Exception_ | None:
    r"""Updates and existing file and associated document. The existing file associated with the given ID
    will be replaced by the given file. The \"title\", \"parentFolderId\", \"description\" and
    \"metaInfo\" fields of the given document will be respected during the update process.

    Args:
        id (str):
        x_realm_id (str):
        x_av_privilege (str | Unset):  Default: ''.
        body (UpdateFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BaseEntity | Exception_
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        x_realm_id=x_realm_id,
        x_av_privilege=x_av_privilege,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateFileBody | Unset = UNSET,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> Response[BaseEntity | Exception_]:
    r"""Updates and existing file and associated document. The existing file associated with the given ID
    will be replaced by the given file. The \"title\", \"parentFolderId\", \"description\" and
    \"metaInfo\" fields of the given document will be respected during the update process.

    Args:
        id (str):
        x_realm_id (str):
        x_av_privilege (str | Unset):  Default: ''.
        body (UpdateFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BaseEntity | Exception_]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        x_realm_id=x_realm_id,
        x_av_privilege=x_av_privilege,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateFileBody | Unset = UNSET,
    x_realm_id: str,
    x_av_privilege: str | Unset = "",
) -> BaseEntity | Exception_ | None:
    r"""Updates and existing file and associated document. The existing file associated with the given ID
    will be replaced by the given file. The \"title\", \"parentFolderId\", \"description\" and
    \"metaInfo\" fields of the given document will be respected during the update process.

    Args:
        id (str):
        x_realm_id (str):
        x_av_privilege (str | Unset):  Default: ''.
        body (UpdateFileBody | Unset):

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
            body=body,
            x_realm_id=x_realm_id,
            x_av_privilege=x_av_privilege,
        )
    ).parsed
