from random import randint


with open("text5.txt", "w", encoding="utf-8") as text5:
    line1 = [randint(1, 200) for i in range(200)]
    text5.write(" ".join(map(str, line1)))

    print(f"сумма элементов: {sum(line1)}")



