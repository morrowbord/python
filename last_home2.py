
class ZeroEx(Exception):
    def __init__(self,txt):
        self.txt = txt

x = input("")
data = input("введите число, кроме 0: ")

try:
    data = int(data)
    x = int(x)
    if data == 0:
        data = 1
        raise ZeroEx("Нельзя делить на 0")

except (ValueError, ZeroEx) as err:
    print(err)
else:
    print(x / data)