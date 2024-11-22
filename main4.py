def find_common_participants(group1, group2, separator=','):
    # Разбиваем строки на списки фамилий
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)
    
    # Находим общие фамилии с помощью множества
    common_participants = set(participants1).intersection(set(participants2))
    
    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)

# Примеры использования функции
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Поиск общих участников с разделителем '|'
common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print("Общие участники (разделитель '|'):", common_participants)

# Проверка работы функции с разделителем запятая
participants_first_group_comma = "Иванов,Петров,Сидоров"
participants_second_group_comma = "Петров,Сидоров,Смирнов"
common_participants_comma = find_common_participants(participants_first_group_comma, participants_second_group_comma)
print("Общие участники (разделитель ','):", common_participants_comma)