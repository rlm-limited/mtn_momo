__version__ = "1.0.1"
"""A client library for accessing Collection"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
