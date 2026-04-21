from enum import Enum


class GetBasicUserinfoAccountHolderIdType(str, Enum):
    ALIAS = "Alias"
    EMAIL = "Email"
    ID = "ID"
    MSISDN = "MSISDN"

    def __str__(self) -> str:
        return str(self.value)
