import os

# os.remove("2.txt")

# os.rename("1.txt", "11.txt")

# os.rmdir("C:/Users/alexe/Desktop/test")
import tarfile

# os.mkdir("C:/Users/alexe/Desktop/test1")

try:
    file = open("C:/Users/alexe/Desktop/test/file.txt", "a", encoding="utf-8")
    try:
        file.write("Новый текст")
    except Exception as error:
        print(error)
    finally:
        file.close()
        print("Файл закрыт")
    file.close()  # После использования файлы нужно закрывать.

except FileNotFoundError as error:
    print(error)

with open("C:/Users/alexe/Desktop/test/file.txt", "a", encoding="utf-8") as fsda:
    fsda.write("Мой новый текст виф")




