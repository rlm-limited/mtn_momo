from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_invoice_body import CancelInvoiceBody
from ...models.cancel_invoice_response_200 import CancelInvoiceResponse200
from ...models.error_reason import ErrorReason
from ...types import UNSET, Response, Unset


def _get_kwargs(
    reference_id: str,
    *,
    body: CancelInvoiceBody | Unset = UNSET,
    authorization: str,
    x_target_environment: str,
    x_reference_id: str,
    x_callback_url: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    headers["X-Target-Environment"] = x_target_environment

    headers["X-Reference-Id"] = x_reference_id

    if not isinstance(x_callback_url, Unset):
        headers["X-Callback-Url"] = x_callback_url

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v2_0/invoice/{reference_id}".format(
            reference_id=quote(str(reference_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CancelInvoiceResponse200 | ErrorReason | None:
    if response.status_code == 200:
        response_200 = CancelInvoiceResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorReason.from_dict(response.json())

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
) -> Response[CancelInvoiceResponse200 | ErrorReason]:
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
    body: CancelInvoiceBody | Unset = UNSET,
    authorization: str,
    x_target_environment: str,
    x_reference_id: str,
    x_callback_url: str | Unset = UNSET,
) -> Response[CancelInvoiceResponse200 | ErrorReason]:
    """CancelInvoice

     This operation is used to delete an invoice. The ReferenceId is associated with the invoice to be
    cancelled

    Args:
        reference_id (str):
        authorization (str):
        x_target_environment (str):
        x_reference_id (str):
        x_callback_url (str | Unset):
        body (CancelInvoiceBody | Unset):  Example: {'externalId': 'string'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelInvoiceResponse200 | ErrorReason]
    """

    kwargs = _get_kwargs(
        reference_id=reference_id,
        body=body,
        authorization=authorization,
        x_target_environment=x_target_environment,
        x_reference_id=x_reference_id,
        x_callback_url=x_callback_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    reference_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CancelInvoiceBody | Unset = UNSET,
    authorization: str,
    x_target_environment: str,
    x_reference_id: str,
    x_callback_url: str | Unset = UNSET,
) -> CancelInvoiceResponse200 | ErrorReason | None:
    """CancelInvoice

     This operation is used to delete an invoice. The ReferenceId is associated with the invoice to be
    cancelled

    Args:
        reference_id (str):
        authorization (str):
        x_target_environment (str):
        x_reference_id (str):
        x_callback_url (str | Unset):
        body (CancelInvoiceBody | Unset):  Example: {'externalId': 'string'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelInvoiceResponse200 | ErrorReason
    """

    return sync_detailed(
        reference_id=reference_id,
        client=client,
        body=body,
        authorization=authorization,
        x_target_environment=x_target_environment,
        x_reference_id=x_reference_id,
        x_callback_url=x_callback_url,
    ).parsed


async def asyncio_detailed(
    reference_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CancelInvoiceBody | Unset = UNSET,
    authorization: str,
    x_target_environment: str,
    x_reference_id: str,
    x_callback_url: str | Unset = UNSET,
) -> Response[CancelInvoiceResponse200 | ErrorReason]:
    """CancelInvoice

     This operation is used to delete an invoice. The ReferenceId is associated with the invoice to be
    cancelled

    Args:
        reference_id (str):
        authorization (str):
        x_target_environment (str):
        x_reference_id (str):
        x_callback_url (str | Unset):
        body (CancelInvoiceBody | Unset):  Example: {'externalId': 'string'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelInvoiceResponse200 | ErrorReason]
    """

    kwargs = _get_kwargs(
        reference_id=reference_id,
        body=body,
        authorization=authorization,
        x_target_environment=x_target_environment,
        x_reference_id=x_reference_id,
        x_callback_url=x_callback_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reference_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CancelInvoiceBody | Unset = UNSET,
    authorization: str,
    x_target_environment: str,
    x_reference_id: str,
    x_callback_url: str | Unset = UNSET,
) -> CancelInvoiceResponse200 | ErrorReason | None:
    """CancelInvoice

     This operation is used to delete an invoice. The ReferenceId is associated with the invoice to be
    cancelled

    Args:
        reference_id (str):
        authorization (str):
        x_target_environment (str):
        x_reference_id (str):
        x_callback_url (str | Unset):
        body (CancelInvoiceBody | Unset):  Example: {'externalId': 'string'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelInvoiceResponse200 | ErrorReason
    """

    return (
        await asyncio_detailed(
            reference_id=reference_id,
            client=client,
            body=body,
            authorization=authorization,
            x_target_environment=x_target_environment,
            x_reference_id=x_reference_id,
            x_callback_url=x_callback_url,
        )
    ).parsed
