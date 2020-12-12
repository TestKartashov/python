# 7 Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
from json import dumps as con_json


def openf(fl):
    with open(fl, "r", encoding="UTF-8") as f:
        return f.readlines()


def parser_file(file):
    ls_file = openf("dz7.txt")
    ls_firm = []
    for ls in ls_file:
        firm = ls.split(" ")
        dict_firm = dict()
        dict_firm["название"] = firm[0]
        dict_firm["форма"] = firm[1]
        dict_firm["выручка"] = firm[2]
        dict_firm["издержки"] = firm[3]
        ls_firm.append(dict_firm)
    return ls_firm


def calc(file):
    firmas = parser_file(file)
    ls = []
    dict_r = dict()
    ls_average = []
    for dict_f in firmas:
        summ = float(dict_f["выручка"]) - int(dict_f["издержки"])
        dict_r[dict_f["название"]] = summ
        if summ > 0:
            ls_average.append(summ)
    dict_av = dict()
    dict_av["average_profit"] = sum(ls_average) / len(ls_average)
    ls.append(dict_r)
    ls.append(dict_av)
    return ls


tr = calc("dz7.txt")
js = con_json(tr)
print(js)
