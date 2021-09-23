from TreeNode import TreeNode
class Tree:
    def __init__(self, node):
        self.root = node
        self.array = [self.root]

    #Метод возвращающий инструкции для принимаемого значения value
    def getInstruction(self,node):
        instruction = self.root.findAndGetInstruction(node)
        return instruction

    #Добавить элемент с использованием инструкции
    def addWithInstruction(self, inst, node):
        var = 0
        for i in range(1, len(inst)):
            if inst[i] == 0:
                var = self.getTreeIndexToGo(0,var)
            elif inst[i] == 1:
                var = self.getTreeIndexToGo(1, var)
        while len(self.array) <= var:
            self.array.append(-228420)
        self.array[var] = node
        a = self.getOlderIndex(var)
        if (var%2) == 0:
            if self.array[int(a)] != -228420:
                self.array[int(a)].right = node
        else:
            if self.array[int(a)] != -228420:
                self.array[int(a)].left = node

    #Метод возвращающий индекс ячейки в которую нужно перейти из текущей - (a)
    def getTreeIndexToGo(self, case, a):
        if case == 0:
            b = (a*2) + 1
        elif case == 1:
            b = (a*2) + 2
        return b

    #Метод возвращающий индекс ячейки родителя
    def getOlderIndex(self,a):
        if (a!=0):
            if (a%2) == 0:
                a = (a - 2)/2
            else:
                a = (a-1)/2
        return a

    #Быстрый метод добавляющий элемент value в дерево
    def add(self, value):
        canwe = True
        for i in range(0,len(self.array)):
            if self.array[i] != -228420:
                if self.array[i].value == value:
                    canwe = False
        if canwe == True:
            a = TreeNode(value)
            self.addWithInstruction(self.getInstruction(value), a)

    #Метод возвращающий индекс передаваемого элемента
    def getIndex(self, value):
        j = -228420
        for i in range(0,len(self.array)):
            if self.array[i] != -228420:
                if self.array[i].value == value:
                    j=i
        return j

    #Метод удаляющий передаваемое значение из дерева
    def remove(self, value):
        a = self.getIndex(value)
        if a != -228420:
            self.array[a] = -228420
            if a%2 == 0:
                self.array[int(self.getOlderIndex(a))].right = None
            else:
                self.array[int(self.getOlderIndex(a))].left = None
        self.updateTree()

    #Метод "обновления" дерева
    def updateTree(self):
        arr = [self.root.value]
        for i in range(1,len(self.array)):
            if self.array[i] != -228420:
                arr.append(self.array[i].value)
        self = Tree(TreeNode(arr[0]))
        for i in range(1,len(arr)):
            self.add(arr[i])

    #Метод выводящий на экран информацию об передаваемом значении
    def printIndexOf(self,val):
        index = self.getIndex(val)
        if index != -228420:
            left = 'Отсутствует'
            right = 'Отсутствует'
            rod = 'Отсутствует'
            if index != 0:
                rod = str(self.array[int(self.getOlderIndex(index))].value)
            if self.array[index].left:
                left = str(self.array[index].left.value)
            if self.array[index].right:
                right = str(self.array[index].right.value)
            return 'Элемент ' + str(val) + ' находится под индексом: ' + str(index) + "\nРодитель: " + rod + "\nЛевый потомок: " + left + "\nПравый потомок: " + right
        else:
            return 'В дереве нет элемента со значением ' + str(val)