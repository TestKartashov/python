# Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.


my_f = open("dz2.txt", "r")
cnt = 0
for line in my_f:
    cnt += 1
    print("-----------------------------------------")
    print("Count row", cnt)
    strLs = line.split(" ")
    strLs = [s for s in strLs if s != "\n"]
    print("Count слов", len(strLs))

my_f.close()
