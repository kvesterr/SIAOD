from BinarTreeNode import BinarTreeNode

class BinarTree:

    #Конструктор
    def __init__(self, node):
        self.root = node

    #Метод добавления значения в дерво
    def add(self, value):
        node = self.root
        while True:
            if value < node.value:
                if node.left:
                    node = node.left
                else:
                    node.left = BinarTreeNode(value)
                    node.left.rod = node
                    break
            elif value > node.value:
                if node.right:
                    node = node.right
                else:
                    node.right = BinarTreeNode(value)
                    node.right.rod = node
                    break
            elif value == node.value:
                break

    #Метод поиска в дереве по значению, возвращает инструкцию(string)
    def find(self, value):
        instruction = []
        instruction_string = ''
        node = self.root
        while True:
            if node.value == value:
                for i in instruction:
                    if i == 0:
                        instruction_string += 'Влево, '
                    else:
                        instruction_string += 'Вправо, '
                instruction_string = (instruction_string + ';').replace(', ;', '')
                return instruction_string
                break
            if node.value > value:
                if node.left:
                    node = node.left
                    instruction.append(0)
                else:
                    return -1
            if node.value < value:
                if node.right:
                    node = node.right
                    instruction.append(1)
                else:
                    return -1

    #Метод поиска узла в дереве по значению, возвращает узел
    def find_and_get(self, value):
        node = self.root
        while True:
            if node.value == value:
                return node
                break
            if node.value > value:
                if node.left:
                    node = node.left
                else:
                    return -1
            if node.value < value:
                if node.right:
                    node = node.right
                else:
                    return -1

    #Метод удаления элемента по значению
    def remove(self, value):
        node = self.root
        arr = [self.root]
        while True:
            if node.value > value:
                if node.left:
                    node = node.left
                else:
                    return -1
            elif node.value < value:
                if node.right:
                    node = node.right
                else:
                    return -1
            elif node.value == value:
                array = self.copyToArray([], self.root)
                array.remove(value)
                newself = BinarTree(BinarTreeNode(array[0]))
                for i in range(1, len(array)):
                    newself.add(array[i])
                break
        self.root = newself.root

    #Вспомогательный метод записывающий все элементы дерева в массив
    def copyToArray(self, array, node):
        arr = array
        if node:
            arr.append(node.value)
            self.copyToArray(arr, node.left)
            self.copyToArray(arr, node.right)
        return arr
