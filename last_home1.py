class Data:
    def __init__(self, date):
        self.date = date

        """
        Программа должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. 
        Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
        Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
        """

    @classmethod
    def class_method(cls):
        cls.date2 = ".".join(map(str, list1))
        return cls.date2

    @staticmethod
    def stat_method():
        if not 0 < int(list1[0]) <= 31:
            print("Неверный день!", end=" ")
        else:
            print("День введен верно.", end=" ")
        if not 0 < int(list1[1]) <= 12:
            print("Неверный месяц!", end=" ")
        else:
            print("Месяц введен верно.", end=" ")
        if not 1900 < int(list1[2]) < 2099:
            print("Неверный год!", end=" ")
        else:
            print("Год введен верно.", end=" ")


list1 = "24-01-1980"
list1 = list1.split(sep="-")
print(f"date: {Data.class_method()}")
list1 = list(map(int, list1))
data1 = Data(list1)
Data.stat_method()
