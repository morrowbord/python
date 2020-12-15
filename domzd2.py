def first_func():
    var1 = (input("введите Имя: "))
    var2 = (input("введите Фамилию: "))
    var3 = (input("введите год рождения: "))
    var4 = (input("введите город проживания: "))
    var5 = (input("введите email: "))
    var6 = (input("введите телефон: "))
    return var1, var2, var3, var4, var5, var6
# 
# var1_val, var2_val, val3_val, val4_val, val5_val,val6_val = first_func()
print(f"результат: {first_func()}")