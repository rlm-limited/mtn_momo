from enum import Enum


class RequestToPayResultStatus(str, Enum):
    FAILED = "FAILED"
    PENDING = "PENDING"
    SUCCESSFUL = "SUCCESSFUL"

    def __str__(self) -> str:
        return str(self.value)
