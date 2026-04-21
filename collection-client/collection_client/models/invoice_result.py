from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_result_status import InvoiceResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_reason import ErrorReason
    from ..models.party import Party


T = TypeVar("T", bound="InvoiceResult")


@_attrs_define
class InvoiceResult:
    """
    Attributes:
        reference_id (str | Unset): The reference id for this invoice.
        external_id (str | Unset): An external transaction id to tie to the payment.
        amount (str | Unset): A positive amount for this invoice.
        currency (str | Unset): ISO4217 Currency - The currency used in this invoice.
        status (InvoiceResultStatus | Unset):
        payment_reference (str | Unset): A unique id that identifies a pending invoice.
        invoice_id (str | Unset): An id for the invoice.
        expiry_date_time (str | Unset): DateTime for when invoice expires, in YYYY-MM-DD:THH:mm:ss format.
        payee_first_name (str | Unset): First name of the payee in this invoice.
        payee_last_name (str | Unset): Surname of the payee in this invoice
        error_reason (ErrorReason | Unset):
        intended_payer (Party | Unset): Party identifies a account holder in the wallet platform. Party consists of two
            parameters, type and partyId. Each type have its own validation of the partyId<br> MSISDN - Mobile Number
            validated according to ITU-T E.164. Validated with IsMSISDN<br> EMAIL - Validated to be a valid e-mail format.
            Validated with IsEmail<br> PARTY_CODE - UUID of the party. Validated with IsUuid
        description (str | Unset): An optional description of the invoice.
    """

    reference_id: str | Unset = UNSET
    external_id: str | Unset = UNSET
    amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    status: InvoiceResultStatus | Unset = UNSET
    payment_reference: str | Unset = UNSET
    invoice_id: str | Unset = UNSET
    expiry_date_time: str | Unset = UNSET
    payee_first_name: str | Unset = UNSET
    payee_last_name: str | Unset = UNSET
    error_reason: ErrorReason | Unset = UNSET
    intended_payer: Party | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_id = self.reference_id

        external_id = self.external_id

        amount = self.amount

        currency = self.currency

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        payment_reference = self.payment_reference

        invoice_id = self.invoice_id

        expiry_date_time = self.expiry_date_time

        payee_first_name = self.payee_first_name

        payee_last_name = self.payee_last_name

        error_reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_reason, Unset):
            error_reason = self.error_reason.to_dict()

        intended_payer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.intended_payer, Unset):
            intended_payer = self.intended_payer.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if status is not UNSET:
            field_dict["status"] = status
        if payment_reference is not UNSET:
            field_dict["paymentReference"] = payment_reference
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if expiry_date_time is not UNSET:
            field_dict["expiryDateTime"] = expiry_date_time
        if payee_first_name is not UNSET:
            field_dict["payeeFirstName"] = payee_first_name
        if payee_last_name is not UNSET:
            field_dict["payeeLastName"] = payee_last_name
        if error_reason is not UNSET:
            field_dict["errorReason"] = error_reason
        if intended_payer is not UNSET:
            field_dict["intendedPayer"] = intended_payer
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_reason import ErrorReason
        from ..models.party import Party

        d = dict(src_dict)
        reference_id = d.pop("referenceId", UNSET)

        external_id = d.pop("externalId", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        _status = d.pop("status", UNSET)
        status: InvoiceResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InvoiceResultStatus(_status)

        payment_reference = d.pop("paymentReference", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        expiry_date_time = d.pop("expiryDateTime", UNSET)

        payee_first_name = d.pop("payeeFirstName", UNSET)

        payee_last_name = d.pop("payeeLastName", UNSET)

        _error_reason = d.pop("errorReason", UNSET)
        error_reason: ErrorReason | Unset
        if isinstance(_error_reason, Unset):
            error_reason = UNSET
        else:
            error_reason = ErrorReason.from_dict(_error_reason)

        _intended_payer = d.pop("intendedPayer", UNSET)
        intended_payer: Party | Unset
        if isinstance(_intended_payer, Unset):
            intended_payer = UNSET
        else:
            intended_payer = Party.from_dict(_intended_payer)

        description = d.pop("description", UNSET)

        invoice_result = cls(
            reference_id=reference_id,
            external_id=external_id,
            amount=amount,
            currency=currency,
            status=status,
            payment_reference=payment_reference,
            invoice_id=invoice_id,
            expiry_date_time=expiry_date_time,
            payee_first_name=payee_first_name,
            payee_last_name=payee_last_name,
            error_reason=error_reason,
            intended_payer=intended_payer,
            description=description,
        )

        invoice_result.additional_properties = d
        return invoice_result

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
