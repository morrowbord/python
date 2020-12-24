from itertools import count, cycle
from random import  randint
def count_func():
    for i in count(3):
        print(i, sep='')
        if i ==10:
            break

def cycle_func():
    list1 = [i**2-1 for i in range(randint(40, 100))]
    print(list1)
    for i in cycle(list1):
        print(i)
        if i > 500:
            break
count_func()
cycle_func()