string1 = input("введите слова через пробел: ")
list1 = string1.split()
# print(list1)
for i,slovo in (enumerate(list1)):
    if len(slovo) > 10:
        slovo = slovo[:10]
        print(i+1,slovo)
    else:
        print(i+1, slovo)

