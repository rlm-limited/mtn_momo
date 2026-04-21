from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.basic_user_info_json_response import BasicUserInfoJsonResponse
from ...models.get_basic_userinfo_account_holder_id_type import GetBasicUserinfoAccountHolderIdType
from ...models.token_post_401_application_json_response import TokenPost401ApplicationJsonResponse
from ...types import Response


def _get_kwargs(
    account_holder_id_type: GetBasicUserinfoAccountHolderIdType,
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
        "url": "/v1_0/accountholder/{account_holder_id_type}/{account_holder_id}/basicuserinfo".format(
            account_holder_id_type=quote(str(account_holder_id_type), safe=""),
            account_holder_id=quote(str(account_holder_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BasicUserInfoJsonResponse | TokenPost401ApplicationJsonResponse | None:
    if response.status_code == 200:
        response_200 = BasicUserInfoJsonResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = TokenPost401ApplicationJsonResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BasicUserInfoJsonResponse | TokenPost401ApplicationJsonResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_holder_id_type: GetBasicUserinfoAccountHolderIdType,
    account_holder_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Response[Any | BasicUserInfoJsonResponse | TokenPost401ApplicationJsonResponse]:
    """GetBasicUserinfo

     This operation returns personal information of the account holder. The operation does not need any
    consent by the account holder.

    Args:
        account_holder_id_type (GetBasicUserinfoAccountHolderIdType):
        account_holder_id (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BasicUserInfoJsonResponse | TokenPost401ApplicationJsonResponse]
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
    account_holder_id_type: GetBasicUserinfoAccountHolderIdType,
    account_holder_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Any | BasicUserInfoJsonResponse | TokenPost401ApplicationJsonResponse | None:
    """GetBasicUserinfo

     This operation returns personal information of the account holder. The operation does not need any
    consent by the account holder.

    Args:
        account_holder_id_type (GetBasicUserinfoAccountHolderIdType):
        account_holder_id (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BasicUserInfoJsonResponse | TokenPost401ApplicationJsonResponse
    """

    return sync_detailed(
        account_holder_id_type=account_holder_id_type,
        account_holder_id=account_holder_id,
        client=client,
        authorization=authorization,
        x_target_environment=x_target_environment,
    ).parsed


async def asyncio_detailed(
    account_holder_id_type: GetBasicUserinfoAccountHolderIdType,
    account_holder_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Response[Any | BasicUserInfoJsonResponse | TokenPost401ApplicationJsonResponse]:
    """GetBasicUserinfo

     This operation returns personal information of the account holder. The operation does not need any
    consent by the account holder.

    Args:
        account_holder_id_type (GetBasicUserinfoAccountHolderIdType):
        account_holder_id (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BasicUserInfoJsonResponse | TokenPost401ApplicationJsonResponse]
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
    account_holder_id_type: GetBasicUserinfoAccountHolderIdType,
    account_holder_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
    x_target_environment: str,
) -> Any | BasicUserInfoJsonResponse | TokenPost401ApplicationJsonResponse | None:
    """GetBasicUserinfo

     This operation returns personal information of the account holder. The operation does not need any
    consent by the account holder.

    Args:
        account_holder_id_type (GetBasicUserinfoAccountHolderIdType):
        account_holder_id (str):
        authorization (str):
        x_target_environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BasicUserInfoJsonResponse | TokenPost401ApplicationJsonResponse
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
