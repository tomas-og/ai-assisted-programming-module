"""A deliberately simple email validator."""
from __future__ import annotations


def validate_email(address: str) -> bool:
    """Return whether *address* contains an @ and a later dot."""
    if not isinstance(address, str) or len(address) > 254:
        return False

    at_index = address.find("@")
    return at_index != -1 and "." in address[at_index + 1:]