# 3 Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

def average(lst):
    return sum(lst) / len(lst)


with open("dz3.txt", "r", encoding="UTF-8") as fl:
    ls = fl.readlines()
    sotr = [l for l in ls if float(l.split(",")[1]) < 20000]
    for s in sotr:
        print(s)
    summs = [float(l.split(",")[1]) for l in ls]
    print("Среднее значения по всем", average(summs))
