from enum import Enum


class GetApprovedPreApprovalsAccountHolderIdType(str, Enum):
    ALIAS = "alias"
    EMAIL = "email"
    ID = "id"
    MSISDN = "msisdn"

    def __str__(self) -> str:
        return str(self.value)
