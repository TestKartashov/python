# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
# подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

def my_while():
    num = 0

    def list_sum(var_str):
        try:
            lis = var_str.split(" ")
            nonlocal num
            for l in lis:
                if not l.isnumeric():
                    return 0
                i = int(l)
                num += i
            print("Сумма: ", num)

            return True
        except Exception as s:
            print(s)
            return False

    while True:
        num_text = input("Введите несколько чисел через пробел, для завершения введите любой символ или число с символом: ")
        if not list_sum(num_text):
            break

    print("Сумма: ", num)


my_while()
