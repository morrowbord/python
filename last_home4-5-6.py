# class ZeroEx(Exception):
#     def __init__(self,txt):
#         self.txt = txt

class Sklad:
    @staticmethod
    def na_sklad():
        list1 = [input(f"добавить на склад:").split()]
        list1.append(list1)
        return list1


class Orgtech(Sklad):
    def __init__(self, x):
        self.x = x
        print(f" {self.x} = нет на складе ")


class Scanner(Orgtech):
    def scanner(self):
        return f"{self.x}"


class Printer(Orgtech):
    def printer(self):
        return f"{self.x}"


class Xerox(Orgtech):
    def xerox(self):
        return f"{self.x}"


scanner1 = Scanner("Сканер")
printer1 = Printer("Принтер")
xerox1 = Xerox("Ксерокс")

while True:
    print(f"на складе: принтеров {Sklad.na_sklad()[0][0]}, сканеров {Sklad.na_sklad()[0][0]}, "
          f"ксероксов {Sklad.na_sklad()[0][0]}")