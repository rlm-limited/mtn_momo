from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_reason import ErrorReason
from ...models.get_approved_pre_approvals_account_holder_id_type import GetApprovedPreApprovalsAccountHolderIdType
from ...models.pre_approval_details import PreApprovalDetails
from ...types import Response


def _get_kwargs(
    account_holder_id_type: GetApprovedPreApprovalsAccountHolderIdType,
    account_holder_id: str,
    *,
    authorization: str,
    x_target_environment: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    headers["X-Target-Environment"] = x_target_environment

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1_0/preapprovals/{account_holder_id_type}/{account_holder_id}".format(
            account_holder_id_type=quote(str(account_holder_id_type), safe=""),
            account_holder_id=quote(str(account_holder_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorReason | list[PreApprovalDetails] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PreApprovalDetails.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorReason | list[PreApprovalDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_holder_id_type: GetApprovedPreApprovalsAccountHolderIdType,
    account_holder_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Response[Any | ErrorReason | list[PreApprovalDetails]]:
    """GetApprovedPreApprovals

     This operation is used to get approved pre-approvals of an account holder. Only those pre-approvals
    of account holder, where requesting Account Holder (Service Provider or Merchant) is the payee, are
    returned.

    Args:
        account_holder_id_type (GetApprovedPreApprovalsAccountHolderIdType):
        account_holder_id (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorReason | list[PreApprovalDetails]]
    """

    kwargs = _get_kwargs(
        account_holder_id_type=account_holder_id_type,
        account_holder_id=account_holder_id,
        authorization=authorization,
        x_target_environment=x_target_environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_holder_id_type: GetApprovedPreApprovalsAccountHolderIdType,
    account_holder_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Any | ErrorReason | list[PreApprovalDetails] | None:
    """GetApprovedPreApprovals

     This operation is used to get approved pre-approvals of an account holder. Only those pre-approvals
    of account holder, where requesting Account Holder (Service Provider or Merchant) is the payee, are
    returned.

    Args:
        account_holder_id_type (GetApprovedPreApprovalsAccountHolderIdType):
        account_holder_id (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorReason | list[PreApprovalDetails]
    """

    return sync_detailed(
        account_holder_id_type=account_holder_id_type,
        account_holder_id=account_holder_id,
        client=client,
        authorization=authorization,
        x_target_environment=x_target_environment,
    ).parsed


async def asyncio_detailed(
    account_holder_id_type: GetApprovedPreApprovalsAccountHolderIdType,
    account_holder_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Response[Any | ErrorReason | list[PreApprovalDetails]]:
    """GetApprovedPreApprovals

     This operation is used to get approved pre-approvals of an account holder. Only those pre-approvals
    of account holder, where requesting Account Holder (Service Provider or Merchant) is the payee, are
    returned.

    Args:
        account_holder_id_type (GetApprovedPreApprovalsAccountHolderIdType):
        account_holder_id (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorReason | list[PreApprovalDetails]]
    """

    kwargs = _get_kwargs(
        account_holder_id_type=account_holder_id_type,
        account_holder_id=account_holder_id,
        authorization=authorization,
        x_target_environment=x_target_environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_holder_id_type: GetApprovedPreApprovalsAccountHolderIdType,
    account_holder_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Any | ErrorReason | list[PreApprovalDetails] | None:
    """GetApprovedPreApprovals

     This operation is used to get approved pre-approvals of an account holder. Only those pre-approvals
    of account holder, where requesting Account Holder (Service Provider or Merchant) is the payee, are
    returned.

    Args:
        account_holder_id_type (GetApprovedPreApprovalsAccountHolderIdType):
        account_holder_id (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorReason | list[PreApprovalDetails]
    """

    return (
        await asyncio_detailed(
            account_holder_id_type=account_holder_id_type,
            account_holder_id=account_holder_id,
            client=client,
            authorization=authorization,
            x_target_environment=x_target_environment,
        )
    ).parsed
