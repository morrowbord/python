timer = int(input('введите время в секундах: '))
hours = timer / 3600
min = hours / 60
sec = min / 60
print(f'Время в часах, минутах и секундах: {hours:.1f}:{min:.1f}:{sec:.1f} ')
