
list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list2 = [list1[x] for x in range(1, len(list1)) if list1[x] > list1[x-1]]

print(list2)