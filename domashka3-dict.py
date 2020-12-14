dict1 = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
month = int(input("введите номер месяца от 1 до 12: "))
if month in dict1.get("Зима"):
    print("Зима")
elif month in dict1.get('Весна'):
    print("Весна")
elif month in dict1.get('Лето'):
    print("Лето")
elif month in dict1.get('Осень'):
    print("Осень")
    