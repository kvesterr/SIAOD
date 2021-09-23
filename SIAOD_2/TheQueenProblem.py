import numpy as np


class TheQueenProblem:
    # Конструктор
    def __init__(self):
        self.field = np.zeros((8,8))
        for i in range(0,8):
            for j in range(0,8):
                self.field[i][j] = 0


    # Метод пытающийся вставить ферзь на уровень i
    def try_queen(self, i):
        result = False
        for j in range(0,8):
            if self.field[i][j] == 0:
                self.set_queen(i, j)
                if i == 7:
                    result = True
                else:
                    result = self.try_queen(i+1)
                    if result == False:
                        self.reset_queen(i, j)
            if result == True:
                break
        return result


    # Метод устанавливающий ферзь на координаты i,j
    def set_queen(self, i, j):
        for x in range(0,8):
            self.field[x][j] += 1
            self.field[i][x] += 1
            foo = j - i + x
            if (foo >= 0)and(foo < 8):
                self.field[x][foo] += 1
            foo = j + i - x
            if (foo >= 0) and (foo < 8):
                self.field[x][foo] += 1
        self.field[i][j] = -1


    # Метод удаляющий ферзь с координат i,j
    def reset_queen(self, i, j):
        for x in range(0,8):
            self.field[x][j] -= 1
            self.field[i][x] -= 1
            foo = j - i + x
            if (foo >= 0)and(foo < 8):
                self.field[x][foo] -= 1
            foo = j + i - x
            if (foo >= 0) and (foo < 8):
                self.field[x][foo] -= 1
        self.field[i][j] = 0