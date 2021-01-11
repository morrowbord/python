list1 =["Один", "Два", "Три", "Четыре"]

with open("text_new.txt", "w", encoding="utf-8") as new_file:
    with open("text_4.txt",encoding="utf-8") as text4:
        for content in text4:
            line = content.split()
        for i in list1:
            new_file.writelines(line[0].replace(line[0], i))

