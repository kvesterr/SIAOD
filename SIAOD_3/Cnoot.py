# Класс алгоритма поиска КМП
class Cnoot:
    def __init__(self):
        self.reg = True


    # Метод поиска наибольшего суффикса во входящей строке
    def find_biggest_suffix(self, st):
        j = 0
        i = 1
        p = [0]*len(st)

        while i < len(st):
            if st[j] == st[i]:
                p[i] = j+1
                i += 1
                j += 1
            else:
                if j == 0:
                    p[i] = 0
                    i += 1
                else:
                    j = p[j-1]

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
            if main_string[i] == f_string[j]:
                i += 1
                j += 1
                if j == m:
                    print('Образ найден.')
                    break
            else:
                if j > 0:
                    j = p[j-1]
                else:
                    i+=1

            if i == n:
                print('Образ не найден.')
                break