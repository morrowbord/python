list1 = [9, 5, 3, 3, 2]
print(list1)
position = 0
reit = int(input("введите рейтинг: "))
if reit > max(list1):
        position = 0
        list1.insert(position, reit)
        print(list1)
elif reit < min(list1):
        list1.append(reit)
        print(list1)
else:
    for x in list1:
        if x < reit:
            position = list1.index(x)
            list1.insert(position, reit)
            print(f"индекс в рейтинге для проверки правильности вставки:{position}")
            print(list1)
            break