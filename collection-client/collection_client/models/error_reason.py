from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_reason_code import ErrorReasonCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorReason")


@_attrs_define
class ErrorReason:
    """
    Attributes:
        code (ErrorReasonCode | Unset):
        message (str | Unset):
    """

    code: ErrorReasonCode | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code: str | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _code = d.pop("code", UNSET)
        code: ErrorReasonCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = ErrorReasonCode(_code)

        message = d.pop("message", UNSET)

        error_reason = cls(
            code=code,
            message=message,
        )

        error_reason.additional_properties = d
        return error_reason

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
