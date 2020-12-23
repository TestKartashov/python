# 2 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class Zero(Exception):
    def __init__(self, txt):
        self.txt = txt


def calc(a: int, b: int):
    if not b:
        raise Zero('Ошибка Вы ввели 0')
    return a / b


try:
    t = input("Enter number: ")
    print(calc(100, int(t)))
except Zero as s:
    print("Error ",s)
