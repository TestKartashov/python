# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
# желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) —
# 2 секунды, третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться
# только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.
from time import sleep


class TrafficLight:
    __color = None

    def check_color(self):
        if self.__color == "Красный":
            self.__color = "Желтый"
        elif self.__color == "Желтый":
            self.__color = "Зеленый"
        else:
            self.__color = "Красный"

    def __period(self):
        self.check_color()
        print(self.__color)
        sleep(7)
        self.check_color()
        print(self.__color)
        sleep(2)
        self.check_color()
        print(self.__color)
        sleep(7)

    def running(self):
        while True:
            self.__period()


a = TrafficLight()
a.running()
