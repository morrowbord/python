
with open("out_file.txt", "w", encoding="utf-8") as out_f:
    f = 0

    while f != 1:
        endof = input("Введите строки для записи:")
        if endof != "":
            out_f.write(endof)
            out_f.write("\n")
        else:
            f = 1
            print("closed")