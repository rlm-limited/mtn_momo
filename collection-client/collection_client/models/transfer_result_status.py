from enum import Enum


class TransferResultStatus(str, Enum):
    FAILED = "FAILED"
    PENDING = "PENDING"
    SUCCESSFUL = "SUCCESSFUL"

    def __str__(self) -> str:
        return str(self.value)
