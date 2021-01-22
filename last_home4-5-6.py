class Sklad:
    def na_sklad(self, count):
        count = [input(f"добавить на склад:").split()]
        self.count = count
        return count

class Orgtech(Sklad):
    def __init__(self, x):
        self.x = x
        print(f" добавлено {data_scaners} шт на склад *сканеров")


class Scanner(Orgtech):
    def scanner(self):
        return f"{self.x}"


class Printer(Orgtech):
    def printer(self):
        return f"{self.x}"


class Xerox(Orgtech):
    def xerox(self):
        return f"{self.x}"


data_scaners = []

# scanner1 = Scanner("Сканер")
# printer1 = Printer("Принтер")
# xerox1 = Xerox("Ксерокс")


while True:
    sc = Scanner(0)
    sc.na_sklad(0)
    data_scaners += [int(sc.count[0][0])]
    print(data_scaners)
    # pr = Printer(8)
    # xe = Xerox(9)
