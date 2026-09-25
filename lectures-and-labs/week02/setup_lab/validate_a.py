"""A conservative validator for ordinary email addresses."""
from __future__ import annotations

import re


_LOCAL_PART = re.compile(r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+")
_DOMAIN_LABEL = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?")
_MAX_ADDRESS_LENGTH = 254


def validate_email(address: str) -> bool:
    """Return whether *address* has a valid ordinary email shape."""
    if not isinstance(address, str) or len(address) > _MAX_ADDRESS_LENGTH:
        return False

    local_part, separator, domain = address.rpartition("@")
    if not separator or not local_part or len(local_part) > 64:
        return False
    if local_part.startswith(".") or local_part.endswith(".") or ".." in local_part:
        return False
    if not _LOCAL_PART.fullmatch(local_part):
        return False

    labels = domain.split(".")
    return len(labels) >= 2 and all(_DOMAIN_LABEL.fullmatch(label) for label in labels)
