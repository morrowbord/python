from random import randint


class Car:
    direction = bool

    def __init__(self, color, name, is_police=False):
        self.is_police = is_police
        self.speed = int(input(f"Введите скорость автомобиля: "))
        self.color = color
        self.name = name

    def go(self):
        """машина поехала!"""
        print(f"машина {self.color} {self.name} поехала! ")

    def turn(self):
        """машина повернула!"""
        self.direction = randint(0, 1)
        # print(self.direction)
        if self.direction:
            print(f"машина {self.color} {self.name} повернула на право")
        else:
            print(f"машина {self.color} {self.name} повернула на лево")

    def stop(self):
        """Машина остановилась!"""
        print(f"Машина {self.color} {self.name} остановилась!")

    def show_speed(self):
        print(f"Скорость авто:{self.speed} ")
        """показывать текущую скорость автомобиля"""


class TownCar(Car):
    """
    текущая скорость TownCar
    При значении скорости свыше 40 (WorkCar)
    должно выводиться сообщение о превышении скорости.
    """

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость TownCar превышена! Снизьте до 40км/ч")
        else:
            print(f"Скорость {self.name}: {self.speed} ")


class WorkCar(Car):
    """
    текущая скорость WorkCar:
    При значении скорости свыше 60 (TownCar)
    должно выводиться сообщение о превышении скорости.
    """

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость WorkCar превышена! Снизьте до 60км/ч")
        else:
            print(f"Скорость: {self.speed} ")


class SportCar(Car):
    pass


class PoliceCar(Car):
    Car.is_police = True


car1 = TownCar("blue", "Toyota")
car1.go()
car1.show_speed()
car1.turn()
car1.stop()

car2 = WorkCar("black", "Ford")
car2.go()
car2.show_speed()
car2.turn()
car2.stop()

scar1 = SportCar("yellow", "McLaren")
scar1.go()
scar1.show_speed()
scar1.turn()
scar1.stop()

if Car.is_police:
    police_car = PoliceCar("Police", "Chevrolet")
    police_car.go()
    police_car.show_speed()
    police_car.turn()
    police_car.stop()
