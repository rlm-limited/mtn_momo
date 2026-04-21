from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pre_approval_details_frequency import PreApprovalDetailsFrequency
from ..models.pre_approval_details_status import PreApprovalDetailsStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PreApprovalDetails")


@_attrs_define
class PreApprovalDetails:
    """
    Example:
        {'preApprovalId': 'string', 'toFri': 'string', 'fromFri': 'string', 'fromCurrency': 'string', 'createdTime':
            'string', 'approvedTime': 'string', 'expiryTime': 'string', 'status': 'string', 'message': 'string',
            'frequency': 'string', 'startDate': 'string', 'lastUsedDate': 'string', 'offer': 'string', 'externalId':
            'string', 'maxDebitAmount': 'string'}

    Attributes:
        pre_approval_id (str): The ID of the pre-approval. Parameter cannot be NULL.
        to_fri (str): The Financial Resource Identifier of the receiving account.
        from_fri (str): The Financial Resource Identifier of the sending account.
        from_currency (str): The currency of the account holder from where the debit happens. ISO4217 Currency
        created_time (str): The date and time at which the pre-approval was created. Validated with IsIso8601DateTime.
            Parameter can not be NULL
        status (PreApprovalDetailsStatus):
        message (str): Message. Validated with IsRestirctedString. Parameter can not be NULL.
        approved_time (str | Unset): The date and time at which the pre-approval was approved. Validated with
            IsIso8601DateTime. Parameter can not be NULL.
        expiry_time (str | Unset): The date and time at which the pre-approval expires. Validated with
            IsIso8601DateTime. Parameter can not be NULL.
        frequency (PreApprovalDetailsFrequency | Unset):
        start_date (str | Unset): The start date of the pre-approval. Validated with IsDateString. Parameter can not be
            NULL.
        last_used_date (str | Unset): The date pre-approval was used last. Validated with IsIso8601DateTime. Parameter
            can not be NULL.
        offer (str | Unset): The offer description. Validated with IsRestrictedString. Parameter can not be NULL.
        external_id (str | Unset): The external reference id. Validated with IsExternalReferenceString. Parameter can
            not be NULL.
        max_debit_amount (str | Unset): The max debit amount allowed. Contains a non-negative amount. Validated with
            IsAmount.
    """

    pre_approval_id: str
    to_fri: str
    from_fri: str
    from_currency: str
    created_time: str
    status: PreApprovalDetailsStatus
    message: str
    approved_time: str | Unset = UNSET
    expiry_time: str | Unset = UNSET
    frequency: PreApprovalDetailsFrequency | Unset = UNSET
    start_date: str | Unset = UNSET
    last_used_date: str | Unset = UNSET
    offer: str | Unset = UNSET
    external_id: str | Unset = UNSET
    max_debit_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pre_approval_id = self.pre_approval_id

        to_fri = self.to_fri

        from_fri = self.from_fri

        from_currency = self.from_currency

        created_time = self.created_time

        status = self.status.value

        message = self.message

        approved_time = self.approved_time

        expiry_time = self.expiry_time

        frequency: str | Unset = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

        start_date = self.start_date

        last_used_date = self.last_used_date

        offer = self.offer

        external_id = self.external_id

        max_debit_amount = self.max_debit_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "preApprovalId": pre_approval_id,
                "toFri": to_fri,
                "fromFri": from_fri,
                "fromCurrency": from_currency,
                "createdTime": created_time,
                "status": status,
                "message": message,
            }
        )
        if approved_time is not UNSET:
            field_dict["approvedTime"] = approved_time
        if expiry_time is not UNSET:
            field_dict["expiryTime"] = expiry_time
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if last_used_date is not UNSET:
            field_dict["lastUsedDate"] = last_used_date
        if offer is not UNSET:
            field_dict["offer"] = offer
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if max_debit_amount is not UNSET:
            field_dict["maxDebitAmount"] = max_debit_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pre_approval_id = d.pop("preApprovalId")

        to_fri = d.pop("toFri")

        from_fri = d.pop("fromFri")

        from_currency = d.pop("fromCurrency")

        created_time = d.pop("createdTime")

        status = PreApprovalDetailsStatus(d.pop("status"))

        message = d.pop("message")

        approved_time = d.pop("approvedTime", UNSET)

        expiry_time = d.pop("expiryTime", UNSET)

        _frequency = d.pop("frequency", UNSET)
        frequency: PreApprovalDetailsFrequency | Unset
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = PreApprovalDetailsFrequency(_frequency)

        start_date = d.pop("startDate", UNSET)

        last_used_date = d.pop("lastUsedDate", UNSET)

        offer = d.pop("offer", UNSET)

        external_id = d.pop("externalId", UNSET)

        max_debit_amount = d.pop("maxDebitAmount", UNSET)

        pre_approval_details = cls(
            pre_approval_id=pre_approval_id,
            to_fri=to_fri,
            from_fri=from_fri,
            from_currency=from_currency,
            created_time=created_time,
            status=status,
            message=message,
            approved_time=approved_time,
            expiry_time=expiry_time,
            frequency=frequency,
            start_date=start_date,
            last_used_date=last_used_date,
            offer=offer,
            external_id=external_id,
            max_debit_amount=max_debit_amount,
        )

        pre_approval_details.additional_properties = d
        return pre_approval_details

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
