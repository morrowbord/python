class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return self.cell

    def __add__(self, other):
        return self.cell+other.cell

    def __sub__(self, other):
        if self.cell > other.cell:
            return self.cell - other.cell
        else:
            return "Так не выйдет!"

    def __mul__(self, other):
        return f"{self.cell * other.cell}"

    def __floordiv__(self, other):
        return f"{self.cell // other.cell}"

    def make_order(self, row):
        pass
        return '\n'.join(['*' * row for _ in range(self.cell//row)])+'\n'+"*" * (self.cell*row)


cell1 = Cell(10)
cell2 = Cell(3)
print(cell1//cell2)
print(cell1+cell2)
print(cell1-cell2)
print(cell1*cell2)
print(Cell.make_order(cell1, 5))
print(Cell.make_order(cell2, 5))
