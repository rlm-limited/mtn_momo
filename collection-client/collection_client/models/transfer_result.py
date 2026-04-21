from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transfer_result_status import TransferResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_reason import ErrorReason
    from ..models.party import Party


T = TypeVar("T", bound="TransferResult")


@_attrs_define
class TransferResult:
    """
    Attributes:
        amount (str | Unset): Amount that will be debited from the payer account.
        currency (str | Unset): ISO4217 Currency
        financial_transaction_id (str | Unset): Financial transactionIdd from mobile money manager.<br> Used to connect
            to the specific financial transaction made in the account
        external_id (str | Unset): External id is used as a reference to the transaction. External id is used for
            reconciliation. The external id will be included in transaction history report. <br>External id is not required
            to be unique.
        payee (Party | Unset): Party identifies a account holder in the wallet platform. Party consists of two
            parameters, type and partyId. Each type have its own validation of the partyId<br> MSISDN - Mobile Number
            validated according to ITU-T E.164. Validated with IsMSISDN<br> EMAIL - Validated to be a valid e-mail format.
            Validated with IsEmail<br> PARTY_CODE - UUID of the party. Validated with IsUuid
        payer_message (str | Unset): Message that will be written in the payer transaction history message field.
        payee_note (str | Unset): Message that will be written in the payee transaction history note field.
        status (TransferResultStatus | Unset):
        reason (ErrorReason | Unset):
    """

    amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    financial_transaction_id: str | Unset = UNSET
    external_id: str | Unset = UNSET
    payee: Party | Unset = UNSET
    payer_message: str | Unset = UNSET
    payee_note: str | Unset = UNSET
    status: TransferResultStatus | Unset = UNSET
    reason: ErrorReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency = self.currency

        financial_transaction_id = self.financial_transaction_id

        external_id = self.external_id

        payee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payee, Unset):
            payee = self.payee.to_dict()

        payer_message = self.payer_message

        payee_note = self.payee_note

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if financial_transaction_id is not UNSET:
            field_dict["financialTransactionId"] = financial_transaction_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if payee is not UNSET:
            field_dict["payee"] = payee
        if payer_message is not UNSET:
            field_dict["payerMessage"] = payer_message
        if payee_note is not UNSET:
            field_dict["payeeNote"] = payee_note
        if status is not UNSET:
            field_dict["status"] = status
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_reason import ErrorReason
        from ..models.party import Party

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        financial_transaction_id = d.pop("financialTransactionId", UNSET)

        external_id = d.pop("externalId", UNSET)

        _payee = d.pop("payee", UNSET)
        payee: Party | Unset
        if isinstance(_payee, Unset):
            payee = UNSET
        else:
            payee = Party.from_dict(_payee)

        payer_message = d.pop("payerMessage", UNSET)

        payee_note = d.pop("payeeNote", UNSET)

        _status = d.pop("status", UNSET)
        status: TransferResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TransferResultStatus(_status)

        _reason = d.pop("reason", UNSET)
        reason: ErrorReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ErrorReason.from_dict(_reason)

        transfer_result = cls(
            amount=amount,
            currency=currency,
            financial_transaction_id=financial_transaction_id,
            external_id=external_id,
            payee=payee,
            payer_message=payer_message,
            payee_note=payee_note,
            status=status,
            reason=reason,
        )

        transfer_result.additional_properties = d
        return transfer_result

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
