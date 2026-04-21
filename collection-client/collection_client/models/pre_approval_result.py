from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pre_approval_result_status import PreApprovalResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_reason import ErrorReason
    from ..models.party import Party


T = TypeVar("T", bound="PreApprovalResult")


@_attrs_define
class PreApprovalResult:
    """
    Attributes:
        payer (Party | Unset): Party identifies a account holder in the wallet platform. Party consists of two
            parameters, type and partyId. Each type have its own validation of the partyId<br> MSISDN - Mobile Number
            validated according to ITU-T E.164. Validated with IsMSISDN<br> EMAIL - Validated to be a valid e-mail format.
            Validated with IsEmail<br> PARTY_CODE - UUID of the party. Validated with IsUuid
        payer_currency (str | Unset): ISO4217 Currency
        payer_message (str | Unset): The mesage that is shown to the approver.
        status (PreApprovalResultStatus | Unset):
        expiration_date_time (int | Unset): The expiry date +time of the preapproval, in YYYY-MM-DDTHH:mm:SS format
        reason (ErrorReason | Unset):
    """

    payer: Party | Unset = UNSET
    payer_currency: str | Unset = UNSET
    payer_message: str | Unset = UNSET
    status: PreApprovalResultStatus | Unset = UNSET
    expiration_date_time: int | Unset = UNSET
    reason: ErrorReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payer, Unset):
            payer = self.payer.to_dict()

        payer_currency = self.payer_currency

        payer_message = self.payer_message

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        expiration_date_time = self.expiration_date_time

        reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payer is not UNSET:
            field_dict["payer"] = payer
        if payer_currency is not UNSET:
            field_dict["payerCurrency"] = payer_currency
        if payer_message is not UNSET:
            field_dict["payerMessage"] = payer_message
        if status is not UNSET:
            field_dict["status"] = status
        if expiration_date_time is not UNSET:
            field_dict["expirationDateTime"] = expiration_date_time
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_reason import ErrorReason
        from ..models.party import Party

        d = dict(src_dict)
        _payer = d.pop("payer", UNSET)
        payer: Party | Unset
        if isinstance(_payer, Unset):
            payer = UNSET
        else:
            payer = Party.from_dict(_payer)

        payer_currency = d.pop("payerCurrency", UNSET)

        payer_message = d.pop("payerMessage", UNSET)

        _status = d.pop("status", UNSET)
        status: PreApprovalResultStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PreApprovalResultStatus(_status)

        expiration_date_time = d.pop("expirationDateTime", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: ErrorReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ErrorReason.from_dict(_reason)

        pre_approval_result = cls(
            payer=payer,
            payer_currency=payer_currency,
            payer_message=payer_message,
            status=status,
            expiration_date_time=expiration_date_time,
            reason=reason,
        )

        pre_approval_result.additional_properties = d
        return pre_approval_result

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
