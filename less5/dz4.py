# 4 Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

temp_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("dz4.txt", "r", encoding="UTF-8") as f:
    ls = f.readlines()
    lst = []
    for l in ls:
        ls = l.split(" ")
        lst.append(f"{temp_dict[ls[0]]} {ls[1]} {ls[2]}")

    with open("dz41.txt", "w", encoding="UTF=8") as fw:
        fw.writelines(lst)
