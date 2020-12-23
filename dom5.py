from random import randint
from functools import reduce


def my_func(x, y):
    return x * y


list1 = [randint(100, 1000) for i in range(10)]
sum_all = reduce(my_func, list1)

print(list1)
print(f"сумма чисел последовательности: {sum_all}")

