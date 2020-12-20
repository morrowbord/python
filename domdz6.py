def int_func():
    text = input("введите строки: ")
    text = text.capitalize()
    return text


list1 = int_func().split()
list_line =[]
for i in list1:
    i = i.capitalize()
    # print(i)
    list_line.append(i)
# print(list_line)
rez = ' '.join(list_line)
print(rez)