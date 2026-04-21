from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_result_status import PaymentResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_reason import ErrorReason


T = TypeVar("T", bound="PaymentResult")


@_attrs_define
class PaymentResult:
    """
    Attributes:
        reference_id (str | Unset): The reference id for this Payment.
        status (PaymentResultStatus | Unset):
        financial_transaction_id (str | Unset): A transaction id associated with this payment.
        reason (ErrorReason | Unset):
    """

    reference_id: str | Unset = UNSET
    status: PaymentResultStatus | Unset = UNSET
    financial_transaction_id: str | Unset = UNSET
    reason: ErrorReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_id = self.reference_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        financial_transaction_id = self.financial_transaction_id

        reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if status is not UNSET:
            field_dict["status"] = status
        if financial_transaction_id is not UNSET:
            field_dict["financialTransactionId"] = financial_transaction_id
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_reason import ErrorReason

        d = dict(src_dict)
        reference_id = d.pop("referenceId", UNSET)

        _status = d.pop("status", UNSET)
        status: PaymentResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PaymentResultStatus(_status)

        financial_transaction_id = d.pop("financialTransactionId", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: ErrorReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ErrorReason.from_dict(_reason)

        payment_result = cls(
            reference_id=reference_id,
            status=status,
            financial_transaction_id=financial_transaction_id,
            reason=reason,
        )

        payment_result.additional_properties = d
        return payment_result

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
