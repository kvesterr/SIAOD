def max_chislo(arr):
    """ Функция составляет из списка входных чисел, максимально вохможное число по значению """
    # Инициализация стеков, в стеках храню пару [Число(str), Стоимость(int)]
    stck1 = []
    stck2 = []
    # Проходимся по исходному массиву и сортируем ценные числа в стэк
    for i in range(0, len(arr)):
        worth = 0
        s1 = str(arr[i])
        for a in s1:
            worth += int(a)
        worth = worth/len(s1)  # Рассчет ценности числа
        if len(stck1) <= 0:  # Если stck1 пуст просто записываем в него рассматриваемое число
            stck1.append([s1, worth])

        # Загонем в stck1 числа с ценностью от наименьшей к наибольшей
        else:
            last = stck1.pop()
            if worth > last[1]:  # При этом условии записываем рассматриваемое число в stck1
                stck1.append(last)
                stck1.append([s1, worth])

            elif worth < last[1]:  # При этом условии перегоняем элементы из stck1 в stck2 пока не найдем подходящее
                # место
                while worth < last[1]:
                    stck2.append(last)
                    try:
                        last = stck1.pop()
                        if worth > last[1]:
                            stck1.append(last)
                            stck1.append([s1, worth])
                            while len(stck2) > 0:
                                stck1.append(stck2.pop())

                        elif worth == last[1]:  # При этом условии сравниваем количество цифр в числах, большую ценность
                            # имеет короткое
                            if len(s1) < len(last[0]):  # Тут у рассматриваемого числа ценность больше
                                stck1.append(last)
                                stck1.append([s1, worth])
                            elif len(s1) > len(last[0]):
                                stck1.append([s1, worth])
                                stck1.append(last)
                            else:
                                if int(s1) > int(last[0]):
                                    stck1.append(last)
                                    stck1.append([s1, worth])
                                else:
                                    stck1.append([s1, worth])
                                    stck1.append(last)
                            while len(stck2) > 0:
                                stck1.append(stck2.pop())

                    except:
                        stck1.append([s1, worth])
                        while len(stck2) > 0:
                            stck1.append(stck2.pop())
                        break

            elif worth == last[1]:  # При этом условии сравниваем количество цифр в числах, большую ценность имеет
                # короткое
                if len(s1) < len(last[0]):  # Тут у рассматриваемого числа ценность больше
                    stck1.append(last)
                    stck1.append([s1, worth])
                elif len(s1) > len(last[0]):
                    stck1.append([s1, worth])
                    stck1.append(last)
                else:
                    if int(s1) > int(last[0]):
                        stck1.append(last)
                        stck1.append([s1, worth])
                    else:
                        stck1.append([s1, worth])
                        stck1.append(last)

    big_chislo = ''
    while len(stck1) > 0:
        big_chislo += str(stck1.pop()[0])

    return big_chislo


if __name__ == '__main__':
    arr = []
    inp = input()
    while not (inp == 'stop'):
        try:
            inp = int(inp)
            if (inp > 10 ** 9) or (inp < 0):
                print('Введеное значение должно быть от 0 до 10^9.')
            else:
                if inp == int(inp):
                    arr.append(inp)
        except:
            print('Введеное значение не является числом')
        inp = input()

    if not (len(arr) < 1) or (len(arr) > 100):
        print(max_chislo(arr))
    else:
        print('Длинна массива неверна')
