# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.11

dict_montf = {(12, 1, 2): "Зима", (3, 4, 5): "Весна", (6, 7, 8): "Лето", (9, 10, 11): "Осень"}

num = int(input("1. Enter number from 1 to 12: "))

for d in dict_montf:
    if num in d:
        print(dict_montf[d])

lis_s = ["Зима", "Весна", "Лето", "Осень"]
lis_pos = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]

num = int(input("2. Enter number from 1 to 12: "))

for index, l in enumerate(lis_pos):
    if num in l:
        print(lis_s[index])
