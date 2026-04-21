from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.party_party_id_type import PartyPartyIdType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Party")


@_attrs_define
class Party:
    """Party identifies a account holder in the wallet platform. Party consists of two parameters, type and partyId. Each
    type have its own validation of the partyId<br> MSISDN - Mobile Number validated according to ITU-T E.164. Validated
    with IsMSISDN<br> EMAIL - Validated to be a valid e-mail format. Validated with IsEmail<br> PARTY_CODE - UUID of the
    party. Validated with IsUuid

        Attributes:
            party_id_type (PartyPartyIdType | Unset):
            party_id (str | Unset):
    """

    party_id_type: PartyPartyIdType | Unset = UNSET
    party_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        party_id_type: str | Unset = UNSET
        if not isinstance(self.party_id_type, Unset):
            party_id_type = self.party_id_type.value

        party_id = self.party_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if party_id_type is not UNSET:
            field_dict["partyIdType"] = party_id_type
        if party_id is not UNSET:
            field_dict["partyId"] = party_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _party_id_type = d.pop("partyIdType", UNSET)
        party_id_type: PartyPartyIdType | Unset
        if isinstance(_party_id_type, Unset):
            party_id_type = UNSET
        else:
            party_id_type = PartyPartyIdType(_party_id_type)

        party_id = d.pop("partyId", UNSET)

        party = cls(
            party_id_type=party_id_type,
            party_id=party_id,
        )

        party.additional_properties = d
        return party

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
