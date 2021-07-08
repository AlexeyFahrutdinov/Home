users = {"name": "Mark", "phone": "+79507864598", "age": 25}
for key in users:
    try:
        print(key + ":" + users[key])
    except TypeError as exeption:
        print(key + ":",exeption )



print("Конец программы")


for key in users:
    try:
        print(key + ":" + users[key])
    except:
        print(key + ":" + "Ошибка")
    finally:
        print("Блок finally сработает при любом раскладе. Чтобы закрыть подклчюение с базой или с сетью")