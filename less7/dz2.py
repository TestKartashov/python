# 2 Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте
# относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу
# этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
# этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class clothes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass


class suit(clothes):

    def __init__(self, size):
        self.size = size

    @property
    def fabric_consumption(self):
        return 2 * self.size + 0.2


class coat(clothes):

    def __init__(self, size):
        self.size = size

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


t = suit(2)
print(t.fabric_consumption)
t = coat(2)
print(t.fabric_consumption)
