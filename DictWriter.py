import csv

row = ["FIO", "Zvanie", "Uroven_probotosti", "Skills"]

with open("solder1.csv", "w", newline="") as solder_file:
    dictwrite_solder_file = csv.DictWriter(solder_file, fieldnames = row, delimiter = ';')
    dictwrite_solder_file.writeheader()
    dictwrite_solder_file.writerow({"FIO": "Petrov", "Zvanie": "Kapitan","Uroven_probotosti": "Klinika",
                                    "Skills": "krasneet" })

rows = [
 {"name": "mark", "phone": "+79514286598", "age": "23", "height": "187", "weight": "83"},
 {"name": "anna", "phone": "+79514286598", "age": "22", "height": "164", "weight": "59"},
 {"name": "oleg", "phone": "+79514286598", "age": "27", "height": "184", "weight": "80"},
]
with open("table.csv", "w", encoding="utf-8", newline="") as csv_file:
 # Определили список заголовков столбцов
 columns = ["name", "phone", "age", 'height', "weight"]
 # Подготовили дескриптор фала для записи CSV
 writer = csv.DictWriter(csv_file, fieldnames=columns, delimiter=';')
 writer.writeheader()
 # Записываем список словарей с данным, где ключ равен заголовку столбца
 writer.writerows(rows)