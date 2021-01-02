class Road:
    # атрибуты класса
    depth = 5
    mass = 0.025
    # методы класса
    def __init__(self, _length,_width):
        all_mass = (Road.mass*Road.depth)*(_length*_width)
        print(f"масса полотна: {all_mass} тонн")


road = Road(_length=int(input("Длина дороги: ")), _width=int(input("Ширина дороги: "))) # создание экземпляра

