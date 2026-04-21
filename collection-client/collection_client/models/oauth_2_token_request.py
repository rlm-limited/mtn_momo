from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Oauth2TokenRequest")


@_attrs_define
class Oauth2TokenRequest:
    """
    Attributes:
        grant_type (str | Unset): Value can be either "urn:openid:params:grant-type:ciba" or "refresh_token"
        auth_req_id (str | Unset): Authentication request ID.Value is only mandatory if grant_type is
            "urn:openid:params:grant-type:ciba"
        refresh_token (str | Unset): UUID.Refresh token retrieved from oauth2 token endpoint for consents with
            grant_type offline. This parameter is only valid if grant_type is refresh_token.
    """

    grant_type: str | Unset = UNSET
    auth_req_id: str | Unset = UNSET
    refresh_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type

        auth_req_id = self.auth_req_id

        refresh_token = self.refresh_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grant_type is not UNSET:
            field_dict["grant_type"] = grant_type
        if auth_req_id is not UNSET:
            field_dict["auth_req_id"] = auth_req_id
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = d.pop("grant_type", UNSET)

        auth_req_id = d.pop("auth_req_id", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        oauth_2_token_request = cls(
            grant_type=grant_type,
            auth_req_id=auth_req_id,
            refresh_token=refresh_token,
        )

        oauth_2_token_request.additional_properties = d
        return oauth_2_token_request

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
