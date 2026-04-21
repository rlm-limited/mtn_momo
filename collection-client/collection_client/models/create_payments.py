from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="CreatePayments")


@_attrs_define
class CreatePayments:
    """
    Attributes:
        external_transaction_id (str | Unset): An external transaction id to tie to the payment.
        money (Money | Unset):
        customer_reference (str | Unset): A customer reference for a provider. Example: +46070911111
        service_provider_user_name (str | Unset): A service provider name. Example: Electricity Inc.
        coupon_id (str | Unset): A coupon the user would like to redeem and use the reward as part of this payment.
        product_id (str | Unset): Optional id of a product, used if paying for a product.
        product_offering_id (str | Unset): Optional id of a product offering, used when paying for a particular offering
            of a product.
        receiver_message (str | Unset): A descriptive note for receiver transaction history.
        sender_note (str | Unset): A descriptive note for sender transaction history.
        max_number_of_retries (int | Unset): maxNumberOfRetries
        include_sender_charges (bool | Unset): Specifies if sender charges, this is, fee and tax paid by the sender,
            should be included in the specified transaction amount. This means that the charges will be deducted from the
            transaction amount before the remaining amount is transferred to the receiver.True indicates that charges shall
            be included in the specified transaction amount. The default value is false, meaning that sender charges are
            charged on top of the transaction amount.
    """

    external_transaction_id: str | Unset = UNSET
    money: Money | Unset = UNSET
    customer_reference: str | Unset = UNSET
    service_provider_user_name: str | Unset = UNSET
    coupon_id: str | Unset = UNSET
    product_id: str | Unset = UNSET
    product_offering_id: str | Unset = UNSET
    receiver_message: str | Unset = UNSET
    sender_note: str | Unset = UNSET
    max_number_of_retries: int | Unset = UNSET
    include_sender_charges: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_transaction_id = self.external_transaction_id

        money: dict[str, Any] | Unset = UNSET
        if not isinstance(self.money, Unset):
            money = self.money.to_dict()

        customer_reference = self.customer_reference

        service_provider_user_name = self.service_provider_user_name

        coupon_id = self.coupon_id

        product_id = self.product_id

        product_offering_id = self.product_offering_id

        receiver_message = self.receiver_message

        sender_note = self.sender_note

        max_number_of_retries = self.max_number_of_retries

        include_sender_charges = self.include_sender_charges

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_transaction_id is not UNSET:
            field_dict["externalTransactionId"] = external_transaction_id
        if money is not UNSET:
            field_dict["money"] = money
        if customer_reference is not UNSET:
            field_dict["customerReference"] = customer_reference
        if service_provider_user_name is not UNSET:
            field_dict["serviceProviderUserName"] = service_provider_user_name
        if coupon_id is not UNSET:
            field_dict["couponId"] = coupon_id
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if product_offering_id is not UNSET:
            field_dict["productOfferingId"] = product_offering_id
        if receiver_message is not UNSET:
            field_dict["receiverMessage"] = receiver_message
        if sender_note is not UNSET:
            field_dict["senderNote"] = sender_note
        if max_number_of_retries is not UNSET:
            field_dict["maxNumberOfRetries"] = max_number_of_retries
        if include_sender_charges is not UNSET:
            field_dict["includeSenderCharges"] = include_sender_charges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.money import Money

        d = dict(src_dict)
        external_transaction_id = d.pop("externalTransactionId", UNSET)

        _money = d.pop("money", UNSET)
        money: Money | Unset
        if isinstance(_money, Unset):
            money = UNSET
        else:
            money = Money.from_dict(_money)

        customer_reference = d.pop("customerReference", UNSET)

        service_provider_user_name = d.pop("serviceProviderUserName", UNSET)

        coupon_id = d.pop("couponId", UNSET)

        product_id = d.pop("productId", UNSET)

        product_offering_id = d.pop("productOfferingId", UNSET)

        receiver_message = d.pop("receiverMessage", UNSET)

        sender_note = d.pop("senderNote", UNSET)

        max_number_of_retries = d.pop("maxNumberOfRetries", UNSET)

        include_sender_charges = d.pop("includeSenderCharges", UNSET)

        create_payments = cls(
            external_transaction_id=external_transaction_id,
            money=money,
            customer_reference=customer_reference,
            service_provider_user_name=service_provider_user_name,
            coupon_id=coupon_id,
            product_id=product_id,
            product_offering_id=product_offering_id,
            receiver_message=receiver_message,
            sender_note=sender_note,
            max_number_of_retries=max_number_of_retries,
            include_sender_charges=include_sender_charges,
        )

        create_payments.additional_properties = d
        return create_payments

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
