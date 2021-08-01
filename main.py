print('Задача 6. Метеостанция')

# Для удобства работы сотрудников международной метеостанции
# каждый день нужно распечатывать различные таблицы
# соответствия градусов по шкале Цельсия и Фаренгейта.
#
# Напишите программу,
# которая принимает на вход три целых числа
# в градусах Цельсия: нижняя граница температуры, верхняя граница температуры и шаг.
#
# Программа выводит на экран
# таблицу соответствия градусов Цельсия градусам Фаренгейта
# от нижней до верхней границы с указанным шагом.
#
# Обеспечьте контроль ввода.
# Верхняя граница должна печататься, даже если последний шаг “перепрыгнул “ ее.
# Известно, что 0С соответствует 32F,
# а каждый градус Цельсия эквивалентен 1.8 градусам Фаренгейта.
#
# Пример:
#
# Ввод:
# Нижняя граница: 0
# Верхняя граница: 50
# Шаг: 20
#
# Вывод:
# C        F

# 0        32
# 20       68
# 40       104
# 50       122

hight_line = int(input('Введите верхнюю границу: '))
low_line = int(input('Введите нижнюю границу: '))
step = int(input('Введтие шаг: '))

for i in range(low_line, hight_line+1, step):
	print(i)