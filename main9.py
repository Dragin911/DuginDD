from typing import List, Any


def remove(lst: List[Any], value: Any) -> List[Any]:
    # Ищем индекс последнего вхождения элемента
    try:
        last_index = len(lst) - 1 - lst[::-1].index(value)
        lst.pop(last_index)  # Удаляем элемент по найденному индексу
    except ValueError:
        raise ValueError("Значение не найдено в списке.")

    return lst


# Примеры использования
print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]