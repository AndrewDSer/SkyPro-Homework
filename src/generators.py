

def filter_by_currency(transactions, currency="USD"):
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction
        else:
            yield


def transaction_descriptions(transactions):
    for transaction in transactions:
        if transaction.get("description") == "":
            yield "Описание транзакции или транзакция отсутствует"
        else:
            yield transaction.get("description")


def card_number_generator(start, end):
    for num in range(start, end):
        num_str = str(num)
        correct_card_num = 16 - len(num_str)
        generate_card_number = "0" * correct_card_num + num_str
        yield (f"{generate_card_number}"[:4] + " " + f"{generate_card_number}"[4:8] + " "
               + f"{generate_card_number}"[8:12] + " " + f"{generate_card_number}"[12:16])
