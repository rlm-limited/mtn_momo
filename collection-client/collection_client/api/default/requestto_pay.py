from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_reason import ErrorReason
from ...models.request_to_pay import RequestToPay
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RequestToPay | Unset = UNSET,
    authorization: str,
    x_callback_url: str | Unset = UNSET,
    x_reference_id: str,
    x_target_environment: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    if not isinstance(x_callback_url, Unset):
        headers["X-Callback-Url"] = x_callback_url

    headers["X-Reference-Id"] = x_reference_id

    headers["X-Target-Environment"] = x_target_environment

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1_0/requesttopay",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorReason | None:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 409:
        response_409 = ErrorReason.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = ErrorReason.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorReason]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RequestToPay | Unset = UNSET,
    authorization: str,
    x_callback_url: str | Unset = UNSET,
    x_reference_id: str,
    x_target_environment: str,
) -> Response[Any | ErrorReason]:
    r"""RequesttoPay

     This operation is used to request a payment from a consumer (Payer). The payer will be asked to
    authorize the payment. The transaction will be executed once the payer has authorized the payment.
    The requesttopay will be in status PENDING until the transaction is authorized or declined by the
    payer or it is timed out by the system.
     Status of the transaction can be validated by using the GET /requesttopay/\<resourceId\>

    Args:
        authorization (str):
        x_callback_url (str | Unset):
        x_reference_id (str):
        x_target_environment (str):
        body (RequestToPay | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorReason]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_callback_url=x_callback_url,
        x_reference_id=x_reference_id,
        x_target_environment=x_target_environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RequestToPay | Unset = UNSET,
    authorization: str,
    x_callback_url: str | Unset = UNSET,
    x_reference_id: str,
    x_target_environment: str,
) -> Any | ErrorReason | None:
    r"""RequesttoPay

     This operation is used to request a payment from a consumer (Payer). The payer will be asked to
    authorize the payment. The transaction will be executed once the payer has authorized the payment.
    The requesttopay will be in status PENDING until the transaction is authorized or declined by the
    payer or it is timed out by the system.
     Status of the transaction can be validated by using the GET /requesttopay/\<resourceId\>

    Args:
        authorization (str):
        x_callback_url (str | Unset):
        x_reference_id (str):
        x_target_environment (str):
        body (RequestToPay | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorReason
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
        x_callback_url=x_callback_url,
        x_reference_id=x_reference_id,
        x_target_environment=x_target_environment,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RequestToPay | Unset = UNSET,
    authorization: str,
    x_callback_url: str | Unset = UNSET,
    x_reference_id: str,
    x_target_environment: str,
) -> Response[Any | ErrorReason]:
    r"""RequesttoPay

     This operation is used to request a payment from a consumer (Payer). The payer will be asked to
    authorize the payment. The transaction will be executed once the payer has authorized the payment.
    The requesttopay will be in status PENDING until the transaction is authorized or declined by the
    payer or it is timed out by the system.
     Status of the transaction can be validated by using the GET /requesttopay/\<resourceId\>

    Args:
        authorization (str):
        x_callback_url (str | Unset):
        x_reference_id (str):
        x_target_environment (str):
        body (RequestToPay | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorReason]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_callback_url=x_callback_url,
        x_reference_id=x_reference_id,
        x_target_environment=x_target_environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RequestToPay | Unset = UNSET,
    authorization: str,
    x_callback_url: str | Unset = UNSET,
    x_reference_id: str,
    x_target_environment: str,
) -> Any | ErrorReason | None:
    r"""RequesttoPay

     This operation is used to request a payment from a consumer (Payer). The payer will be asked to
    authorize the payment. The transaction will be executed once the payer has authorized the payment.
    The requesttopay will be in status PENDING until the transaction is authorized or declined by the
    payer or it is timed out by the system.
     Status of the transaction can be validated by using the GET /requesttopay/\<resourceId\>

    Args:
        authorization (str):
        x_callback_url (str | Unset):
        x_reference_id (str):
        x_target_environment (str):
        body (RequestToPay | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorReason
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
            x_callback_url=x_callback_url,
            x_reference_id=x_reference_id,
            x_target_environment=x_target_environment,
        )
    ).parsed
