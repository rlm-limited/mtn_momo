from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsentkycResponse")


@_attrs_define
class ConsentkycResponse:
    """
    Attributes:
        sub (str | Unset): Subject - Identifier for the End-User at the Issuer.
        name (str | Unset): End-User's full name in displayable form including all name parts.
        given_name (str | Unset): Given name(s) or first name(s) of the End-User.
        family_name (str | Unset): Surname(s) or last name(s) of the End-User.
        middle_name (str | Unset): Middle name(s) of the End-User.
        email (str | Unset): End-User's preferred e-mail address. Its value MUST conform to the  RFC 5322 [RFC5322]
            address specification syntax.
        email_verified (bool | Unset): The response value is True if the End-User's e-mail address has been
            verified;otherwise false.
        gender (str | Unset): End-User's gender.
        locale (str | Unset): Preffered language.
        phone_number (str | Unset): End-User's preferred telephone number
        phone_number_verified (bool | Unset): The response value is True if the End-User's phone number has been
            verified; otherwise false.
        address (str | Unset): User Address
        updated_at (float | Unset): The time the End-User's information was last updated.
        status (str | Unset): Account holder status.
        birthdate (str | Unset): The birth date of the account holder.
        credit_score (str | Unset): The credit score of the account holder.
        active (bool | Unset): The status of the account holder.
        country_of_birth (str | Unset): Account holder country of birth.
        region_of_birth (str | Unset): The birth region of the account holder.
        city_of_birth (str | Unset): The city of birth for the account holder.
        occupation (str | Unset): Occupation of the account holder.
        employer_name (str | Unset): The name of the employer.
        identification_type (str | Unset): Type of identification.The first non-expired identification is always chosen.
        identification_value (str | Unset): The value of the identification.
    """

    sub: str | Unset = UNSET
    name: str | Unset = UNSET
    given_name: str | Unset = UNSET
    family_name: str | Unset = UNSET
    middle_name: str | Unset = UNSET
    email: str | Unset = UNSET
    email_verified: bool | Unset = UNSET
    gender: str | Unset = UNSET
    locale: str | Unset = UNSET
    phone_number: str | Unset = UNSET
    phone_number_verified: bool | Unset = UNSET
    address: str | Unset = UNSET
    updated_at: float | Unset = UNSET
    status: str | Unset = UNSET
    birthdate: str | Unset = UNSET
    credit_score: str | Unset = UNSET
    active: bool | Unset = UNSET
    country_of_birth: str | Unset = UNSET
    region_of_birth: str | Unset = UNSET
    city_of_birth: str | Unset = UNSET
    occupation: str | Unset = UNSET
    employer_name: str | Unset = UNSET
    identification_type: str | Unset = UNSET
    identification_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sub = self.sub

        name = self.name

        given_name = self.given_name

        family_name = self.family_name

        middle_name = self.middle_name

        email = self.email

        email_verified = self.email_verified

        gender = self.gender

        locale = self.locale

        phone_number = self.phone_number

        phone_number_verified = self.phone_number_verified

        address = self.address

        updated_at = self.updated_at

        status = self.status

        birthdate = self.birthdate

        credit_score = self.credit_score

        active = self.active

        country_of_birth = self.country_of_birth

        region_of_birth = self.region_of_birth

        city_of_birth = self.city_of_birth

        occupation = self.occupation

        employer_name = self.employer_name

        identification_type = self.identification_type

        identification_value = self.identification_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub is not UNSET:
            field_dict["sub"] = sub
        if name is not UNSET:
            field_dict["name"] = name
        if given_name is not UNSET:
            field_dict["given_name"] = given_name
        if family_name is not UNSET:
            field_dict["family_name"] = family_name
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if email is not UNSET:
            field_dict["email"] = email
        if email_verified is not UNSET:
            field_dict["email_verified"] = email_verified
        if gender is not UNSET:
            field_dict["gender"] = gender
        if locale is not UNSET:
            field_dict["locale"] = locale
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if phone_number_verified is not UNSET:
            field_dict["phone_number_verified"] = phone_number_verified
        if address is not UNSET:
            field_dict["address"] = address
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if status is not UNSET:
            field_dict["status"] = status
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if credit_score is not UNSET:
            field_dict["credit_score"] = credit_score
        if active is not UNSET:
            field_dict["active"] = active
        if country_of_birth is not UNSET:
            field_dict["country_of_birth"] = country_of_birth
        if region_of_birth is not UNSET:
            field_dict["region_of_birth"] = region_of_birth
        if city_of_birth is not UNSET:
            field_dict["city_of_birth"] = city_of_birth
        if occupation is not UNSET:
            field_dict["occupation"] = occupation
        if employer_name is not UNSET:
            field_dict["employer_name"] = employer_name
        if identification_type is not UNSET:
            field_dict["identification_type"] = identification_type
        if identification_value is not UNSET:
            field_dict["identification_value"] = identification_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sub = d.pop("sub", UNSET)

        name = d.pop("name", UNSET)

        given_name = d.pop("given_name", UNSET)

        family_name = d.pop("family_name", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        email = d.pop("email", UNSET)

        email_verified = d.pop("email_verified", UNSET)

        gender = d.pop("gender", UNSET)

        locale = d.pop("locale", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        phone_number_verified = d.pop("phone_number_verified", UNSET)

        address = d.pop("address", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        status = d.pop("status", UNSET)

        birthdate = d.pop("birthdate", UNSET)

        credit_score = d.pop("credit_score", UNSET)

        active = d.pop("active", UNSET)

        country_of_birth = d.pop("country_of_birth", UNSET)

        region_of_birth = d.pop("region_of_birth", UNSET)

        city_of_birth = d.pop("city_of_birth", UNSET)

        occupation = d.pop("occupation", UNSET)

        employer_name = d.pop("employer_name", UNSET)

        identification_type = d.pop("identification_type", UNSET)

        identification_value = d.pop("identification_value", UNSET)

        consentkyc_response = cls(
            sub=sub,
            name=name,
            given_name=given_name,
            family_name=family_name,
            middle_name=middle_name,
            email=email,
            email_verified=email_verified,
            gender=gender,
            locale=locale,
            phone_number=phone_number,
            phone_number_verified=phone_number_verified,
            address=address,
            updated_at=updated_at,
            status=status,
            birthdate=birthdate,
            credit_score=credit_score,
            active=active,
            country_of_birth=country_of_birth,
            region_of_birth=region_of_birth,
            city_of_birth=city_of_birth,
            occupation=occupation,
            employer_name=employer_name,
            identification_type=identification_type,
            identification_value=identification_value,
        )

        consentkyc_response.additional_properties = d
        return consentkyc_response

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
