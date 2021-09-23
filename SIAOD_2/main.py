import hashlib
import time
from random import randint
from datetime import datetime
from FibonacciSearch import FibonacciSearch
from TheQueenProblem import TheQueenProblem
from Tree import Tree
from TreeNode import TreeNode
from BinarTreeNode import BinarTreeNode
from BinarTree import BinarTree
from collections import deque


# Binary_Search
def binarySearch(array, value):
    lowBound = 0
    upBound = len(array) - 1
    while lowBound <= upBound:
        center = (lowBound + upBound) // 2
        if array[center] == value:
            return center
        elif array[center] > value:
            upBound = center - 1
        elif array[center] < value:
            lowBound = center + 1
    return -1


# Interpolation_Search
def interpolation_search(lst, val):
    low = 0
    high = len(lst) - 1
    search_res = False
    index = -1

    while (low <= high) and (val >= lst[low]) and (val <= lst[high]) and not search_res:
        middle = low + int(((high - low) / (lst[high] - lst[low])) * (val - lst[low]))
        guess = lst[middle]
        if guess == val:
            search_res = True
            index = middle
        if guess < val:
            low = middle + 1
        if guess > val:
            high = middle - 1
    return index


# Простое рехэширование
def simple_re_hash(sl, value):
    temp = str(value)
    i = 1
    while True:
        if hash(temp) not in sl.keys():
            sl[hash(temp)] = value
            break
        else:
            while hash(temp) + i in sl.keys():
                i += 1
            sl[hash(temp) + i] = value
            break


# Рехэширование с помощью псевдослучайных чисел
def rand_re_hash(sl, value):
    temp = value
    while True:
        if hash(temp) not in sl.keys():
            sl[hash(temp)] = value
            break
        else:
            temp += str(randint(0, 1000))


# Метод цепочек
def chain_method(sl, value):
    temp = value
    if hash(temp) in sl.keys():
        if isinstance(sl[hash(temp)], deque):
            sl[hash(temp)].append(value)
        else:
            a = sl[hash(temp)]
            sl[hash(temp)] = deque([a, value])
    else:
        sl[hash(value)] = value


# Pre-Order
def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


# Post_Order
def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)


# In_Order
def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)


# Get_Info
def get_info(a, rnd):
    if not (a.find_and_get(rnd).rod == None):
        print('Родитель: ' + str(a.find_and_get(rnd).rod.value))
    else:
        print('Родитель: Отсутствует')
    if not (a.find_and_get(rnd).left == None):
        print('Левый потомок: ' + str(a.find_and_get(rnd).left.value))
    else:
        print('Левый потомок: Отсутствует')
    if not (a.find_and_get(rnd).right == None):
        print('Правый потомок: ' + str(a.find_and_get(rnd).right.value))
    else:
        print('Правый потомок: Отсутствует')

# Процедуры



# Бинарный поиск

# value = randint(-1000, 1000)
# print('Бинарный поиск.')
# print('Диапазон - [-1000, 1000]')
# print('Ищем элемент со значением ' + str(value))
# list = [randint(-1000,1000) for a in range(2000)]
# list = sorted(list)
# start = time.monotonic_ns()
# search_result = binarySearch(list, value)
# final = time.monotonic_ns() - start
# if not(search_result == -1):
#     print('Элемент со значением ' + str(value) + ' находится под индексом - ' + str(search_result))
#     print('Времени на поиск затрачено - ' + str(final) + ' наносекунд')
# else:
#     print('Элемента со значением ' + str(value) + ' нет в списке')



# Бинарное дерево

# a = BinarTree(BinarTreeNode(50))
# for i in range(25):
#     a.add(randint(0,100))
# print('Бинарное дерево.\n')
# pre_order(a.root)
# rnd = randint(0,100)
# while not(a.find(rnd) == -1):
#     rnd = randint(0, 100)
# print('\nДобавим к дереву элемент ' + str(rnd))
# a.add(rnd)
# print('\nОбновленное дерево:')
# pre_order(a.root)
# print('\nНайдем путь к элементу от корня дерева')
# print('Путь: ' + a.find(rnd))
# get_info(a, rnd)
# print('\nНайдем элемент по пути: Влево, Вправо, Вправо; и получим информацию о нем')
# get_info(a, a.root.left.right.right.value)
# print('\nТеперь удалим элемент ' + str(rnd) + ' и ' + str(a.root.left.right.right.value) + ' из дерева')
# a.remove(rnd)
# a.remove(a.root.left.right.right.value)
# print('\nОбновленное дерево:')
# pre_order(a.root)
# print('\nУдалим корень дерева')
# a.remove(50)
# print('\nОбновленное дерево:')
# pre_order(a.root)



# Фибоначчиев

# value = randint(-1000, 1000)
# print('Фибоначчиев.')
# print('Диапазон - [-1000, 1000]')
# print('Ищем элемент со значением ' + str(value))
# list = [randint(-1000,1000) for a in range(2000)]
# list = sorted(list)
# start = time.monotonic_ns()
# fsearch = FibonacciSearch()
# search_result = fsearch.search(list, value)
# final = time.monotonic_ns() - start
# if not(search_result == -1):
#     print('Элемент со значением ' + str(value) + ' находится под индексом - ' + str(search_result))
#     print('Времени на поиск затрачено - ' + str(final) + ' наносекунд')
# else:
#     print('Элемента со значением ' + str(value) + ' нет в списке')



# Интерполяционный

# value = randint(-1000, 1000)
# print('Интерполяционный.')
# print('Диапазон - [-1000, 1000]')
# print('Ищем элемент со значением ' + str(value))
# list = [randint(-1000,1000) for a in range(2000)]
# list = sorted(list)
# start = time.monotonic_ns()
# search_result = interpolation_search(list, value)
# final = time.monotonic_ns() - start
# if not(search_result == -1):
#     print('Элемент со значением ' + str(value) + ' находится под индексом - ' + str(search_result))
#     print('Времени на поиск затрачено - ' + str(final) + ' наносекунд')
# else:
#     print('Элемента со значением ' + str(value) + ' нет в списке')

















# # Простое рехэширование
# print('Простое рехэширование')
# print('Ввод строки:')
# str1 = input()
# print('Ввод строки:')
# str2 = input()
# print('Ввод строки:')
# str3 = input()
# sl = dict()
# simple_re_hash(sl, str1)
# simple_re_hash(sl, str2)
# simple_re_hash(sl, str3)
# print('Значения и их ключи:')
# stroka = str(sl.items())
# stroka = stroka.replace('dict_items([','').replace('])','')
# print(stroka)






# # Рехэширование с помощью псевдослучайных чисел
# print('Рехэширование с помощью псевдослучайных чисел')
# print('Ввод строки:')
# str1 = input()
# print('Ввод строки:')
# str2 = input()
# print('Ввод строки:')
# str3 = input()
# sl = dict()
# rand_re_hash(sl, str1)
# rand_re_hash(sl, str2)
# rand_re_hash(sl, str3)
# print('Значения и их ключи:')
# stroka = str(sl.items())
# stroka = stroka.replace('dict_items([','').replace('])','')
# print(stroka)





# # Метод цепочек
# print('Метод цепочек')
# print('Ввод строки:')
# str1 = input()
# print('Ввод строки:')
# str2 = input()
# print('Ввод строки:')
# str3 = input()
# sl = dict()
# chain_method(sl, str1)
# chain_method(sl, str2)
# chain_method(sl, str3)
# print('Значения и их ключи:')
# stroka = str(sl.items())
# stroka = stroka.replace('dict_items([','').replace('deque','').replace(')])',')')
# print(stroka)




# a = TheQueenProblem()
# a.try_queen(0)
# st = ''
# for i in range(0,8):
#     for j in range(0, 8):
#         if a.field[i][j] == -1:
#             st += ' X '
#         else:
#             st += ' . '
#     print(st)
#     st = ''




# Стандартный поиск
value = randint(-1000, 1000)
print('Стандартный поиск.')
print('Диапазон - [-1000, 1000]')
print('Ищем элемент со значением ' + str(value))
list = [randint(-1000,1000) for a in range(2000)]
list = sorted(list)
start = time.monotonic_ns()
search_result = 0
for i in range(0,len(list)):
    if list[i] == value:
        search_result = i
        break
final = time.monotonic_ns() - start
if not(search_result == 0):
    print('Элемент со значением ' + str(value) + ' находится под индексом - ' + str(search_result))
    print('Времени на поиск затрачено - ' + str(final) + ' наносекунд')
else:
    print('Элемента со значением ' + str(value) + ' нет в списке')
