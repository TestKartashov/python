# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать
# функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.
li = [1, 1.2, "ssssss", (1, 2, 3), [1, 3, 4], {1, 3, 4}]

for l in li:
    print(type(l))
