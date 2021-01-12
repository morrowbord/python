# cписал с разбора дз(слишком сложно!)

result = {}
with open("text_6.txt", "r", encoding="utf-8") as text6:
    for line in text6:
        lesson_t = []
        lessons = ([el for el in line.split(" ")])
        # print(lessons)
        for el in lessons:
            lesson_t.append(''.join(i for i in list(el) if i.isdigit()))
        result[line.split(":")[0]] = sum([int(i) for i in lesson_t if i.isdigit()])

print(result)