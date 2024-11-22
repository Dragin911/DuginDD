from random import choice

EAGLE = "Орел"
TAILS = "Решка"

# Определяем монету
coin = [EAGLE, TAILS]
# Различное количество подбрасываний
counts = [10, 100, 1000, 100000, 1000000]
# Список для хранения относительных частот
list_freq = []

for count in counts:
    # Подбросим монету и посчитаем количество случаев
    eagle_count = sum(choice(coin) == EAGLE for _ in range(count))
    tails_count = count - eagle_count  # Если это не орел, то это решка

    # Вычисляем отношение меньшего к большему
    ratio = min(eagle_count, tails_count) / max(eagle_count, tails_count)
    list_freq.append(ratio)

# Выводим результаты
print(list_freq)