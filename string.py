name = "Федор"
name2 = "Федорович"
name3 = "Федоров"
date = "01.01.2021"
balance = "2567"

import datetime

text = "Уважаемый Иванов Иван Иванович, баланс Вашего лицевогос счета на 01.01.2021 составляет 2567 рублей."
text1 = "Уважаемый " + name3 + " " + name + " " + name2 + ", баланс Вашего лицевого счета на " + date + " составляет " \
        + balance + " рублей."
name = input("Имя")
name2 = input("Отчество")
name3 = input("Фамилия")
date = datetime.datetime.now()
balance = input("Баланс")


text2 = "Уважаемый {0} {1} {2}, баланс Вашего лицевого счета на {3} составляет {4} рублей".format(name3, name, name2,
                                                                                                  date, balance)
text3 = "Уважаемый {name3} {name} {name2}, баланс Вашего лицевого счета на {date} составляет {balance} рублей".\
    format(name3 = name3, name = name, name2 = name2, date = date, balance = balance)



print(text)
print(text1)
print(text2)
print(text3)