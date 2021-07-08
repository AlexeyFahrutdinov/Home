ref_id = "21943"
link = "http://ya.ru/"
ref_link = ref_id + link  # Такой порядок не подходит
ref_link = link + ref_id  # Сложение строк. Итоговая строка сумма, будет в таком же порядке как слагаемые
print(ref_link)

# Псевдонимы
# ref_link = "http://ya.ru/{ref_id1}".format(ref_id1 = input("Введите ref_id1"))
# print(ref_link)

# Замена по порядоковому номеру

ref_link = "http://ya.ru/{0}".format(1111)
print(ref_link)

ref_link = "http://ya.ru/{0}/{1}/{2}/{1}".format(1, 2, 3)
print(ref_link)

# Форматирование через подстановку переменных

name = "Ivan"
x = "Введите с кем здороваться"
word = f"Hello {x} my name is {name}"
print(word)

# Cклеивание join

word = "строка"
glue = "//"
join_word = glue.join(word)
join_glue = word.join(glue)
print(join_word)
print(join_glue)

word = ["Раз", "Два", "Три", "Четыре", "Пять"]
glue = "|"
join_word = glue.join(word)
print(join_word)

# Разделение split

word = "Собака друг человека - человек собаке друг"
word_list_short = word.split(" ", 2)  # Разделяет первые два но в список добавляет всю оставшуюся строку
word_list = word.split(" ")  # Разделяет все
print(word_list_short)
print(word_list)

# Проверка начинается ли строка с подстроки

word = "Таракан тараканище"
word_vhod = word.startswith("Тараканище")
print(word_vhod)

# Проверяем заканчивается ли подстрокой

word = "На золотой трубе сидели: мишки гами, Том и Джери"
word_end = word.endswith("Джери")
print(word_end)

# Замена подстроки в строке replace

word = "Девушки фабричные с парнями встречаются"
word_replace = word.replace("встречаются", "гуляют")
print(word_replace)

# Если нужно заменить подстроку заданное число раз

word = "Ветер с моря дул, Ветер с моря дул. Нагонял беду, Нагонял беду. И сказал ты мне, И сказал ты мне. " \
       "Больше не прийду"
word_replace = word.replace("Ветер с моря дул", "", 1)
print(word_replace)

# Удаление пробелов

word = "             Слово с лишними пробелами              "
print("|", word, "|")
word_strip = word.strip()
print("|", word_strip, "|")
print("|", word, "|")

word_lstrip = word.lstrip()
print("|", word_lstrip, "|")

word_rstrip = word.rstrip()
print("|", word_rstrip, "|")

word = "много слов с маленькой буквы"
word_capitalize = word.capitalize()
print(word)
print(word_capitalize)

word_title = word.title()
print(word)
print(word_title)


word_num = "123"
word_str = "f23"
result = word_num.isnumeric()
result1 = word_str.isnumeric()
print(word_num)
print(word_str)
print(result)
print(result1)

my_string = "Hello world"
print(my_string[0])
print(my_string[-1])

my_string = "abcdefg"
print(my_string[2])
print(my_string[2:])
print(my_string[:3])
print(my_string[3:6])
print(my_string[2:] + my_string[4:])
print(my_string[1:5:2])

letter = "a"
letter = letter*10
print(letter)

result = 10/3
print(result)
print("Результат = {r:1.2 f}".format(r = result))







