

def filter_by_state(list_of_dictionaries: list, user_state: str = "EXECUTED") -> list:
    """Функция получающая на вход список словарей и дополнительный параметр(по умолчанию EXECUTED). Функция возвращает
    список с теми словарями
    в которых значение ключа state равнялось заданному параметру (по умолчанию значение EXECUTED)"""
    new_list_of_dictionaries = []
    for dic in list_of_dictionaries:
        if dic.get("state") == user_state:
            new_list_of_dictionaries.append(dic)
    return new_list_of_dictionaries


def sort_by_date(list_of_dates: list, is_decreasing: bool = True) -> list:
    """Функция получающая на вход список словарей и дополнительный параметр представляющий собой булевую переменную.
    Функция сортирует список по датам (ключ "date")
    и возвращает новый список словарей
    с отсортированными по убыванию или возрастанию датами (По умолчанию сортирует по убыванию)"""
    return sorted(list_of_dates, key=lambda date_sorted: date_sorted["date"], reverse=is_decreasing)
