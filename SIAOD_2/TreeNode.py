class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.i = 1

    #Добавление элемента к узлу
    def add(self,value):
        a = 9
        if value < self.value:
            self.left = TreeNode(value)
            a = 0
        else:
            self.right = TreeNode(value)
            a = 1
        self.i = self.i + 1
        return a

    #Нахождение места и получение инструкции
    def findAndGetInstruction(self, val):
        #мусор
        copy_var = TreeNode(self.value)
        copy_var.left = self.left
        copy_var.right = self.right
        copy_var.i = self.i
        #
        navigator = self
        instruction = [9]
        while (navigator.left)or(navigator.right):
            if val < navigator.value:
                    navigator.goLeft()
                    instruction.append(0)
            else:
                    navigator.goRight() #Этот метод стирает корень класса дерева
                    instruction.append(1)
        if (not(navigator.left))and(not(navigator.right)):
            if navigator.value != None:
                a = navigator.add(val)
                instruction.append(a)
        #мусор
        self.value = copy_var.value
        self.left = copy_var.left
        self.right = copy_var.right
        self.i = copy_var.i
        #
        return instruction

    def goLeft(self):
        if self.left:
            self.value = self.left.value
            self.right = self.left.right
            self.i = self.left.i
            self.left = self.left.left
        else:
            self.value = None
            self.right = None
            self.left = None

    def goRight(self):
        if self.right:
            self.value = self.right.value
            self.left = self.right.left
            self.i = self.right.i
            self.right = self.right.right
        else:
            self.value = None
            self.right = None
            self.left = None