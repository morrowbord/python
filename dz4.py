number = int(input("Введите число: "))
max = 0
while number:
    number_i = number % 10 #вытаскивает  цифры с конца, т.к это осаток от деления на 10
    if number_i > max:
        max = number_i
#    print(number_i)
    number = (number // 10) #режет число,пока number не станет false
print(f'самое большое число: {max} ')