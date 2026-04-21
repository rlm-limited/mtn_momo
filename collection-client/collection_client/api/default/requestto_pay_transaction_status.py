from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_reason import ErrorReason
from ...models.request_to_pay_result import RequestToPayResult
from ...types import Response


def _get_kwargs(
    reference_id: str,
    *,
    authorization: str,
    x_target_environment: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    headers["X-Target-Environment"] = x_target_environment

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1_0/requesttopay/{reference_id}".format(
            reference_id=quote(str(reference_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorReason | RequestToPayResult | None:
    if response.status_code == 200:
        response_200 = RequestToPayResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = ErrorReason.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorReason.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorReason | RequestToPayResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reference_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Response[Any | ErrorReason | RequestToPayResult]:
    """RequesttoPayTransactionStatus

     This operation is used to get the status of a request to pay. X-Reference-Id that was passed in the
    post is used as reference to the request.

    Args:
        reference_id (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorReason | RequestToPayResult]
    """

    kwargs = _get_kwargs(
        reference_id=reference_id,
        authorization=authorization,
        x_target_environment=x_target_environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    reference_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Any | ErrorReason | RequestToPayResult | None:
    """RequesttoPayTransactionStatus

     This operation is used to get the status of a request to pay. X-Reference-Id that was passed in the
    post is used as reference to the request.

    Args:
        reference_id (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorReason | RequestToPayResult
    """

    return sync_detailed(
        reference_id=reference_id,
        client=client,
        authorization=authorization,
        x_target_environment=x_target_environment,
    ).parsed


async def asyncio_detailed(
    reference_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Response[Any | ErrorReason | RequestToPayResult]:
    """RequesttoPayTransactionStatus

     This operation is used to get the status of a request to pay. X-Reference-Id that was passed in the
    post is used as reference to the request.

    Args:
        reference_id (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorReason | RequestToPayResult]
    """

    kwargs = _get_kwargs(
        reference_id=reference_id,
        authorization=authorization,
        x_target_environment=x_target_environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reference_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Any | ErrorReason | RequestToPayResult | None:
    """RequesttoPayTransactionStatus

     This operation is used to get the status of a request to pay. X-Reference-Id that was passed in the
    post is used as reference to the request.

    Args:
        reference_id (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorReason | RequestToPayResult
    """

    return (
        await asyncio_detailed(
            reference_id=reference_id,
            client=client,
            authorization=authorization,
            x_target_environment=x_target_environment,
        )
    ).parsed
