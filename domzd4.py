def my_func(x, y):
    x = x ** (-y)
    return x


print(f"X в степени -Y: {my_func(int(input('введите X: ')), int(input('введите Y: ')))}")
