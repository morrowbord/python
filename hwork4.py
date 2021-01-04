from random import randint


class Car:
    direction = bool

    def __init__(self, color, name, is_police=False):
        try:
            self.speed = int(input(f"Введите скорость автомобиля: "))
        except TypeError or ValueError or AttributeError:
            print("Введите скорость заного!")
            self.speed = 0

        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """машина поехала!"""
        if self.speed == 0:
            print("машина не едет!")

        else:
            print(f"машина {self.color} {self.name} поехала! ")

    def turn(self):
        """машина повернула!"""
        if self.speed == 0:
            pass
        else:
            self.direction = randint(0, 1)

            if self.direction:
                print(f"машина {self.color} {self.name} повернула на право")
            else:
                print(f"машина {self.color} {self.name} повернула на лево")

    def stop(self):
        """Машина остановилась!"""
        if self.speed == 0:
            pass
        else:
            print(f"машина {self.color} {self.name} остановилась!")

    def show_speed(self):
        print(f"Скорость авто: {self.speed}км/ч ")
        """показывать текущую скорость автомобиля"""


class TownCar(Car):
    """
    текущая скорость TownCar
    При значении скорости свыше 40 (WorkCar)
    должно выводиться сообщение о превышении скорости.
    """

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость TownCar превышена на {self.speed - 40}км/ч! Снизьте до 40км/ч")
        else:
            print(f"Скорость {self.name}: {self.speed}км/ч ")


class WorkCar(Car):
    """
    текущая скорость WorkCar:
    При значении скорости свыше 60 (TownCar)
    должно выводиться сообщение о превышении скорости.
    """

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость WorkCar превышена на {self.speed - 60}км/ч!! Снизьте до 60км/ч")
        else:
            print(f"Скорость: {self.speed}км/ч! ")


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
