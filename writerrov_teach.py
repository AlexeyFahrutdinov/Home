import csv

with open("new_table.csv", "w", newline="") as new_table_file:
    new_table_writer = csv.writer(new_table_file, delimiter = ';')
    new_table_writer.writerow(["name", "phone", "age", 'height', "weight"])
    new_table_writer.writerow(["mark", "+79514286598", "23", '187', "83"])

row = [
    ["fio", "staj", "dohod"],
    ["ivan", "5 let", "100 rub"],
    ["stepan", "2 day", "1 dollar"],
]

with open("str_table.csv", "w", newline="") as str_table:
    writer_str_table = csv.writer(str_table, delimiter = ';')
    writer_str_table.writerows(row)

row_vacansy = [
    ["Должность", "Оклад", "График работы", "Требования"],
    ["Сантехник", "100 рублей", "Пятидневка", "Не пьющий"],
    ["Программист", "500 рублей", "Удаленно", "Высшее образование"],
    ["Секретарша", "10000 рублей", "По вечерам", "Самазливость"]
]

with open("vacansy1.csv", "w", newline="") as vacansy_file:
    writer_vacansy_file = csv.writer(vacansy_file, delimiter = ';')
    writer_vacansy_file.writerows(row_vacansy)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
with open("test2.csv", "w", newline = "") as test_file:
    writer_test_file = csv.writer(test_file, delimiter = ';')


    for num in nums:
        writer_test_file.writerow(str(num))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

with open("nums.csv", "w", newline = "") as nums_file:
    writer_nums_file = csv.writer(nums_file, delimiter = ';')
    for index1, num in enumerate(nums):
        if num % 2 == 0:
            continue
        str_num = ("Число №", index1, "нечетное, оно равно:", num)
        writer_nums_file.writerow(str_num)

str_table = "Закрепление знаний о записи в ЦСВ"

with open("zakrep.csv", "w", newline="") as zakrep_file:
    writer_zakrep_file = csv.writer(zakrep_file, delimiter = ';')
    writer_zakrep_file.writerow(str_table)





