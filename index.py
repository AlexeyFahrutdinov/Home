import users  # Вызываем модуль. Имя модуля без расширения

# Вызываем функции из модуля через точку.
users.new(1, 2)
users.auth(1, 2)
users.block(1)

# Псевдонимы для модулей и функций

import users as peoples
from users import new

print(new(1, 2))
print(peoples.auth(1, 2))
print(peoples.block(1))

# Можно импортировать все функции из модуля

from users import *

# Подключение модулей из пакетов

import user.admin as admin  # Вызвал модуль из пакета и дал ему псевдоним
# admin.slojenie()  # Вызвал функцию сложение из модуля.

from user.admin import slojenie
slojenie()





