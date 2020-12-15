def first_func():
    var1 = int(input("введите первое число: "))
    var2 = int(input("введите второе число: "))
    if var2 == 0:
        print('На ноль делить нельзя!')
    else:
        var1 = var1 / var2
        return var1


print(f"результат деления: {first_func():.3f}")
