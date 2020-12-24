def fact_old(number1):
    f_num = 1
    if number == 0:
        return 0
    else:
        for i in range(1, number+1):
            f_num=f_num*i
            # print(f_num)
        yield f_num


number = int(input("n!: "))
for el in fact_old(number):
    print(el)