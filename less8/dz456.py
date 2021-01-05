# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных
# на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.
import re


class office_equipment:

    def __init__(self, size: int, type_name: str, serial_number: int):
        self.size = size
        self.type_name = type_name
        self.serial_number = serial_number


class printer(office_equipment):
    def __init__(self, size: int, type_name: str, list_number: int, speed_minute: int, serial_number: int):
        super().__init__(size, type_name, serial_number)
        self.list_number = list_number
        self.speed_minute = speed_minute


class scanner(office_equipment):
    def __init__(self, size: int, type_name: str, speed: int, serial_number: int):
        super().__init__(size, type_name, serial_number)
        self.speed = speed


class xerox(office_equipment):
    def __init__(self, size: int, speed_minute: int, type_name: str, list_number: int, speed: int, serial_number: int):
        super().__init__(size, type_name, serial_number)
        self.speed_minute = speed_minute
        self.list_number = list_number
        self.speed = speed


class warehouse:
    type_tex = [printer, scanner, xerox]

    def __init__(self):
        # [{'item': type_tex, 'warehouse': 0}]
        self.dict_warehouse = []

    def add_warehouse(self, item, count: int):
        try:
            if not bool(re.match('^[1234567890.]+$', str(count))):
                raise Exception("Указано не число")

            if item.__class__ in self.type_tex:
                temp = {'item': item, 'warehouse': count}
                self.dict_warehouse.append(temp)
                return "Ok"
            else:
                raise Exception("Типа товара нет на складе")
        except Exception as e:
            return repr(e)

    def __str__(self):
        return repr(self.dict_warehouse)

    def undo_warehouse(self, item, count: int, division: str):
        try:
            if not bool(re.match('^[1234567890.]+$', str(count))):
                raise Exception("Указано не число")

            if item.__class__ in self.type_tex:
                for s in self.dict_warehouse:
                    if s['item'].__class__ == item.__class__:
                        if s['warehouse'] > 0:
                            s['warehouse'] -= count
                            if not s.get(division):
                                s[division] = count
                            else:
                                s[division] += count
                            return "Ok"
                        else:
                            raise Exception("Товар на складе отсутствует")
            else:
                raise Exception("Типа товара нет на складе")
        except Exception as e:
            return repr(e)
        else:
            return "Ok"


p = printer(10, "Printer", 100, 10, 1000)

s = scanner(10, "Scanner", 100, 1001)

x = xerox(10, 20, "Xerox", 100, 30, 100002)

w = warehouse()

print(w.add_warehouse(p, 5))
w.add_warehouse(s, 6)
w.add_warehouse(x, 7)
print(w)

print(w.undo_warehouse(p, 2, "otdel1"))
print(w)
