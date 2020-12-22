def zarplata():
    from sys import argv
    (script_name, hours, money_in_hour, premiya) = argv

    print("Имя скрипта: ", script_name)
    print("Выработка в часах: ", hours)
    print("Ставка в час: ", money_in_hour)
    print("Премия: ", premiya)
    return hours, money_in_hour, premiya


print(zarplata())
list_raschet = (list(map(int, zarplata())))
result = list_raschet[0] * list_raschet[1] + list_raschet[2]
print(f"Ваша зарплата: {result} руб")
