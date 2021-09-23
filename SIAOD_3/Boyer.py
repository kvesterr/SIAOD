# Класс алгоритма поиска Бойера-Мура
class Boyer:
    def __init__(self):
        self.reg = True

    # Метод записывающий все символы входящей строки в словарь
    def s_table(self, st):
        S = set()
        M = len(st)
        d = {}

        for i in range(M - 2, -1, -1):  # итерации с предпоследнего символа
            if st[i] not in S:  # если символ еще не добавлен в таблицу
                d[st[i]] = M - i - 1
                S.add(st[i])

        if st[M-1] not in S:
            d[st[M-1]] = M

        d['*'] = M
        return d

    # Метод находит подстроку в строке, возвращает результат поиска и индекс вхождения
    def find_string(self, main_s, st):
        if self.reg == True:
            main_s = str.lower(main_s)
            st = str.lower(st)

        N = len(main_s)
        M = len(st)
        d = self.s_table(st)

        if N >= M:
            i = M-1

            while i < N:
                k = 0
                j = 0
                flBreak = False
                for j in range(M-1, -1, -1):
                    if main_s[i-k] != st[j]:
                        if j == M-1:
                            off = d[main_s[i]] if d.get(main_s[i], False) else d['*']
                        else:
                            off = d[st[j]]

                        i += off
                        flBreak = True
                        break

                    k += 1

                if not flBreak:
                    print("Исходная строка: \"" + main_s + "\"\n" + "Искомая строка: \"" + st + "\"\n" + f"Образ найден по индексу: {i-k+1}")
                    break
            else:
                print('Образ не найден.')
        else:
            print('Образ не найден.')