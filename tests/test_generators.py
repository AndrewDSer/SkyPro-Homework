import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions_list):
    result = filter_by_currency(transactions_list)
    empty_list = filter_by_currency([{}])
    assert next(result) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert next(result) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    assert next(result) == None
    assert next(empty_list) == None


def test_transaction_descriptions(transactions_list):
    result = transaction_descriptions(transactions_list)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод с карты на карту"
    assert next(result) == "Перевод организации"
    assert next(transaction_descriptions([{}])) == None


@pytest.mark.parametrize("start, end, expected", [
    (1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002",
            "0000 0000 0000 0003", "0000 0000 0000 0004", "0000 0000 0000 0005"]),
    (10, 15, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012",
              "0000 0000 0000 0013", "0000 0000 0000 0014", "0000 0000 0000 0015"]),
    (999, 1001, ["0000 0000 0000 0999", "0000 0000 0000 1000", "0000 0000 0000 1001"]),
])
def test_card_number_generator(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected
