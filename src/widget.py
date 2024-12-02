

def mask_account_card(card_account: str) -> str:
    """Функция макскирующая номер карты или счета"""
    numbers_in_account = "0123456789"
    card_number = ""
    account_type = "Счет"
    account_number = ""
    correct_account_type = ""
    correct_card_type = ""
    result = ""

    # Действия если пользователь ввел номер счета
    for letters_account in card_account:
        if letters_account in account_type:
            correct_account_type = correct_account_type + letters_account
        elif letters_account in numbers_in_account:
            account_number = account_number + letters_account

    # Действия если пользователь ввел номер карты
    for card_type in card_account:
        if card_type not in numbers_in_account:
            correct_card_type = correct_card_type + card_type
        else:
            card_number = card_number + card_type

    # Реализация маскировки номера карты
    masked_card_number = f"{card_number[:6]}******{card_number[12:]}"
    formated_mask_card_number = ' '.join([masked_card_number[i:i + 4] for i in range(0, len(masked_card_number), 4)])

    # Реализация маскировки номера счета
    masked_account_number = f"**{account_number[16:]}"

    if correct_account_type == "Счет":
        result = f"{account_type} {masked_account_number}"
    else:
        result = f"{correct_card_type} {formated_mask_card_number}"
    return result


def get_date(date: str) -> str:
    """Функция которая приводит полученную дату к формату ДД.ММ.ГГГГ"""
    formated_date = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    return formated_date
