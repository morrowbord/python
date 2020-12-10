revenue = int(input("выручка: "))
expenses = int(input("издержки: "))

if revenue > expenses:
    income = revenue - expenses  # прибыль
    print(f'мы получили прибыль в размере: {income}млн')
    revenue_margin = income / revenue*100
    print(f"рентабельность выручки: {revenue_margin:.2f}%")
    staff = int(input("Численность сотрудников: "))
    print(f"прибыль на одного сотрудника: {income / staff}млн ")
elif revenue == expenses:
    print('работаем за еду: прибыль = расходам!')
else:
    loss = expenses - revenue
    print(f'одни расходы, УБЫТОК: {loss} млн')
