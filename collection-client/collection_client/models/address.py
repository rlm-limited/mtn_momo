from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """
    Attributes:
        formatted (str | Unset): Full mailing address, formatted for display or use on a mailing label. This field may
            contain multiple lines, separated by newlines.
        street_address (str | Unset): Full street address component, which may include house number, street name, Post
            Office Box, and multi-line extended street address information.
        locality (str | Unset): City or locality component.
        region (str | Unset): State, province, prefecture, or region component.
        postal_code (str | Unset): Zip code or postal code component.
        country (str | Unset): Country name component.
    """

    formatted: str | Unset = UNSET
    street_address: str | Unset = UNSET
    locality: str | Unset = UNSET
    region: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    country: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        formatted = self.formatted

        street_address = self.street_address

        locality = self.locality

        region = self.region

        postal_code = self.postal_code

        country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if formatted is not UNSET:
            field_dict["formatted"] = formatted
        if street_address is not UNSET:
            field_dict["street_address"] = street_address
        if locality is not UNSET:
            field_dict["locality"] = locality
        if region is not UNSET:
            field_dict["region"] = region
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        formatted = d.pop("formatted", UNSET)

        street_address = d.pop("street_address", UNSET)

        locality = d.pop("locality", UNSET)

        region = d.pop("region", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        country = d.pop("country", UNSET)

        address = cls(
            formatted=formatted,
            street_address=street_address,
            locality=locality,
            region=region,
            postal_code=postal_code,
            country=country,
        )

        address.additional_properties = d
        return address

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
