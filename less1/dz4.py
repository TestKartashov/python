# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n_str = input('Enter number: ')

if not n_str.isdigit() or int(n_str) < 0:
    print('Неверное значение')
    exit()

# Первый способ
i = -1
num = 0
while i < len(n_str):
    if len(n_str) > (i + 1) and num < int(n_str[i + 1]):
        num = int(n_str[i + 1])
    i += 1

print(num)

# Второй способ
i = 0
max_num = 0
while i < len(n_str):
    num = int(n_str[i])
    if len(n_str) > (i + 1):
        if num < int(n_str[i + 1]):
            num = int(n_str[i + 1])

        if max_num < num:
            max_num = num
    i += 1

print(max_num)
