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
        if TrafficLight.__color == "Красный":
            TrafficLight.__color = "Желтый"
        elif TrafficLight.__color == "Желтый":
            TrafficLight.__color = "Зеленый"
        else:
            TrafficLight.__color = "Красный"

    def __period(self):
        self.check_color()
        return TrafficLight.__color

    def running(self):
        while True:
            print(self.__period())
            sleep(7)
            print(self.__period())
            sleep(2)
            print(self.__period())
            sleep(7)


a = TrafficLight()
a.running()