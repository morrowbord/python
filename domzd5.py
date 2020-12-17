# программа для сложения чисел
def func_key():
    s = 0
    while True:
        string1 = input("Введите числа для сложения через пробел, "
                        "для выхода напишите 'q': ").split()
        for number_i in string1:
            if number_i == 'q':
                print('exit')
                return s
            s = s + int(number_i)
        print(s)


print(func_key(), end='')
