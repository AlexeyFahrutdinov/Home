def add(n1, n2):
    print(n1+n2)

n1 = "10"


try:

    n2 = input("Введите n2:")
    print(add(n1, n2))
except:
    n2 = 20
    print("Что-то пошло не так при вводе n2 с клавиатуры, поэтому пришлось присвоить")
    print(add(n1, n2))
else:
    print("Получилось сложить то, что ввели с клавиатуры")


