from enum import Enum


class BcAuthorizeBodyAccessType(str, Enum):
    OFFLINE = "offline"
    ONLINE = "online"

    def __str__(self) -> str:
        return str(self.value)
