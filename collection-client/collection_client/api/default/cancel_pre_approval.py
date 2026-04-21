from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_reason import ErrorReason
from ...types import Response


def _get_kwargs(
    preapprovalid: str,
    *,
    authorization: str,
    x_target_environment: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    headers["X-Target-Environment"] = x_target_environment

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1_0/preapproval/{preapprovalid}".format(
            preapprovalid=quote(str(preapprovalid), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorReason | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

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
    preapprovalid: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Response[Any | ErrorReason]:
    """CancelPreApproval

     This operation is used to cancel a pre-approval. It is possible to cancel only that preapproval
    which is in approved state and the requesting Account Holder (Service Provider or Merchant) is the
    payee

    Args:
        preapprovalid (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorReason]
    """

    kwargs = _get_kwargs(
        preapprovalid=preapprovalid,
        authorization=authorization,
        x_target_environment=x_target_environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    preapprovalid: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Any | ErrorReason | None:
    """CancelPreApproval

     This operation is used to cancel a pre-approval. It is possible to cancel only that preapproval
    which is in approved state and the requesting Account Holder (Service Provider or Merchant) is the
    payee

    Args:
        preapprovalid (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorReason
    """

    return sync_detailed(
        preapprovalid=preapprovalid,
        client=client,
        authorization=authorization,
        x_target_environment=x_target_environment,
    ).parsed


async def asyncio_detailed(
    preapprovalid: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Response[Any | ErrorReason]:
    """CancelPreApproval

     This operation is used to cancel a pre-approval. It is possible to cancel only that preapproval
    which is in approved state and the requesting Account Holder (Service Provider or Merchant) is the
    payee

    Args:
        preapprovalid (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorReason]
    """

    kwargs = _get_kwargs(
        preapprovalid=preapprovalid,
        authorization=authorization,
        x_target_environment=x_target_environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    preapprovalid: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Any | ErrorReason | None:
    """CancelPreApproval

     This operation is used to cancel a pre-approval. It is possible to cancel only that preapproval
    which is in approved state and the requesting Account Holder (Service Provider or Merchant) is the
    payee

    Args:
        preapprovalid (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorReason
    """

    return (
        await asyncio_detailed(
            preapprovalid=preapprovalid,
            client=client,
            authorization=authorization,
            x_target_environment=x_target_environment,
        )
    ).parsed
