import csv

open("table1.csv", "w", encoding = "utf-8", newline = "")  # Передаем пораметр newline чтобы избежать проблем
# с совместимостью



file = open("readme.txt","a")  # флаг w - перезаписывает, флаг a - дописывает в коннец
print(type(file))
file.write("1")
file.close()

file = open("readme1.txt","r")  # read
data = file.read()
print(data)

file.close()

with open("readme3.txt", "w") as readme3_file:
    readme3_file.write("hello world")




