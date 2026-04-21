from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenPost200ApplicationJsonResponse")


@_attrs_define
class TokenPost200ApplicationJsonResponse:
    """
    Attributes:
        access_token (str | Unset): A JWT token which can be used to authrize against the other API end-points. The
            format of the token follows the JWT standard format (see jwt.io for an example). This is the token that should
            be sent in in the Authorization header when calling the other API end-points.
        token_type (str | Unset): The token type.
        expires_in (int | Unset): The validity time in seconds of the token.
    """

    access_token: str | Unset = UNSET
    token_type: str | Unset = UNSET
    expires_in: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        token_type = self.token_type

        expires_in = self.expires_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token", UNSET)

        token_type = d.pop("token_type", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        token_post_200_application_json_response = cls(
            access_token=access_token,
            token_type=token_type,
            expires_in=expires_in,
        )

        token_post_200_application_json_response.additional_properties = d
        return token_post_200_application_json_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
