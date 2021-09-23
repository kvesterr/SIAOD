def check(file):
    f = open(file, 'r').readlines()
    count = int(f[0])
    stack = []

    for i in range(1, count + 1):
        if f[i][0] == 'A':# Добавляем проект
            stack.append(str(f[i][3]))
        else: # Закрываем проект
            if len(stack) > 0:
                if stack[len(stack) - 1] == str(f[i][4]):
                    stack.pop()
            else:
                return 'No'
    if len(stack) > 0:
        return 'No'
    else:
        return 'Yes'

if __name__ == '__main__':
    print(check('in.txt'))