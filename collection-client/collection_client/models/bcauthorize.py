from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bcauthorize_access_type import BcauthorizeAccessType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Bcauthorize")


@_attrs_define
class Bcauthorize:
    """
    Attributes:
        scope (str | Unset): Space separated list of scopes.
        login_hint (str | Unset): The identity of the account holder.
        access_type (BcauthorizeAccessType | Unset): Value either online, or offline.
        consent_valid_in (int | Unset): The validity time of the consent in secondsThis parameter can only be used
            together with access type offline.
        client_notification_token (str | Unset): This token is required when the client is using Ping or Push mode.
        scope_instruction (str | Unset): Base64 encoded Instrcution of the financial transaction.
    """

    scope: str | Unset = UNSET
    login_hint: str | Unset = UNSET
    access_type: BcauthorizeAccessType | Unset = UNSET
    consent_valid_in: int | Unset = UNSET
    client_notification_token: str | Unset = UNSET
    scope_instruction: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope = self.scope

        login_hint = self.login_hint

        access_type: str | Unset = UNSET
        if not isinstance(self.access_type, Unset):
            access_type = self.access_type.value

        consent_valid_in = self.consent_valid_in

        client_notification_token = self.client_notification_token

        scope_instruction = self.scope_instruction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if login_hint is not UNSET:
            field_dict["login_hint"] = login_hint
        if access_type is not UNSET:
            field_dict["access_type"] = access_type
        if consent_valid_in is not UNSET:
            field_dict["consent_valid_in"] = consent_valid_in
        if client_notification_token is not UNSET:
            field_dict["client_notification_token"] = client_notification_token
        if scope_instruction is not UNSET:
            field_dict["scope_instruction"] = scope_instruction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scope = d.pop("scope", UNSET)

        login_hint = d.pop("login_hint", UNSET)

        _access_type = d.pop("access_type", UNSET)
        access_type: BcauthorizeAccessType | Unset
        if isinstance(_access_type, Unset):
            access_type = UNSET
        else:
            access_type = BcauthorizeAccessType(_access_type)

        consent_valid_in = d.pop("consent_valid_in", UNSET)

        client_notification_token = d.pop("client_notification_token", UNSET)

        scope_instruction = d.pop("scope_instruction", UNSET)

        bcauthorize = cls(
            scope=scope,
            login_hint=login_hint,
            access_type=access_type,
            consent_valid_in=consent_valid_in,
            client_notification_token=client_notification_token,
            scope_instruction=scope_instruction,
        )

        bcauthorize.additional_properties = d
        return bcauthorize

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
