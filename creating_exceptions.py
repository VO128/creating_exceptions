# Создание двух исключений, наследуемых от класса Exception
class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


# Функция, генерирующая исключения
def generate_exception(value):
    try:
        if value < 0:
            raise InvalidDataException("недопустимое значение: {}".format(value))
        elif value > 100:
            raise ProcessingException("ошибка обработки значения: {}".format(value))
        else:
            print("значение допустимо")
    except InvalidDataException as e:
        print("недопустимые данные:", e)
        raise
    except ProcessingException as e:
        print("исключение при обработке:", e)
        raise
    except Exception as e:
        print("неизвестное исключение:", e)
        raise
    else:
        print("исключений не произошло")
    finally:
        print("обработка исключений завершена")


# Обработка исключений в функции и передача по стеку вызовов
def calling_function(value):
    try:
        generate_exception(value)
    except InvalidDataException as e:
        print("исключение недопустимых данных, перехваченное при вызове функции:", e)
    except ProcessingException as e:
        print("исключение обработки, перехваченное в calling_function:", e)
    except Exception as e:
        print("неизвестное исключение, перехваченное при вызове функции:", e)
    else:
        print("не обнаружено исключения")


# Вызов функций и обработка исключений
try:
    calling_function(-10)
    print("---")
    calling_function(50)
    print("---")
    calling_function(200)
except InvalidDataException as e:
    print("недопустимое исключение данных:", e)
except ProcessingException as e:
    print("исключение перехваченной обработки:", e)
except Exception as e:
    print("неизвестное исключение:", e)
finally:
    print("выполнение программы завершено")
