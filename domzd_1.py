def first_func(var1, var2):
    if var2 == 0:
        print('На ноль делить нельзя!')
        return var1-var1
    else:
        var1 = var1 / var2
        return var1


print(
    f'результат деления: {first_func(int(input("введите первое число: ")),int(input("введите второе число: "))):.3f}')

