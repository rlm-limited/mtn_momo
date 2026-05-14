__version__ = "1.1.1"
"""A client library for accessing Collection"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
