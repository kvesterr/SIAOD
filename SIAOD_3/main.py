import time

import Boyer
import Cnoot

print('Методы поиска:\n1. Кнута-Морриса-Пратта\n2. Бойера-Мура\n3. Стандартный поиск')

inst = input()

if inst == '1':
    cnoot = Cnoot.Cnoot()
    print('Учитывать регистр при поиске?\n1. Да\n2. Нет')
    if input() == '1':
        cnoot.reg = False
    print('Введите основную строку:')
    ms = input()
    print('Введите подстроку:')
    ps = input()
    start_time = time.time()
    cnoot.find_string(ms, ps)
    print('На поиск затрачено ' + str(time.time() - start_time) + ' сек.')

elif inst == '3':
    print('Введите основную строку:')
    ms = input()
    print('Введите подстроку:')
    ps = input()
    start_time = time.time()
    print(str.find(ms,ps))
    print('На поиск затрачено ' + str(time.time() - start_time) + ' сек.')

elif inst == '2':
    boyer = Boyer.Boyer()
    print('Учитывать регистр при поиске?\n1. Да\n2. Нет')
    if input() == '1':
        boyer.reg = False
    print('Введите основную строку:')
    ms = input()
    print('Введите подстроку:')
    ps = input()
    start_time = time.time()
    boyer.find_string(ms, ps)
    print('На поиск затрачено ' + str(time.time() - start_time) + ' сек.')
