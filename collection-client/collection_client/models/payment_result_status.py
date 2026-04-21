from enum import Enum


class PaymentResultStatus(str, Enum):
    CREATED = "CREATED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    SUCCESSFUL = "SUCCESSFUL"

    def __str__(self) -> str:
        return str(self.value)
