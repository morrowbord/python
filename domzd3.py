def my_func(var1, var2, var3):
    minvar = min(var1,var2,var3)
    if minvar == var3:
        return (var1+var2)
    if minvar == var1:
        return  var2+var3
    if minvar == var2:
        return var1+var3
    # return сумма наибольших двух (var1+var2)


print(my_func(int(input("введите значения: ")), int(input("введите значения: ")), int(input("введите значения: "))))
