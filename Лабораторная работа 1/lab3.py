list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2

# Распределяем игроков на две команды
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

# Распечатываем каждую команду на отдельной строке
print(first_team)
print(second_team)
