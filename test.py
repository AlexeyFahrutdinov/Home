# name = input("Ваше имя: ")
# date = input("Сегодняшняя дата: ")
# print("Привет,", name, "! Сегодня: ", date, " ты впервые написал программу на языке Python!")

# Пропуск итерации цикла. Вернуться в начало continue

users = ["Mark", "Alex", "Anna", "Roma", "Ivan"]


for user in users:
    if user == "Anna":
        continue
    print("Мужик 1: ", user)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for num in nums:
    if num % 2 == 1:
        continue
    print("Число:", num)


users = ["Mark", "Anna", "Oleg", "Alex"]
for index, user in enumerate(users):
 print(str(index) +": " + user)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


for index1, num in enumerate(nums):
    if num % 2 == 0:
        continue
    print("Число №", index1, "нечетное, оно равно:", num)



