from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deliverynotification import Deliverynotification
from ...types import UNSET, Response, Unset


def _get_kwargs(
    reference_id: str,
    *,
    body: Deliverynotification | Unset = UNSET,
    notification_message: str,
    language: str | Unset = UNSET,
    authorization: str,
    x_target_environment: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["notificationMessage"] = notification_message

    if not isinstance(language, Unset):
        headers["Language"] = language

    headers["Authorization"] = authorization

    headers["X-Target-Environment"] = x_target_environment

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1_0/requesttopay/{reference_id}/deliverynotification".format(
            reference_id=quote(str(reference_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 404:
        return None

    if response.status_code == 409:
        return None

    if response.status_code == 410:
        return None

    if response.status_code == 429:
        return None

    if response.status_code == 500:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
    body: Deliverynotification | Unset = UNSET,
    notification_message: str,
    language: str | Unset = UNSET,
    authorization: str,
    x_target_environment: str,
) -> Response[Any]:
    """RequesttoPayDeliveryNotification

     This operation is used to send additional Notification to an End User.

    Args:
        reference_id (str):
        notification_message (str):
        language (str | Unset):
        authorization (str):
        x_target_environment (str):
        body (Deliverynotification | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        reference_id=reference_id,
        body=body,
        notification_message=notification_message,
        language=language,
        authorization=authorization,
        x_target_environment=x_target_environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    reference_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Deliverynotification | Unset = UNSET,
    notification_message: str,
    language: str | Unset = UNSET,
    authorization: str,
    x_target_environment: str,
) -> Response[Any]:
    """RequesttoPayDeliveryNotification

     This operation is used to send additional Notification to an End User.

    Args:
        reference_id (str):
        notification_message (str):
        language (str | Unset):
        authorization (str):
        x_target_environment (str):
        body (Deliverynotification | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        reference_id=reference_id,
        body=body,
        notification_message=notification_message,
        language=language,
        authorization=authorization,
        x_target_environment=x_target_environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
