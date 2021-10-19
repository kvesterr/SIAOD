class Boyer:
    """ Класс алгоритма поиска Бойера-Мура """

    def __init__(self):
        """ Конструктор класса """
        self.reg = True  # Не учитывать регистры по умолчанию(пользователю будет предложен выбор

    def s_table(self, st):
        """
        Метод записывающий все символы входящей строки в словарь
        (формирование таблицы смещений)
        """

        S = set()  # Инициализация множества
        M = len(st)
        d = {}

        for i in range(M - 2, -1, -1):  # итерации с предпоследнего символа
            if st[i] not in S:  # если символа нет в множестве
                d[st[i]] = M - i - 1  # В словарь d записываем значение с соотв. ключем в виде символа st[i]
                S.add(st[i])  # И добавляем символ в множество S

        if st[M-1] not in S:  # Если последнего символа строки нет в множестве S
            d[st[M-1]] = M  # Записываем в словарь d последний символ со значением длинны строки

        # Ключ со значением смещения длинны строки (если при поиске подстроки в множестве нет проверяемого символа)
        d['*'] = M

        return d

    def find_string(self, main_s, st):
        """ Метод находит подстроку в строке, возвращает результат поиска и индекс вхождения """

        if self.reg:
            # Приведение входящих строк к общему регистру
            main_s = str.lower(main_s)
            st = str.lower(st)

        N = len(main_s)  # Длинна главной строки
        M = len(st)  # Длинна подстроки
        d = self.s_table(st)  # Формирование таблицы  смещений

        if N >= M:
            i = M-1  # Счетик текущего символа строки

            while i < N:  # Пока не сравним всю главную строку с подстрокой
                k = 0  # Счетчик отхода назад при сравнении (для главной строки)
                flBreak = False  # Переменная для остановки проверки

                for j in range(M-1, -1, -1):  # Счетчик текущего символа подстроки
                    if main_s[i-k] != st[j]:  # Если символы не совпали
                        if j == M-1:  # Если не совпал последний символ
                            off = d[main_s[i]] if d.get(main_s[i], False) else d['*']  # off - определение смещения
                            # исходя из словаря d
                        else:
                            off = d[st[j]]  # Смещение если не совпал не последний символ

                        i += off  # Перенос счетчика на значение смещения
                        flBreak = True
                        break

                    k += 1

        # Вывод результатов
                if not flBreak:
                    print("Исходная строка: \"" + main_s + "\"\n" + "Искомая строка: \"" + st + "\"\n" + f"Образ найден по индексу: {i-k+1}")
                    break
            else:
                print('Образ не найден.')
        else:
            print('Образ не найден.')
