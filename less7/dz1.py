# 1 Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
from itertools import zip_longest


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return f"Матрица: {' '.join((str(x) for x in self.lists))}"

    def __add__(self, other):
        temp_add_list = []
        for x, y in zip_longest(self.lists, other.lists, fillvalue=0):
            temp_ls = []
            for x_1, y_1 in zip_longest(x, y, fillvalue=0):
                temp_ls.append(x_1 + y_1)

            temp_add_list.append(temp_ls)
        return temp_add_list;


lst = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

print('Печать ', Matrix(lst))

lst1 = [[1, 1, 1], [5, 5, 5]]
tt1 = Matrix(lst1)
lst2 = [[2, 2, 2], [2, 2, 2]]
tt2 = Matrix(lst2)

print(tt1, tt2, 'Сложение трехмерных матриц', tt1 + tt2)

m_2_2 = [[1, 1], [5, 5]]
m_3_2 = [[2, 2, 2], [2, 2, 2]]
matr_2 = Matrix(m_2_2)
matr_3 = Matrix(m_3_2)

print('Сложение разных матриц: ', matr_2, matr_3, 'Result: ', matr_2 + matr_3)
