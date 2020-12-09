timer = int(input('введите время в секундах: '))
hours = timer // 3600
minutes = int(timer % 3600 / 60)
seconds = abs(minutes - (timer % 3600 / 60))
print(f'Время в часах, минутах и секундах: {hours}:{minutes}:{seconds*60:.0f}')