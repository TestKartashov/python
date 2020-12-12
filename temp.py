from functools import reduce
from functools import partial
from logging import getLogger

logger = getLogger(__name__)

logger.info("Start program")
logger.warning("Warrning program")
logger.debug("Debug program")
logger.error("error program")

import logging

# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", level=logging.INFO)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")

exit()


def d(a, b):
    return a + b


p_o = partial(d, a=100)
p_o = partial(p_o, b=50)


# print(p_o())

# uu = input("xx: ")
# ss = float(uu)

class Tttt:

    def __enter__(self):
        print("__enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")

    def tes(self):
        print('tes')


tt = Tttt();
# print(tt.test(self=1))

with Tttt():
    tt.tes()

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
