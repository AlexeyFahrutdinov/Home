import csv

with open("table.csv", "r", encoding="utf-8", newline="") as table_file:
    reader = csv.reader(table_file, delimiter = ';')
    for line in reader:
        for item in line:
            print(item)
        print("\n")

# for line in reader:
# print(line)