from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.token_post_200_application_json_response import TokenPost200ApplicationJsonResponse
from ...models.token_post_401_application_json_response import TokenPost401ApplicationJsonResponse
from ...types import Response


def _get_kwargs(
    *,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/token/",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TokenPost200ApplicationJsonResponse | TokenPost401ApplicationJsonResponse | None:
    if response.status_code == 200:
        response_200 = TokenPost200ApplicationJsonResponse.from_dict(response.json())

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
) -> Response[Any | TokenPost200ApplicationJsonResponse | TokenPost401ApplicationJsonResponse]:
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
) -> Response[Any | TokenPost200ApplicationJsonResponse | TokenPost401ApplicationJsonResponse]:
    """CreateAccessToken

     This operation is used to create an access token which can then be used to authorize and
    authenticate towards the other end-points of the API.

    Args:
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TokenPost200ApplicationJsonResponse | TokenPost401ApplicationJsonResponse]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
) -> Any | TokenPost200ApplicationJsonResponse | TokenPost401ApplicationJsonResponse | None:
    """CreateAccessToken

     This operation is used to create an access token which can then be used to authorize and
    authenticate towards the other end-points of the API.

    Args:
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TokenPost200ApplicationJsonResponse | TokenPost401ApplicationJsonResponse
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
) -> Response[Any | TokenPost200ApplicationJsonResponse | TokenPost401ApplicationJsonResponse]:
    """CreateAccessToken

     This operation is used to create an access token which can then be used to authorize and
    authenticate towards the other end-points of the API.

    Args:
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TokenPost200ApplicationJsonResponse | TokenPost401ApplicationJsonResponse]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    authorization: str,
) -> Any | TokenPost200ApplicationJsonResponse | TokenPost401ApplicationJsonResponse | None:
    """CreateAccessToken

     This operation is used to create an access token which can then be used to authorize and
    authenticate towards the other end-points of the API.

    Args:
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TokenPost200ApplicationJsonResponse | TokenPost401ApplicationJsonResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
