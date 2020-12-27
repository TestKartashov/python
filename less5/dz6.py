# 6 Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и лабораторных
# занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий
# название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def ls_dict_count(ls):
    ts = [l for l in ls if l != "" and l != "-"]
    ts.pop(0)
    count = 0
    for t in ts:
        num = ""
        for n in t:
            if not n.isdigit():
                break
            num = f"{num}{n}"
        if num != "":
            count += int(num)
    return count


with open("dz6.txt", "r", encoding="UTF-8") as f:
    ls = f.readlines()
    dic = dict()
    for l in ls:
        sp = l.split(" ")
        dic[sp[0]] = ls_dict_count(sp)
    print(dic)