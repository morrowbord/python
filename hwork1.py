import time


class TrafficLight:
    # атрибуты класса
    __color = ["Красный", "Желтый", "Зеленый", "Желтый"]
    # методы класса

    def running(self):
        while True:
            for i in self.__color:
                print(i)
                if i == "Красный":
                    time.sleep(7)
                time.sleep(2)


tl = TrafficLight() #создание экземпляра
print(tl.running())  #вызов метода







