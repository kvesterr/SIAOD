class Cnoot:
    """ Класс алгоритма поиска КМП """

    def __init__(self):
        """ Конструктор класса """
        self.reg = True  # Не учитывать регистры по умолчанию(пользователю будет предложен выбор


    def find_biggest_suffix(self, st):
        """ Метод поиска наибольшего суффикса во входящей строке """

        # Стандартная для алгоритма инициализация
        j = 0
        i = 1
        p = [0]*len(st)  # Массив значений длин суффиксов и префиксов

        while i < len(st):  # Пока не прошлись по всей строке
            if st[j] == st[i]:  # Если символы равны
                p[i] = j+1
                i += 1
                j += 1
            else:  # Если не равны
                if j == 0:
                    p[i] = 0
                    i += 1
                else:
                    j = p[j-1]

        # Возвращаем список пи
        return p

    # Метод находит подстроку в строке и возвращает результат поиска
    def find_string(self, main_string, f_string):
        if self.reg == True:
            main_string = str.lower(main_string)
            f_string = str.lower(f_string)
        i = 0
        j = 0
        n = len(main_string)
        m = len(f_string)
        p = self.find_biggest_suffix(f_string)

        while i < n:
            if main_string[i] == f_string[j]:  # Если символы равны
                # Увеличиваем счетчики
                i += 1
                j += 1

                # Условие нахождения образа
                if j == m:
                    print('Образ найден.')
                    break
            else:  # Если символы не равны
                # Перезаписываем значения нужных счетчиков
                if j > 0:
                    j = p[j-1]
                else:
                    i += 1

            if i == n:
                print('Образ не найден.')
                break
