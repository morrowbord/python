spisok1 = list(input("введите список элементов: "))
print(spisok1)
list1 = spisok1[::2]
list2 = spisok1[1::2]
position = 1
if position % 2 != 0:
    i = 0
    while i < len(list1):
        list2.insert(position, list1[i])
        i = i + 1
        position = position + 2
    print(list2)
