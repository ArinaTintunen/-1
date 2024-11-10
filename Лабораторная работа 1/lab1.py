numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

# Ищем сумму всех элементов, кроме None
sum_numbers = sum(num for num in numbers if num is not None)

# Ищем количество всех элементов в списке (включая None)
total_count = len(numbers)

# Количество элементов без None
count_without_none = total_count - numbers.count(None)

# Вычисляем среднее арифметическое
average = sum_numbers / count_without_none

# Заменяем None на среднее арифметическое
numbers = [average if num is None else num for num in numbers]

print("Измененный список:", numbers)
