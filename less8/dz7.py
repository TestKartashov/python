# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class complex_number:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.i = "i"

    def __add__(self, other):
        b = (self.b + other.b)
        a = (self.a + other.a)

        p = ("+ " if b >= 0 else "-")

        return f"{a} {p} {abs(b)}i"


    def __mul__(self, other):
        a = (self.a * other.a) - (self.b * other.b)
        b = (self.a * other.b) + (self.b * other.a)

        p = ("+ " if b >= 0 else "-")

        return f"{a} {p} {abs(b)}i"


a = complex_number(-3, 5)
b = complex_number(4, -8)

print(a + b)

a = complex_number(2, 0)
b = complex_number(7, 0)

print(a + b)

a = complex_number(-2, 3)
b = complex_number(-2, -3)

print(a + b)

a = complex_number(2, 3)
b = complex_number(5, 4)

print(a * b)
