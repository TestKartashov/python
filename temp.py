<<<<<<< Updated upstream
from functools import reduce
from functools import partial



def d(a, b):
    return a + b
p_o = partial(d, a = 100)
p_o = partial(p_o, b = 50)
print(p_o())



'''
from datetime import datetime as dt
from time import sleep

from random import random, randint, randrange
#from datetime import

d = {k: v for k in range(10) for v in range(10) if v == k}
print(d)
from sys import argv

def tt():
    yield 1
    yield 2
    yield 3
t = tt()

print(next(t))
print(next(t))




st = dt.now()

print(random())
print((randint(1, 4)))
print((randrange(1, 10, 2)))

print(argv)


a = {1: 10, 2: 20, 3: 30}
b = [[i, a[i]] for i in a]
print(b)
print([j for i in b for j in i])
'''
 
class ttt:
    def __init__(self):
        print('2')

    def cvll(self):
        print("d")





t = ttt()
t.cvll()
>>>>>>> Stashed changes
