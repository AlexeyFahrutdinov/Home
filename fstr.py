import datetime

text = "Уважаемый Иванов Иван Иванович, баланс Вашего лицевогос счета на 01.01.2021 составляет 2567 рублей."

name = input("Имя")
name2 = input("Отчество")
name3 = input("Фамилия")
date = datetime.datetime.now()
balance = input("Баланс")

text_f = f"Уважаемый {name3} {name} {name2}, баланс Вашего лицевого счета на {date} сосатавляет {balance} рублей"

print(text)
print(text_f)