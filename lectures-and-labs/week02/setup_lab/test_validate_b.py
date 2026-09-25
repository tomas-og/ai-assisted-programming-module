from validate_b import validate_email


def test_validate_email_accepts_normal_address() -> None:
    assert validate_email("student@example.com") is True


def test_validate_email_rejects_address_without_dot() -> None:
    assert validate_email("student@example") is False


def test_validate_email_rejects_address_without_local_part() -> None:
    assert validate_email("@example.com") is False


def test_validate_email_rejects_300_character_address() -> None:
    address = "a" * 288 + "@example.com"

    assert len(address) == 300
    assert validate_email(address) is False
