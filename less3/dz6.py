# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое
# слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(stroka):
    return stroka.title()


print(int_func('text'))


def my_wh(var_1):
    lis = var_1.split(" ")
    res = ""
    for l in lis:
        """Первая проверка чтоб не проставлял пробел"""
        if res == "":
            res = int_func(l)
        else:
            res = f"{res} {int_func(l)}"

    return res


print(my_wh('text res man dan'))