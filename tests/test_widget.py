
from src.widget import mask_account_card, get_date


def test_mask_account_card(card_account):
    assert mask_account_card(card_account) == "Visa Platinum  7000 79** **** 6361"


def test_get_date(date):
    assert get_date(date) == "11.03.2024"
