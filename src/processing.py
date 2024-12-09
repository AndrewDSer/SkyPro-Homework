

def filter_by_state(list_of_dictionary: list, user_state: str = "EXECUTED") -> list:
    """Функция выводящая список словарей с указанным значением для ключа state (по умолчанию значени EXECUTED)"""
    new_list_dictionary = []
    for dic in list_of_dictionary:
        if dic.get("state") == user_state:
            new_list_dictionary.append(dic)
    return new_list_dictionary


def sort_by_date(list_of_dates: list, is_decreasing: bool = True) -> list:
    """Функция сортирующая список словарей по дате (по убыванию или по увеличению)
    по умолчанию сортирует по убыванию)"""
    return sorted(list_of_dates, key=lambda date_sorted: date_sorted["date"], reverse=is_decreasing)
