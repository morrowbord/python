spisok1 = list(input("введите список элементов: "))
print(spisok1)
list1 = spisok1[::2]
list2 = spisok1[1::2]
# print(f'это список 2{list2}')
# print(f'это список 1{list1}')
# в list2 нужно засунуть значения лист1
position = 1
if position % 2 != 0:
    # print(position)
    i = 0

    # list2.insert(1, list1[0])
    # list2.insert(3, list1[1])
    # list2.insert(5, list1[2])
    while i < len(list1):
        list2.insert(position, list1[i])
        i = i + 1
        position = position + 2
    print(list2)
