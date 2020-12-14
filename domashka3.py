list1 = ['Зима', 'Весна', 'Лето', 'Осень']
# dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
month = int(input("введите номер месяца от 1 до 12: "))
if month == 1 or month == 2 or month == 12:
    print(list1[0])
elif month == 3 or month == 4 or month == 5:
    print(list1[1])
elif month == 6 or month == 7 or month == 8:
    print(list1[2])
else:
    print(list1[3])
