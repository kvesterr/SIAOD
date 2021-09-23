def thc(s1):
        chislo10 = int(s1)
        for base in range(2, 10**9):
            if not (str(chislo10).__contains__(str(base))):
                for i in range(chislo10):
                    num = in_any_base(i, base)
                    if str(num) == str(chislo10):
                        D = i
                        B = -1
                        if (base >= 2) and (base <= 10 ** 9):
                            B = base
                        x = D//2
                        if (x >= 2) and (x <= 10 ** 9):
                            X = x
                        else:
                            X = -1
                        if (not (B == -1)) and (not (X == -1)):
                            return 'B = ' + str(B) + ', X = ' + str(X)
        return -1

def in_any_base(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

if __name__ == '__main__':
    s1 = input('Введите строку из десятичных цифр.\n')
    print(thc(s1))
