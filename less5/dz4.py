# 4 Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


with open("dz4.txt", "r", encoding="UTF-8") as f:
    ls = f.readlines()
    lst = []
    for l in ls:
        ls = l.split(" ")
        if ls[0] == "One":
            lst.append(f"Один {ls[1]} {ls[2]}")
        elif ls[0] == "Two":
            lst.append(f"Два {ls[1]} {ls[2]}")
        elif ls[0] == "Three":
            lst.append(f"Три {ls[1]} {ls[2]}")
        elif ls[0] == "Four":
            lst.append(f"Четыре {ls[1]} {ls[2]}")
    with open("dz41.txt", "w", encoding="UTF=8") as fw:
        fw.writelines(lst)
