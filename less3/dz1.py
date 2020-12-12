# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def del_num(var_1, var_2):
    '''
    Функция деления числа
    :param var_1:
    :param var_2:
    :return: Возвращает (Значение или Описание ошибки если есть)
    '''
    try:
        if var_2 == 0:
            raise ZeroDivisionError

        return var_1 / var_2, ''
    except ZeroDivisionError as ss:
        print("Деление на 0")


inp_1 = int(input("Enter number One: "))
inp_2 = int(input("Enter number Two: "))

print(del_num(inp_1, inp_2))
