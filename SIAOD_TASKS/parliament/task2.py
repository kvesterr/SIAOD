def count_versh(N):
    """ Функция принимает количество углов (N-угольник), возвращает минимальное количество вершин для составления другого
    правильного многоугольника """
    if (N < 3) or (N > 10**12):
        return 'Число не входит в заданный диапазон.'
    else:
        if N%2 == 0:
            return  str(N // 2)
        else:
            return str((N+1) // 2)

if __name__ == '__main__':
    N = int(input('Введите количество граней многоугольника.\n'))
    print(count_versh(N) + ' - минимальное количество граней для составления правильного многоугольника')
