import pytest


@pytest.fixture
def card_number():
    return "4567890234567856"


@pytest.fixture
def account_number():
    return "34567291846572364752"


@pytest.fixture
def card_account():
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"
