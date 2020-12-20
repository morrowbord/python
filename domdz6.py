def int_func():
    # global list_line
    text = input("введите строки: ").split()
    list_line =[]
    for i in text:
        i = i.capitalize()
    # print(i)
        list_line.append(i)
    return list_line


list_line = int_func()
# print(list_line)
rez = ' '.join(list_line)
print(rez)