import random


def generate_three_digit_number():
    # Генерируем три случайные цифры от 0 до 9
    digit1 = random.randint(0, 9)
    digit2 = random.randint(0, 9)
    digit3 = random.randint(0, 9)

    # Формируем трехзначное число
    three_digit_number = f"{digit1}{digit2}{digit3}"

    return three_digit_number


# Пример использования функции
if __name__ == "__main__":
    result = generate_three_digit_number()
    print("Сгенерированное трехзначное число:", result