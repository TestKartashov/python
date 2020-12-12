# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

def my_max(var_1, var_2, var_3):
    l = [var_1, var_2, var_3]
    l.sort(key=lambda t: -t)
    return l[0] + l[1]


print(my_max(1, 8, 2))
