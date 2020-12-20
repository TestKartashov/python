# 5 Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить ее на экран.

def create_ad_file(num_str):
    with open("dz5.txt", "w", encoding="UTF-8") as f:
        f.writelines(num_str)


create_ad_file("1 2 3 4 5 6 1232")


def sum_file():
    with open("dz5.txt", "r", encoding="UTF-8") as f:
        ls = f.readlines()
        '''Если больше одной строки'''
        for l in ls:
            lt = l.split(" ")
            lt = [int(l) for l in lt]
            print("Sum ", sum(lt))


sum_file()
