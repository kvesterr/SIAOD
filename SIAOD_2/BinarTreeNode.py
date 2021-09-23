class BinarTreeNode:

    #Конструктор
    def __init__(self, value):
        self.value = value
        self.rod = None
        self.left = None
        self.right = None

    def setValue(self, value):
        self.value = value

    def setRod(self, node):
        self.rod = node

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def getValue(self):
        return self.value

    def getRod(self):
        return self.rod

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right