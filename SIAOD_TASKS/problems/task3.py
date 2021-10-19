def sort_d(A):
    """ Функция сортирует диагонали матрицы """
    try:
        m = len(A)
        n = len(A[0])
        if (m > 100) or (m < 1) or (n > 100) or (n < 1):
            return print('Неверный размер матрицы. (1 <= m, n <= 100)')

        temp_list = []
        closed_list = []  # Список просмотренных элементов

        for i in range(0, m):
            for j in range(0, n):
                if (A[i][j] < 1) or (A[i][j] > 100):
                    return print('В матрице содержится неподходящее число. (1 <= mat[i][j] <= 100)')
                if not (closed_list.__contains__([i, j])):  # Проверяем только те ячейки которых нет в списке
                    # закрытых(просмотренных)
                    temp_list.append(A[i][j])
                    new_i = i + 1
                    new_j = j + 1
                    closed_list.append([i, j])
                    while (new_i < m) and (new_j < n) and (not (closed_list.__contains__([new_i, new_j]))):  # Пока по
                        # диогонали есть ячейки записываем их в временный список
                        closed_list.append([new_i, new_j])
                        temp_list.append(A[new_i][new_j])
                        new_i += 1
                        new_j += 1
                    temp_list.sort()  # Сортируем временный список
                    new_i = i
                    new_j = j

                    for k in range(0, len(temp_list)):  # Заменяем диагональ в матрице только что отсортированной
                        # диагональю
                        A[new_i][new_j] = temp_list[k]
                        new_i += 1
                        new_j += 1
                    temp_list = []

        print(A)
    except():
        print('Что то пошло не так...')

if __name__ == '__main__':
    mat = [[62, 95, 2, 58, 9, 79], [11, 21, 10, 91, 13, 14], [86, 27, 7, 42, 5, 4], [19, 27, 69, 21, 68, 41], [92, 25, 98, 24, 51, 2]]
    print('Исходная матрица:\n' + str(mat) + '\n')
    print('Отсортированная матрица.')
    sort_d(mat)
