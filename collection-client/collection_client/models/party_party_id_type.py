from enum import Enum


class PartyPartyIdType(str, Enum):
    EMAIL = "EMAIL"
    MSISDN = "MSISDN"
    PARTY_CODE = "PARTY_CODE"

    def __str__(self) -> str:
        return str(self.value)
