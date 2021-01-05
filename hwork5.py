class Stationery:
    title = 0

    def draw(self):
        print("Запуск отрисовки:")


class Pen(Stationery):

    def draw(self):
        print("Запуск Ручка")


class Pencil(Stationery):

    def draw(self):
        print("Запуск Карандаш")


class Handle(Stationery):

    def draw(self):
        print("Запуск Маркер")

s = Stationery()
s.draw()
p = Pen()
p.draw()
pen= Pencil()
pen.draw()
han=Handle()
han.draw()