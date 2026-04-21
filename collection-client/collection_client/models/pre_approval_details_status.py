from enum import Enum


class PreApprovalDetailsStatus(str, Enum):
    APPROVED = "APPROVED"
    CANCELLED = "CANCELLED"
    EXPIRED = "EXPIRED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
