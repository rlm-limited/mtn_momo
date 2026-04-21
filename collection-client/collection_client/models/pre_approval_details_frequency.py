from enum import Enum


class PreApprovalDetailsFrequency(str, Enum):
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    WEEKLY = "WEEKLY"

    def __str__(self) -> str:
        return str(self.value)
