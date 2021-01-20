
class ZeroEx(Exception):
    def __init__(self,txt):
        self.txt = txt


data = []
q = 1
while q == 1:
    try:
        x = input("введите число или 'stop' для выхода :\n ")
        if x == 'stop':
            q = 0
        if not x.isdigit():
            raise ZeroEx("Можно добавлять только цифры!")
        else:
            data.append(x)
    except (ValueError, ZeroEx) as err:
        print(err)
    finally:
        print(data)



