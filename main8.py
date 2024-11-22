import random
import string


def get_random_password(n=8) -> str:
    # Определяем алфавит для пароля
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits

    # Генерируем пароль с помощью sample
    password = ''.join(random.sample(alphabet, n))

    return password


# Пример использования
print(get_random_password())