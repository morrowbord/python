class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.n = name
        self.s = surname
        self.p = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"полное имя: {self.n} {self.s}")

    def get_total_income(self):
        # full_income=wage+bonus
        x = int(self._income["wage"])
        y = int(self._income["bonus"])
        full_income = x + y

        print(f"полный доход: {full_income}")


pos1 = Position("Вася", "Пупкин", "БухГалтер", "22000", "10000")
pos2 = Position("Толик", "Полик", "Программист", "20000", "13000")
pos3 = Position("Даша", "Дудина", "Тестеровщик", "30000", "25000")

pos1.get_full_name()
pos1.get_total_income()
print("")
pos2.get_full_name()
pos2.get_total_income()
print("")
pos3.get_full_name()
pos3.get_total_income()
