from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.balance import Balance
from ...models.error_reason import ErrorReason
from ...types import Response


def _get_kwargs(
    currency: str,
    *,
    authorization: str,
    x_target_environment: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    headers["X-Target-Environment"] = x_target_environment

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1_0/account/balance/{currency}".format(
            currency=quote(str(currency), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Balance | ErrorReason | None:
    if response.status_code == 200:
        response_200 = Balance.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 500:
        response_500 = ErrorReason.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Balance | ErrorReason]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    currency: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Response[Any | Balance | ErrorReason]:
    """GetAccountBalanceInSpecificCurrency

     Get the balance of own account. Currency parameter passed in GET

    Args:
        currency (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Balance | ErrorReason]
    """

    kwargs = _get_kwargs(
        currency=currency,
        authorization=authorization,
        x_target_environment=x_target_environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    currency: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Any | Balance | ErrorReason | None:
    """GetAccountBalanceInSpecificCurrency

     Get the balance of own account. Currency parameter passed in GET

    Args:
        currency (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Balance | ErrorReason
    """

    return sync_detailed(
        currency=currency,
        client=client,
        authorization=authorization,
        x_target_environment=x_target_environment,
    ).parsed


async def asyncio_detailed(
    currency: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Response[Any | Balance | ErrorReason]:
    """GetAccountBalanceInSpecificCurrency

     Get the balance of own account. Currency parameter passed in GET

    Args:
        currency (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Balance | ErrorReason]
    """

    kwargs = _get_kwargs(
        currency=currency,
        authorization=authorization,
        x_target_environment=x_target_environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    currency: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Any | Balance | ErrorReason | None:
    """GetAccountBalanceInSpecificCurrency

     Get the balance of own account. Currency parameter passed in GET

    Args:
        currency (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Balance | ErrorReason
    """

    return (
        await asyncio_detailed(
            currency=currency,
            client=client,
            authorization=authorization,
            x_target_environment=x_target_environment,
        )
    ).parsed
