class stack:
    """Класс реализующий структуру данных Стек"""

    def __init__(self, arg):
        """Конструктор класса Стек"""
        self.stack = list(arg)

    def is_empty(self):
        """Метод проверяющий содержит ли Стек элементы"""
        if len(self.stack) == 0:
            return True
        else:
            return False

    def add(self, obj):
        """Метод добавления элемента в Стек"""
        self.stack.insert(0,obj)

    def remove(self):
        """Метод удаления элемента из Стека"""
        if len(self.stack) == 0:
            return -1
        else:
            temp = self.stack[0]
            self.stack.remove(self.stack[0])
            return temp

    def look(self):
        """Метод возвращающий последний элемент занесенный в Стек, при этом сам элемент из Стека не удаляется"""
        temp = self.remove()
        if not (temp == -1):
            self.add(temp)
        return temp
