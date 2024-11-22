def find_item_index(items, item_to_find):
    try:
        # Используем метод index, который возвращает индекс первого вхождения элемента
        return items.index(item_to_find)
    except ValueError:
        # Если элемент не найден, ловим исключение и возвращаем None
        return None

# Список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Перечень товаров, которые нужно найти
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # Вызов функции для получения индекса товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")