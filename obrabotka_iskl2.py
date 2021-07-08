try:
    f = open("4.txt", "w")
    f.write("Записываем строку в файл")
except TypeError:
    print("Произошла ошибка TypeErorr")
except OSError:
    print("Произошла ошибка OSError")
except:
    print("Любая другая ошибка")
finally:
    print("Этот код выполнится в любом случае")


def asc_for_int():
    while True:
        try:  # Пробуем выполнить код
            result = int(input("Введите целое число:"))
            print("Это целое число", result)
        except:  # Если ошибка то выполняем всё что здесь
            print("Это не число")
            continue
        else:  # Если не было ошибки, то выполняем это
            print("Спасибо что ввели число")
            break 
        finally:
            print("Конец выполнения функции")


asc_for_int()