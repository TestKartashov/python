import time

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.


second = input('Enter second: ')

if not second.isdigit():
    print('Неверное значение')
    exit()

second = int(second)

# самопальный расчте
hour = second / 3600

if hour > 24:
    day = hour // 24
    hour = hour - (day * 24)

min = (second % 3600) / 60
sec = (second % 3600 % 60)

print('чч:мм:сс %02d:%02d:%02d' % (hour, min, sec))

# системный
# print(time.strftime("Modul time: чч:мм:сс %H:%M:%S", time.gmtime(second)))


