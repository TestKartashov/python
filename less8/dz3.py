# 3 Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел. Проверить работу
# исключения на реальном примере. Необходимо запрашивать у пользователя
# данные и заполнять список только числами. Класс-исключение должен
# контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например,
# команду “stop”. При этом скрипт завершается, сформированный список
# с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить
# только числа и строки. При вводе пользователем очередного элемента необходимо
# реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
import re


class Number(Exception):
    def __init__(self, txt):
        self.txt = txt


list_number = []
while True:
    try:
        n = input("Введите число или stop для остановки: ")
        if n == "stop":
            break
        if not bool(re.match('^[1234567890.]+$', n)):
            raise Number("Ввели не число")
        list_number.append(float(n))

    except Number as t:
        print(t)

print("Что ввели:", list_number)
