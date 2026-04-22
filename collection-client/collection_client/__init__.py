__version__ = "0.1.0"
"""A client library for accessing Collection"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
