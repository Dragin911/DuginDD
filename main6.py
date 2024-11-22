import random

def get_unique_list_numbers() -> list[int]:
    # Получаем все уникальные числа в диапазоне от -10 до 10
    possible_numbers = list(range(-10, 11))
    # Перемешиваем список
    random.shuffle(possible_numbers)
    # Берем первые 15 чисел
    unique_numbers = possible_numbers[:15]
    return unique_numbers

# Используем функцию
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
# Проверяем, все ли числа уникальны
print(len(list_unique_numbers) == len(set(list_unique_numbers)))