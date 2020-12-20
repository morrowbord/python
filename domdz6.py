def int_func():
    global list_line
    text = input("введите строки: ").split()
    list_line =[]
    for i in text:
        i = i.capitalize()
    # print(i)
        list_line.append(i)


print(int_func())
rez = ' '.join(list_line)
print(rez)