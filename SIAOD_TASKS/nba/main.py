import player

if __name__ == '__main__':
    file = open('in.txt', 'r').readlines()
    out_string = ''
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    for i in range(len(file)):
        if i == 0:
            count = int(file[0])
        else:
            if a == 0:
                a = int(file[i])
            elif b == 0:
                b = int(file[i])
            elif c == 0:
                c = int(file[i])
            elif d == 0:
                d = int(file[i])
            elif e == 0:
                e = int(file[i])
            else:
                pl = player.player(a, b, c, d, e)
                out_string += str(pl.get_player_category()) + '\n'
                a = int(file[i])
                b = 0
                c = 0
                d = 0
                e = 0
    pl = player.player(a, b, c, d, e)
    out_string += str(pl.get_player_category()) + '\n'

    open('out.txt', 'w').write(out_string)