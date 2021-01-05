# Реализовать класс «Дата», функция-конструктор которого
# должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
import datetime
import re


class Data:
    @classmethod
    def ret_number(cls, stroka):

        if not bool(re.match('^[1234567890-]+$', stroka)):
            raise Exception("Содержит символы")
        dat = stroka.split("-")

        return [int(dat[0]), int(dat[1]), int(dat[2])]

    @staticmethod
    def valid_num(stroka):
        try:

            dat = Data.ret_number(stroka)
            t = datetime.date(dat[2], dat[1], dat[0])
        except Exception as e:
            print(e)
            return False
        else:
            return True


print(Data.ret_number("01-12-2020"))

print(Data.valid_num("01-1d2-2020"))

print(Data.valid_num("01-122-2020"))

print(bool(re.match('^[1234567890-]+$', "01-12-2020")))
