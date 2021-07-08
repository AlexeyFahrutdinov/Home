my_iterable = [1, 2, 3]

for item_name in my_iterable:
    print(item_name)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:
    print(num)
    print("Hello")

for check in mylist:
    # Check for even
    if check % 2 == 0:
        print(check, " - четное число")
    else:
        print(check, " - нечетное число")

list_sum = 0
for slag in mylist:
    # summ all elemenmt in mylist
    list_sum = list_sum + slag
    print(list_sum)
print("сумма всех числе в списке:", list_sum)

long_list = [
    [1, 2, 3, 4, 5],
    [11, 12, 13, 14, 15],
    [111, 112, 113, 114, 115]
]
print(long_list)

print("Пример для закрепления:")


for str_list in long_list:
    print("На этом шаге проверялось:", str_list)
    for krat in str_list:
        print("На этом шаге проверялось", krat)
        if krat > 100:
            print("Числа больше 100", krat)
        if 10 < krat < 100:
            print("Числа больше 10 но меньше 100", krat)
        if krat < 10:
            print("Числа меньше 10", krat)

print("Модуль работы с циклами и строками \n \n")

i = 0
for letter in "hello word":
    print(letter)
    i = i + 1
print(i)


string_check = "Мама, мыла, раму; очень долго"

tz = 0
zap = 0
for j in string_check:
    if j == ";":
        tz = tz + 1
    if j == ",":
        zap = zap + 1
print("В строке точек с запятой :", tz)
print("В строке запятых", zap)


print("Началась работа с кортежами")
tup = (1, 2, 3)
for t in tup:
    print(t)

list_kort = [(1, 2), (3, 4), (5, 6), (7, 8)]
for item in list_kort:
    print(item)

for (a, b) in list_kort:  # Распаковка кортежей
    print(a)
    print(b)
    print(a, b)

for a, b in list_kort:
    print(a)

print("И в заключение поработаем со словарями")

dict1 = {"k1": 1, "k2": 2, "k3": 3, "k4": 4}

for item in dict1:
    print(item)

for item in dict1.items():
    print(item)

for a, b in dict1:
    print(b)

for item in dict1.values():
    print(item)




