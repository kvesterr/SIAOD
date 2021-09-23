def find_pol(string):
    pol_list = []
    res = [string[i: j] for i in range(len(string))
           for j in range(i + 1, len(string) + 1)]
    max = 0
    for i in res:
        if i == i[::-1]:
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
