# todo Реализовать функцию my_func(),
# todo которая принимает три позиционных аргумента, и
# todo возвращает сумму наибольших двух аргументов.

def my_max(var_1, var_2, var_3):
    ret_1 = var_1
    ret_2 = var_2

    if ret_1 < var_3:
        ret_1 = var_3
        if ret_2 < var_1:
            ret_2 = var_1
    else:
        if ret_2 < var_3:
            ret_2 = var_3

    return ret_1 + ret_2


print(my_max(1, 8, 2))

print(my_max(1, 2, 8))

print(my_max(8, 1, 2))

print(my_max(8, 2, 1))

print(my_max(2, 1, 8))

print(my_max(2, 8, 1))




