from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BasicUserInfoJsonResponse")


@_attrs_define
class BasicUserInfoJsonResponse:
    """
    Attributes:
        given_name (str | Unset): Given name(s) or first name(s) of the End-User. Note that in some cultures, people can
            have multiple given names; all can be present, with the names being separated by space characters.
        family_name (str | Unset): Surname(s) or last name(s) of the End-User. Note that in some cultures, people can
            have multiple family names or no family name; all can be present, with the names being separated by space
            characters.
        birthdate (str | Unset): Account holder birth date.
        locale (str | Unset): End-User's locale, represented as a  BCP47 [RFC5646] language tag. This is typically an
            ISO 639-1 Alpha-2 [ISO639�|�1] language code in lowercase and an  ISO 3166-1 Alpha-2 [ISO3166�|�1] country code
            in uppercase, separated by a dash. For example,  en-US or  fr-CA. As a compatibility note, some implementations
            have used an underscore as the separator rather than a dash, for example,  en_US; Relying Parties may choose to
            accept this locale syntax as well.
        gender (str | Unset): End-User's gender. Values defined by this specification are female and male. Other values
            may be used when neither of the defined values are applicable.
        status (str | Unset): Accountholder status.
    """

    given_name: str | Unset = UNSET
    family_name: str | Unset = UNSET
    birthdate: str | Unset = UNSET
    locale: str | Unset = UNSET
    gender: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        given_name = self.given_name

        family_name = self.family_name

        birthdate = self.birthdate

        locale = self.locale

        gender = self.gender

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if given_name is not UNSET:
            field_dict["given_name"] = given_name
        if family_name is not UNSET:
            field_dict["family_name"] = family_name
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if locale is not UNSET:
            field_dict["locale"] = locale
        if gender is not UNSET:
            field_dict["gender"] = gender
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        given_name = d.pop("given_name", UNSET)

        family_name = d.pop("family_name", UNSET)

        birthdate = d.pop("birthdate", UNSET)

        locale = d.pop("locale", UNSET)

        gender = d.pop("gender", UNSET)

        status = d.pop("status", UNSET)

        basic_user_info_json_response = cls(
            given_name=given_name,
            family_name=family_name,
            birthdate=birthdate,
            locale=locale,
            gender=gender,
            status=status,
        )

        basic_user_info_json_response.additional_properties = d
        return basic_user_info_json_response

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
