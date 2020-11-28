# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.


var_1 = 'test'

print(var_1)

var_2 = True

print(var_2)

var_3 = 123455

print(var_1, var_2, var_3)
print(type(var_1), type(var_2), type(var_3))

var_1 = input('Введите число/строку: ')

if not var_1.isdigit():
    print(f'Строка: {var_1}')
else:
    print(f'число: {int(var_1)}')

var_1 = input('Введите число/строку: ')

if not var_1.isnumeric():
    print(f'Строка: {var_1}')
else:
    print(f'число: {int(var_1)}')
