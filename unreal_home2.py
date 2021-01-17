from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumpion(self):
        pass
    """
    проект расчета суммарного расхода ткани на производство одежды
    """


class Coat(Clothes):
    """
     Для определения расхода ткани по каждому типу одежды использовать формулы:
     для пальто (V/6.5 + 0.5)
    """

    # def __init__(self, v):
    #     self.v = v

    def consumpion(self):
        v = (self.param / 6.5 + 0.5)
        return v


class Suit(Clothes):
    """
     Для определения расхода ткани по каждому типу одежды использовать формулы:
     для костюма (2 * H + 0.3).
    """

    # def __init__(self, h):
    #     self.h = h

    def consumpion(self):
        h = (2 * self.param + 0.3)
        return h


rashod_tkani_coat = Coat(float(input("Введите размер пальто: ")))
rashod_tkani_suit = Suit(float(input("Введите рост костюма: ")))

# print(rashod_tkani_coat.v)
# print(rashod_tkani_suit.h)

rashod = rashod_tkani_coat.consumpion() + rashod_tkani_suit.consumpion()
print(f"суммарный расход ткани: {rashod:1f}")
