from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.party import Party


T = TypeVar("T", bound="CreateInvoice")


@_attrs_define
class CreateInvoice:
    """
    Attributes:
        external_id (str | Unset): External id is used as a reference to the transaction. External id is used for
            reconciliation. The external id will be included in transaction history report. <br>External id is not required
            to be unique.
        amount (str | Unset): Amount that will be debited from the payer account.
        currency (str | Unset): ISO4217 Currency
        validity_duration (str | Unset): ValidityTime - The duration that the invoice is valid in seconds.
        intended_payer (Party | Unset): Party identifies a account holder in the wallet platform. Party consists of two
            parameters, type and partyId. Each type have its own validation of the partyId<br> MSISDN - Mobile Number
            validated according to ITU-T E.164. Validated with IsMSISDN<br> EMAIL - Validated to be a valid e-mail format.
            Validated with IsEmail<br> PARTY_CODE - UUID of the party. Validated with IsUuid
        payee (Party | Unset): Party identifies a account holder in the wallet platform. Party consists of two
            parameters, type and partyId. Each type have its own validation of the partyId<br> MSISDN - Mobile Number
            validated according to ITU-T E.164. Validated with IsMSISDN<br> EMAIL - Validated to be a valid e-mail format.
            Validated with IsEmail<br> PARTY_CODE - UUID of the party. Validated with IsUuid
        description (str | Unset): Message that will be written in the payer transaction history message field.
    """

    external_id: str | Unset = UNSET
    amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    validity_duration: str | Unset = UNSET
    intended_payer: Party | Unset = UNSET
    payee: Party | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        amount = self.amount

        currency = self.currency

        validity_duration = self.validity_duration

        intended_payer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.intended_payer, Unset):
            intended_payer = self.intended_payer.to_dict()

        payee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payee, Unset):
            payee = self.payee.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if validity_duration is not UNSET:
            field_dict["validityDuration"] = validity_duration
        if intended_payer is not UNSET:
            field_dict["intendedPayer"] = intended_payer
        if payee is not UNSET:
            field_dict["payee"] = payee
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.party import Party

        d = dict(src_dict)
        external_id = d.pop("externalId", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        validity_duration = d.pop("validityDuration", UNSET)

        _intended_payer = d.pop("intendedPayer", UNSET)
        intended_payer: Party | Unset
        if isinstance(_intended_payer, Unset):
            intended_payer = UNSET
        else:
            intended_payer = Party.from_dict(_intended_payer)

        _payee = d.pop("payee", UNSET)
        payee: Party | Unset
        if isinstance(_payee, Unset):
            payee = UNSET
        else:
            payee = Party.from_dict(_payee)

        description = d.pop("description", UNSET)

        create_invoice = cls(
            external_id=external_id,
            amount=amount,
            currency=currency,
            validity_duration=validity_duration,
            intended_payer=intended_payer,
            payee=payee,
            description=description,
        )

        create_invoice.additional_properties = d
        return create_invoice

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
