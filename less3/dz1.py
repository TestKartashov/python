# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def del_num(var_1, var_2):
    try:
        return var_1 / var_2, ''
    except ZeroDivisionError as err:
        return None, err


inp_1 = int(input("Enter number One: "))
inp_2 = int(input("Enter number Two: "))

print(del_num(inp_1, inp_2))
