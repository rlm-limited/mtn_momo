from enum import Enum


class PreApprovalResultStatus(str, Enum):
    FAILED = "FAILED"
    PENDING = "PENDING"
    SUCCESSFUL = "SUCCESSFUL"

    def __str__(self) -> str:
        return str(self.value)
