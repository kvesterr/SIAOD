import itertools

def can_win(s1, s2):
    """ Функция возвращает ответ может ли строка s1 победить строку s2 """
    if not (len(s1) == len(s2)):
        return False
    if (len(s1) > 10**5) or (len(s1) < 1) or (len(s2) > 10**5) or (len(s2) < 1):
        return False
    else:
        n = len(s1)

        # Инициализация всевозможных перестановок s1 и s2
        perm1 = itertools.permutations(s1)
        perm2 = itertools.permutations(s2)

        # Проход по всевозможным перестановкам и комбинациям входных строк
        for a in perm1:
            for b in perm2:
                s1_syms = []  # Список символов первой строки
                s2_syms = []  # Список символов второй строки
                s1_wins = 0  # Счетчик побед символов
                s2_wins = 0  # ^

                # Запись символов в списки
                for z in a:
                    s1_syms.append(z)
                for z in b:
                    s2_syms.append(z)

                for i in range(0, len(s1_syms)):
                    c = s1_syms[i]  # Текущий рассматриваемый символ первой строки
                    d = s2_syms[i]  # Текущий рассматриваемый символ второй строки

                    if ord(c) >= ord(d):  # В зависимости от того какой символ побеждает добавляем к соотв. счетчику 1
                        s1_wins += 1
                        if s1_wins == n:  # Если все символы строки победили
                            return True
                    else:
                        s1_wins = 0
                    if ord(c) <= ord(d):
                        s2_wins += 1
                        if s2_wins == n:  # Если все символы строки победили
                            return True
                    else:
                        s2_wins = 0

    return False

if __name__ == '__main__':
    print('Введите первую строку:')
    s1 = input()
    print('Введите вторую строку:')
    s2 = input()
    print(can_win(s1, s2))
