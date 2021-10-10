import deque
import stack


def name_count(name):
    """Возвращает абстрактный коэффициент стоимости названия(книги)"""
    return ord(name[0]) * 100 + ord(name[3]) * 10 + ord(name[6])


# Задание 1
def run_task1():
    """Отсортировать названия книг в алфавитном порядке, используя два дека"""
    # Чтение файла
    str_list = open('in.txt', encoding='utf8').readlines()

    # Удаление из названия книги символа переноса строки
    for name in str_list:
        str_list[str_list.index(name)] = str(name).replace('\n', '')

    # Инициализация деков
    deq1 = deque.deque([])  # В этом деке хранятся имена с меньшей стоимостью, идут слева направо от меньшего к большему
    deq2 = deque.deque([])  # В этом деке хранятся имена с большей стоимостью, такая же логика ^

    sr = int  # Переменная от которой будем отталкиваться

    # Распределение всех имен по двум декам
    for name in str_list:
        if deq1.is_empty() and deq2.is_empty():  # Если оба дека пустые
            deq1.add_start(name)  # Записываем имя в первый дек
            sr = name_count(name)  # Тут от этого элемента будем отталкиваться,
            # далее sr будет хранить элемент дека с меньшей стоимостью
        else:
            # Алгоритм примерной сортировки внутри двух деков
            if len(deq1.deque) > 0:  # Если первый дек не пустой
                last = deq1.remove_end()  # Переменная которую мы рассматриваем для сравнения, берем с конца первого
                # дека
            deq1.add_end(last)  # Возвращаем на место взятое значение для переменной
            if name_count(name) < sr:  # Если стоимость рассматриваемого имени меньше текущего меньше элемента дека
                deq1.add_start(name)  # Добавляем его в левый край дека
            elif name_count(name) > name_count(last):  # Если стоимость рассматриваемого имени больше текущего большего
                # элемента дека
                deq1.add_end(name)  # Добавляем его в правый край
            else:  # Если стоимость имени не подошла под условия выше, выбираем для него место во втором деке
                # Тут все также как с первым деком
                if deq2.is_empty():
                    deq2.add_start(name)
                    sr2 = name_count(name)
                else:
                    # Тут примерно такое же распределение как в первом деке
                    last2 = deq2.remove_end()
                    deq2.add_end(last2)
                    if name_count(name) < sr2:
                        deq2.add_start(name)
                    else:
                        deq2.add_end(name)

            # Запись в переменные sr и sr2 элементов с меньшей стоимостью из первого и второго дека
            if not deq1.is_empty():
                sr = deq1.remove_start()
                deq1.add_start(sr)
                sr = name_count(sr)
            if not deq2.is_empty():
                sr2 = deq2.remove_start()
                deq2.add_start(sr2)
                sr2 = name_count(sr2)

    # Слияние двух деков
    in_memory = []
    first_shag = True
    # С помощью цикла ниже, вставляем все неотсортированные элементы из второго в первый дек, и параллельно
    # досортировываем первый дек
    while not deq2.is_empty():
        if first_shag:  # Если прошлый элемент вставлен/Первый проход цикла
            name = deq2.remove_start()  # Элемент с меньшей стоимостью второго дека
            first_shag = False
        while not first_shag:
            first = deq1.remove_start()  # Элемент с меньшей стоимостью первого дека
            deq1.add_start(first)
            # Находим место
            if name_count(name) < name_count(first):  # Если элемент второго дека меньше элемента первого(место найдено)
                deq1.add_start(name)
                deq1.deque = list(in_memory) + list(deq1.deque)
                first_shag = True
                in_memory = []
            else:  # Записываем в память элемент с меньшей стоимостью первого дека, чтобы далее найти место для вставки
                in_memory.append(deq1.remove_start())

    # Вывод в файл
    f = open('out.txt', 'w', encoding='utf8')
    for i in deq1.deque:
        f.write(i + '\n')


# Задание 2
def run_task2():
    """Расшифровать сообщение использую дек с шифровкой"""
    # Дек с шифровкой
    deq = deque.deque(['r', 't', 's', 'y', 'p', 'o', 'x', 'f', 'm', 'b', 'q',
                       'd', 'a', 'g', 'n', 'v', 'u', 'i', 'k', 'h', 'j', 'l', 'z', 'c', 'e', 'w'])

    # Чтение файла
    text = open('in2.txt', 'r', encoding='utf8').read()
    translate = ''  # Строка для хранение расшифрованного сообщения
    # Проход по сообщению
    for a in text:
        if not (a == ' '):  # Если символ не пробел
            last = deq.remove_end()  # Переменная last для просмотра последнего элемента дека
            deq.add_end(last)  # Возвращаем деку взятое значение для last
            if not (last == a):  # Если последний элемент дека не равен текущему просматривоемому символу
                while not (last == a):  # Пока последний элемент дека не равен текущему просматривоемому символу
                    move = deq.remove_end()  # Пододвигаем дек-шифр и берем его последнее значение
                    deq.add_start(move)
                    last = move
            else:
                move = deq.remove_end()  # Двигаем дек-шифр еще разок...
                deq.add_start(move)
                last = move
            if (last == a):  # Если последний элемент дека соответствует просматриваемому символу
                move = deq.remove_end()  # Двигаем
                deq.add_start(move)  # Последний
                move = deq.remove_end()  # Раз!
                deq.add_start(move)
                translate += str(move)  # Записываем в строку translate расшифрованый символ
        else:
            translate += ' '

    open('out2.txt', 'w').write(translate)


# Задание 3
def run_task3():
    """Переложить N дисков с стержня A на стержень B используя стержень C"""
    def hanoi(n, pin1, pin2, list_of_stacks):
        if n == 1:  # Условие выхода из рекурсии
            print(f"Переложить диск 1 со стержня {pin1} на {pin2}")
            list_of_stacks[pin2 - 1].add(list_of_stacks[pin1 - 1].remove())  # Перекладываем (в стеках)
        else:  # Если количество дисков не равно одному
            hanoi(n - 1, pin1, 6 - pin1 - pin2, list_of_stacks)  # Запускаем рекурсивный алгоритм
            print(f"Переложить диск {n} со стержня {pin1} на {pin2}")
            list_of_stacks[pin2 - 1].add(list_of_stacks[pin1 - 1].remove())  # Перекладываем (в стеках)
            hanoi(n - 1, 6 - pin1 - pin2, pin2, list_of_stacks)  # И снова рекурсия

    list_of_stacks = [stack.stack([]), stack.stack([]), stack.stack([])]
    n = int(input("Введите кол-во дисков\n"))
    # Надеваем на стержень диски
    for i in range(n, 0, -1):
        list_of_stacks[0].add(i)
    hanoi(n, 1, 2, list_of_stacks)  # n - количество дисков; с первого стержня на второй, list_of_stacks - текущее
    # положение стержней


# Задание 4
def run_task4():
    """Проверка баланса круглых скобок с помощью стека"""
    text = open('in4.txt', 'r', encoding='utf8').read()
    stk1 = stack.stack([])
    stk2 = stack.stack([])
    for a in text:
        if a == '(':
            stk1.add(1)
        if a == ')':
            stk2.add(1)
    if len(stk1.stack) == len(stk2.stack):
        print('Баланс скобок соблюден')
    else:
        print('Баланс скобок не соблюден')


# Задание 5
def run_task5():
    """Проверка баланса квадратных скобок с помощью дека"""
    text = open('in5.txt', 'r', encoding='utf8').read()
    dq1 = deque.deque([])
    dq2 = deque.deque([])
    for a in text:
        if a == '[':
            dq1.add_start(1)
        if a == ']':
            dq2.add_start(1)
    if len(dq1.deque) == len(dq2.deque):
        print('Баланс скобок соблюден')
    else:
        print('Баланс скобок не соблюден')


# Задание 6
def run_task6():
    """Напечатать сначала цифры, затем буквы, и после все остальные символы из файла используя стек"""
    stck = stack.stack([])  # Стек прочих символов
    syms = stack.stack([])  # Стек букв
    cyfs = stack.stack([])  # Стек цифр
    text = open('in6.txt', 'r', encoding='utf8').read()

    # Проход по файлу и добавление всех элементов в соответствующие стеки
    for a in text:
        if (ord(a.lower()) > 1071) and (ord(a.lower()) < 1104):
            syms.add(a)
        elif (ord(a) > 47) and (ord(a) < 58):
            cyfs.add(a)
        else:
            stck.add(a)

    # Просто реверс данных из одного стека в другой
    cyfs2 = stack.stack([])
    syms2 = stack.stack([])
    stck2 = stack.stack([])
    for i in range(0, len(cyfs.stack)):
        cyfs2.add(cyfs.remove())
    for i in range(0, len(syms.stack)):
        syms2.add(syms.remove())
    for i in range(0, len(stck.stack)):
        stck2.add(stck.remove())

    # Вывод
    print(cyfs2.stack)
    print(syms2.stack)
    print(stck2.stack)


# Задание 7
def run_task7():
    """Напечатать сначала все отрицательные числа, а затем все остальные, используя дек"""
    # Читаем файл
    text = open('in7.txt', 'r').read()
    # Инициализация дека
    deq = deque.deque([])
    # Временная перменная
    temp_s = ''

    # Пробегаемся по считанной строке, считываем числа и распределяем используя дек
    for a in text:
        # Считывание числа
        if a == '-':
            temp_s += a
        if (ord(a) > 47) and (ord(a) < 58):
            temp_s += a
        if a == ' ':
            if int(temp_s) < 0:
                deq.add_end(int(temp_s))
            else:
                deq.add_start(int(temp_s))
            temp_s = ''

    # Распределение числа
    if int(temp_s) < 0:
        deq.add_end(int(temp_s))
    else:
        deq.add_start(int(temp_s))

    otr_deq = deque.deque([])
    a = deq.remove_end()
    while a < 0:  # Пока мы читаем отрицательный числа с конца дека
        otr_deq.add_start(a)  # Добавляем эти числа в "отрицательный дек"
        if len(deq.deque) > 0:  # Если основной дек не пуст то
            a = deq.remove_end()  # Читаем конец этого дека
    pol_deq = deque.deque([])
    while a > -1:  # Если мы прочитали все отрицательный числа
        pol_deq.add_end(a)  # Тут все то же самое
        if len(deq.deque) > 0:
            a = deq.remove_end()
        else:
            a = -2

    # Выводим числа
    print(otr_deq.deque)
    print(pol_deq.deque)


# Задание 8
def run_task8():
    """Записать строки исходного файла в обратном порядке"""
    # Чтение файла
    text = open('in8.txt', 'r', encoding='utf8').readlines()

    # Инициализация стека, и добавление в него всех строк файла
    stck = stack.stack([])
    for a in text:
        stck.add(a)

    pr_s = ''
    # Запись в строку строки файла в обратном порядке
    for i in range(0, len(stck.stack)):
        s = str(stck.remove())
        if s.__contains__('\n'):
            pr_s += s
        else:
            pr_s += s + '\n'

    # Вывод
    print(pr_s)


# Задание 9
def run_task9():
    """Вычисление значения логического выражения с помощью стека"""
    # Инициализация двух стеков
    stack1 = stack.stack([])
    stack2 = stack.stack([])

    # Чтение файла
    text = open('in9.txt', 'r', encoding='utf8').read()
    for a in text:
        if a == ')':  # Если текущий символ строка(высчитываем последние данные)
            z = stack1.remove()  # В z записываем первое выражение
            x = stack1.remove()  # В x записываем второе выражение
            c = stack2.remove()  # В c записываем операцию
            while not ((c == 'A') or (c == 'O') or (c == 'X') or (c == 'N')):
                c = stack2.remove()  # Просто корректно записываем операцию в c

            # Выбор действия, и запись вычисленного выражения в стек выражений
            if c == 'A':
                stack1.add(z and x)
            if c == 'O':
                stack1.add(z or x)
            if c == 'X':
                if z == x:
                    stack1.add(False)
                else:
                    stack1.add(True)
            if c == 'N':
                stack1.add(x)
                stack1.add(not z)

        else:  # Если текущий символ выражение (записываем)
            if a == 'T':
                stack1.add(True)
            elif a == 'F':
                stack1.add(False)
            else:
                stack2.add(a)

    # Вывод вычисленного выражения
    print(stack1.remove())


# Задание 10
def run_task10():
    """Вычисление значения формулы с использованием стека"""
    # Функция определения минимума
    def min(a, b):
        if a <= b:
            return a
        else:
            return b

    # Функция определения максимума
    def max(a, b):
        if a > b:
            return a
        else:
            return b

    # Инициализация стеков
    stack1 = stack.stack([])
    stack2 = stack.stack([])

    # Чтение файла
    text = open('in10.txt', 'r', encoding='utf8').read()
    sbros = False  # Переменная для корректной записи чисел во время прохода по строке выражения

    # Проход по строке выражения
    for a in text:

        # Если символ текущей итерации ")", то вычисляем предыдущие значения по предыдущей формуле
        if a == ')':
            # Записываем в a и b два предыдущих значения
            a = stack1.remove()
            b = stack1.remove()
            # Записываем в z предыдущую операцию
            z = stack2.remove()

            # Пока в z не записана конкретная операция нахождения минмума или макимума
            while not ((z == 'M') or (z == 'N')):
                z = stack2.remove() # Записываем в z следующую операцию из стека операций

            # Вычисление максимума
            if z == 'M':
                stack1.add(max(int(a), int(b)))
            # Вычисление минимума
            elif z == 'N':
                stack1.add(min(int(a), int(b)))
            sbros = False

        # Иначе распределяем в стеки символы
        else:
            # Записываем в первый стек числа
            if (ord(a) > 47) and (ord(a) < 58) and (sbros == False):
                stack1.add(a)
                sbros = True
            # Это условие создано для записи чисел а не только цифр т.к. запись ведется посимвольно
            elif (ord(a) > 47) and (ord(a) < 58) and (sbros == True):
                temp = stack1.remove() + a
                stack1.add(temp)
            # Во второй стек остальные символы(операции)
            else:
                stack2.add(a)
                sbros = False

    # Вывод результата вычисления
    print(str(stack1.remove()))


# Задание 11
def run_task11():
    """Проверить является ли содержимое формулой корректного вида"""
    # Инициализация стеков
    stack1 = stack.stack([])
    stack2 = stack.stack([])
    # Чтение файла
    text = open('in11.txt', 'r', encoding='utf8').read()
    # Проход по строке выражения
    for a in text:
        # В первый стек записываем значения "x", "y", "z"
        if (a == 'x') or (a == 'y') or (a == 'z'):
            stack1.add(a)
        # Во второй стек записываем остальные операции
        else:
            stack2.add(a)

    count_of_xs = 0  # Переменная содержащая количество переменных "x", "y" и "z" в единственном экземпляре
    temp = stack1.remove()  # Вытаскиваем из стека переменных элемент для просмотра
    b1 = False  # Переменная содержащая статус наличия в выражении "x"
    b2 = False  # Переменная содержащая статус наличия в выражении "y"
    b3 = False  # Переменная содержащая статус наличия в выражении "z"
    # Пока первый стек содержит переменные
    while not (temp == -1):
        # Запись данных о наличии переменных(x, y, z)
        if temp == 'x':
            b1 = True
            count_of_xs += 1
        if temp == 'y':
            b2 = True
            count_of_xs += 1
        if temp == 'z':
            b3 = True
            count_of_xs += 1
        temp = stack1.remove()

    bool1 = b1 and b2 and b3  # Переменная содержащая статус наличия всех трех переменных x, y и z

    # Подсчет баланса скобок и соответствия количества операций к количеству переменных
    # Инициализация переменных хранящих количество вышеупомянутых данных
    ch1 = 0
    ch2 = 0
    ch3 = 0
    temp = stack2.remove()  # Переменная для просмотра второго стека
    while not (temp == -1):
        if temp == '(':
            ch1 += 1
        elif temp == ')':
            ch2 += 1
        else:
            ch3 += 1
        temp = stack2.remove()

    # bool2 - Баланс скобок
    if ch1 == ch2:
        bool2 = True
    else:
        bool2 = False

    # bool3 - Баланс операций и переменных
    if (count_of_xs - ch3) == 1:
        bool3 = True
    else:
        bool3 = False

    # Вывод итогового результата является ли выражение корректным
    print((bool1 == True) and (bool2 == True) and (bool3 == True))


if __name__ == '__main__':
    print('Лабораторная работа 4.\nВыберите задание:\n1. ' + str(run_task1.__doc__) + '\n2. ' + str(run_task2.__doc__)
           + '\n3. ' + str(run_task3.__doc__) + '\n4. ' + str(run_task4.__doc__) + '\n5. ' + str(run_task5.__doc__) + '\n6. ' +
          str(run_task6.__doc__) + '\n7. ' + str(run_task7.__doc__) + '\n8. ' + str(run_task8.__doc__) + '\n9. ' + str(run_task9.__doc__)
           + '\n10. ' + str(run_task10.__doc__) + '\n11. ' + str(run_task11.__doc__))
    nomer = input()

    if nomer == '1':
        run_task1()
    elif nomer == '2':
        run_task2()
    elif nomer == '3':
        run_task3()
    elif nomer == '4':
        run_task4()
    elif nomer == '5':
        run_task5()
    elif nomer == '6':
        run_task6()
    elif nomer == '7':
        run_task7()
    elif nomer == '8':
        run_task8()
    elif nomer == '9':
        run_task9()
    elif nomer == '10':
        run_task10()
    elif nomer == '11':
        run_task11()
