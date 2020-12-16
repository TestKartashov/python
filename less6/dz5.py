# 5 Реализовать класс Stationery (канцелярская принадлежность). Определить в
# нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
# “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    title = ""

    def draw(self):
        print(f"{Stationery.title} Запуск отрисовки.")


class Pen(Stationery):

    def draw(self):
        print(f"{self.title} Запуск отрисовки. Pen")


class Pencil(Stationery):

    def draw(self):
        print(f"{self.title} Запуск отрисовки. Pencil")


class Handle(Stationery):

    def draw(self):
        print(f"{self.title} Запуск отрисовки. Handle")


Stationery = Stationery()
Stationery.title = "Stationery"
Stationery.draw()

Pen = Pen()
Pen.title = "Pen"
Pen.draw()

Pencil = Pencil()
Pencil.title = "Pencil"
Pencil.draw()

Handle = Handle()
Handle.title = "Handle"
Handle.draw()
