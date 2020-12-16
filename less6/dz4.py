# 4 Реализуйте базовый класс Car. У данного класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed = float
    color = str
    name = str
    is_police = bool

    def go(self):
        print(f"{self.name} Go")

    def stop(self):
        print(f"{self.name} Stop")

    def turn(self, direction):
        print(f"{self.name} turn {direction}")

    def show_speed(self):
        print(Car.speed)


class TownCar(Car):

    def show_speed(self):
        if TownCar.speed > 60:
            print(f"{TownCar.name} Speed > 60: {TownCar.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if WorkCar.speed > 40:
            print(f"{TownCar.name} Speed > 40: {WorkCar.speed}")


class PoliceCar(Car):
    pass

TownCar = TownCar()
TownCar.speed = 100
TownCar.name = "TownCar"
TownCar.color = "blue"
TownCar.go()
TownCar.show_speed()
TownCar.stop()

WorkCar = WorkCar()
WorkCar.speed = 50
WorkCar.name = "WorkCar"
WorkCar.color = "red"
WorkCar.go()
WorkCar.show_speed()
WorkCar.stop()