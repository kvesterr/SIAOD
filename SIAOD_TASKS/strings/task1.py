import itertools

def can_win(s1, s2):
    if not (len(s1) == len(s2)):
        return False
    if (len(s1) > 10**5) or (len(s1) < 1) or (len(s2) > 10**5) or (len(s2) < 1):
        return False
    else:
        n = len(s1)
        perm1 = itertools.permutations(s1)
        perm2 = itertools.permutations(s2)
        for a in perm1:
            for b in perm2:
                s1_syms = []
                s2_syms = []
                s1_wins = 0
                s2_wins = 0
                for z in a:
                    s1_syms.append(z)
                for z in b:
                    s2_syms.append(z)

                for i in range(0, len(s1_syms)):
                    c = s1_syms[i]
                    d = s2_syms[i]
                    if ord(c) >= ord(d):
                        s1_wins += 1
                        if s1_wins == n:
                            return True
                    else:
                        s1_wins = 0
                    if ord(c) <= ord(d):
                        s2_wins += 1
                        if s2_wins == n:
                            return True
                    else:
                        s2_wins = 0

    return False

if __name__ == '__main__':
    print('Введите первую строку:')
    s1 = input()
    print('Введите вторую строку:')
    s2 = input()
    print(can_win(s1, s2))
