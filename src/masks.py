

def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    masked_number = f"{card_number[:6]}******{card_number[12:]}"
    formated_mask = ' '.join([masked_number[i:i+4] for i in range(0, len(masked_number), 4)])
    return formated_mask


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    masked_account = f"**{account_number[16:]}"
    return masked_account
