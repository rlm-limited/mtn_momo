from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.consentkyc_response import ConsentkycResponse
from ...types import Response


def _get_kwargs(
    *,
    authorization: str,
    x_target_environment: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    headers["X-Target-Environment"] = x_target_environment

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/oauth2/v1_0/userinfo",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConsentkycResponse | None:
    if response.status_code == 200:
        response_200 = ConsentkycResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConsentkycResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Response[ConsentkycResponse]:
    """GetUserInfoWithConsent

     This operation is used to claim a consent by the account holder for the requested scopes.

    Args:
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsentkycResponse]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
        x_target_environment=x_target_environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> ConsentkycResponse | None:
    """GetUserInfoWithConsent

     This operation is used to claim a consent by the account holder for the requested scopes.

    Args:
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsentkycResponse
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
        x_target_environment=x_target_environment,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Response[ConsentkycResponse]:
    """GetUserInfoWithConsent

     This operation is used to claim a consent by the account holder for the requested scopes.

    Args:
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsentkycResponse]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
        x_target_environment=x_target_environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> ConsentkycResponse | None:
    """GetUserInfoWithConsent

     This operation is used to claim a consent by the account holder for the requested scopes.

    Args:
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsentkycResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
            x_target_environment=x_target_environment,
        )
    ).parsed
