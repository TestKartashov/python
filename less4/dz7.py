# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение
# факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from functools import reduce


def my_f(prev_el, el):
    return prev_el * el


def fact(n):
    '''Для каждого с 1! и до n!'''
    for i in range(1, (n + 1)):
        '''Формирование генератора с указанием какой факториал равен чему'''
        yield {F"{i}!": reduce(my_f, [el for el in range(1, (i + 1))])}


for el in fact(4):
    print(el)
