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
    speed: float
    color: str
    name: str
    is_police = False
    msg = ""

    def go(self):
        self.msg = "Auto"
        if self.is_police:
            self.msg = "Auto Police"
        print(f"{self.name} {self.msg} Go")

    def stop(self):
        print(f"{self.name} {self.msg} Stop")

    def turn(self, direction):
        print(f"{self.name} {self.msg} turn {direction}")

    def show_speed(self):
        print(f"{self.msg} Speed {self.speed}")


class TownCar(Car):
    _stop_speed = 60

    def show_speed(self):
        if self.speed > self._stop_speed:
            print(f"{self.name} {self.msg} Alarm Speed > {self._stop_speed}: {self.speed}")
        else:
            print(f"{self.name} {self.msg} Speed > 60: {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    _stop_speed = 40

    def show_speed(self):
        if self.speed > self._stop_speed:
            print(f"{self.name} {self.msg} Alarm Speed > {self._stop_speed}: {self.speed}")
        else:
            print(f"{self.name} {self.msg} Speed: {self.speed}")


class PoliceCar(Car):

    def __init__(self):
        self.is_police = True


print('----------------')
TownCar = TownCar()
TownCar.speed = 100
TownCar.name = "TownCar"
TownCar.color = "blue"
TownCar.go()
for i in range(10):
    TownCar.speed -= i * 2
    TownCar.show_speed()
TownCar.stop()
print('----------------')
WorkCar = WorkCar()
WorkCar.speed = 50
WorkCar.name = "WorkCar"
WorkCar.color = "red"
WorkCar.go()
for i in range(5):
    WorkCar.speed -= i * 2
    WorkCar.show_speed()

WorkCar.stop()
print('----------------')
PoliceCar = PoliceCar()
PoliceCar.speed = 150
PoliceCar.name = "PoliceCar"
PoliceCar.color = "red"
PoliceCar.go()
for i in range(5):
    PoliceCar.speed -= i * 2
    PoliceCar.show_speed()

PoliceCar.stop()
print('----------------')
SportCar = SportCar()
SportCar.speed = 150
SportCar.name = "SportCar"
SportCar.color = "red"
SportCar.go()
for i in range(5):
    SportCar.speed -= i * 2
    SportCar.show_speed()

SportCar.stop()
