# 3 Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным
# и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных
# данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    name = ""
    surname = ""
    position = ""
    _income = dict()

    def __init__(self, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


a = Position(20, 30)
a.name = "Leo"
a.surname = "Servion"

b = Position(110, 30)
b.name = "Seo"
b.surname = "Tervion"

print(a.get_full_name())
print(a.get_total_income())
print(b.get_full_name())
print(b.get_total_income())
