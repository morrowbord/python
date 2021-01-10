with open("text_3.txt", "r", encoding="utf-8") as t3_file:

    content = t3_file.readlines()
    print(f'число сотрудников: {len(content)}')
    everage = 0.0
    for i in content:
        sername = i.split()
        float_sername = float(sername[1])
        everage = everage + float_sername
        if float_sername < 20000:

            print(f"доход менее20тр: {sername[0]}")

    print(f"среднй доход: {everage/len(content)}")
