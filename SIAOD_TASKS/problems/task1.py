def max_p(list):
    if (len(list) < 3) or (len(list) > 10000):
        return 0
    max_list = []
    temp_max = list[0]
    while len(list) > 0:
        while len(max_list) < 3:
            for i in list:
                if (i < 1) or (i > 10**6):
                    return 0
                if i > temp_max:
                    temp_max = i
            if list.__contains__(temp_max):
                list.remove(temp_max)
                max_list.append(temp_max)
                temp_max = 0
            else:
                temp = list.pop()
                max_list.append(temp)
        max = max_element(max_list)
        max_list.remove(max)
        if (max_list[0] + max_list[1]) > max:
            max_p = max + max_list[0] + max_list[1]
            return max_p
    return 0


def max_element(list):
    max = 1
    for i in list:
        if i > max:
            max = i
    return max


def min_element(list):
    min = 1
    for i in list:
        if i < min:
            min = i
    return min

if __name__ == '__main__':
    arr = []
    print('Введите массив.')
    inp = input()
    while not (inp == 'stop'):
        try:
            inp = int(inp)
            if inp == int(inp):
                arr.append(inp)
        except:
            print('Введеное значение не является числом')
        inp = input()
    print(max_p(arr))
