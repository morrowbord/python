from random import randint
from functools import reduce


def my_func(x, y):
    return x * y


list1 = [i for i in range(100, 1001) if (i) % 2 == 0]
sum_all = reduce(my_func, list1)

print(f"последовательность:\n{list1}\n")
print(f"умножение чисел последовательности:\n{sum_all}\n")
