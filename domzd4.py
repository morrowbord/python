def my_func(x, y):
    x = x ** (-y)
    return x

print("Программа считает Х в степени (-Y):")
print(f"X в степени (-Y): {my_func(float(input('введите X: ')), int(input('введите Y: '))):.5f}")
