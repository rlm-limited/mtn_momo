from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bc_authorize_body import BcAuthorizeBody
from ...models.bcauthorize_response import BcauthorizeResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BcAuthorizeBody | Unset = UNSET,
    authorization: str,
    x_target_environment: str,
    x_callback_url: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    headers["X-Target-Environment"] = x_target_environment

    if not isinstance(x_callback_url, Unset):
        headers["X-Callback-Url"] = x_callback_url

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1_0/bc-authorize",
    }

    if not isinstance(body, Unset):
        _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BcauthorizeResponse | None:
    if response.status_code == 200:
        response_200 = BcauthorizeResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BcauthorizeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BcAuthorizeBody | Unset = UNSET,
    authorization: str,
    x_target_environment: str,
    x_callback_url: str | Unset = UNSET,
) -> Response[BcauthorizeResponse]:
    """bc-authorize

     This operation is used to claim a consent by the account holder for the requested scopes.

    Args:
        authorization (str):
        x_target_environment (str):
        x_callback_url (str | Unset):
        body (BcAuthorizeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BcauthorizeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_target_environment=x_target_environment,
        x_callback_url=x_callback_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BcAuthorizeBody | Unset = UNSET,
    authorization: str,
    x_target_environment: str,
    x_callback_url: str | Unset = UNSET,
) -> BcauthorizeResponse | None:
    """bc-authorize

     This operation is used to claim a consent by the account holder for the requested scopes.

    Args:
        authorization (str):
        x_target_environment (str):
        x_callback_url (str | Unset):
        body (BcAuthorizeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BcauthorizeResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
        x_target_environment=x_target_environment,
        x_callback_url=x_callback_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BcAuthorizeBody | Unset = UNSET,
    authorization: str,
    x_target_environment: str,
    x_callback_url: str | Unset = UNSET,
) -> Response[BcauthorizeResponse]:
    """bc-authorize

     This operation is used to claim a consent by the account holder for the requested scopes.

    Args:
        authorization (str):
        x_target_environment (str):
        x_callback_url (str | Unset):
        body (BcAuthorizeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BcauthorizeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_target_environment=x_target_environment,
        x_callback_url=x_callback_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BcAuthorizeBody | Unset = UNSET,
    authorization: str,
    x_target_environment: str,
    x_callback_url: str | Unset = UNSET,
) -> BcauthorizeResponse | None:
    """bc-authorize

     This operation is used to claim a consent by the account holder for the requested scopes.

    Args:
        authorization (str):
        x_target_environment (str):
        x_callback_url (str | Unset):
        body (BcAuthorizeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BcauthorizeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
            x_target_environment=x_target_environment,
            x_callback_url=x_callback_url,
        )
    ).parsed
