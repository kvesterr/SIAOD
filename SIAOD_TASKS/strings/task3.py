def count_of_conc(string):
    counter = 0
    res = [string[i: j] for i in range(len(string))
           for j in range(i + 1, len(string) + 1)]
    lfl = []
    for i in res:
        if (len(i) % 2) == 0:
            s1 = i[0:(len(i)//2)]
            s2 = i[(len(i)//2):len(i)]
            if s1 == s2:
                if not (lfl.__contains__(s1+s2)):
                    counter += 1
                    lfl.append(s1+s2)
    return counter

if __name__ == '__main__':
    print('Введите строку:')
    s1 = input()
    print(count_of_conc(s1))
