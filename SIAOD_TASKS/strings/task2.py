def find_pol(string):
    """ Функция принимает на вход строку, возвращает самую длинную полиндромную подстроку """
    pol_list = []
    res = [string[i: j] for i in range(len(string))  # res - коллекция всевозможных подстрок string
           for j in range(i + 1, len(string) + 1)]
    max = 0

    for i in res:  # i - текущая рассматриваемая подстрока
        if i == i[::-1]:  # проверка подстроки на полиндром
            if len(i) > max:
                max = len(i)
                if len(pol_list) > 0:
                    pol_list.pop()
                pol_list.append(i)
    if len(pol_list) > 0:
        return pol_list.pop()
    else:
        return 'No polindroms'

if __name__ == '__main__':
    print('Введите строку:')
    s1 = str(input())
    print(find_pol(s1))
