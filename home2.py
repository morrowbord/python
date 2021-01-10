with open("out_file.txt", "r") as my_file:
    i = 0
    for lines in my_file:
        print(lines, sep="")
        stroki = lines.split()
        dlina = len(stroki)
        i += 1
        print(f"Число слов в {i} строке: {dlina}")
        print("")
