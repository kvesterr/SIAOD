class deque:
    """Класс реализующий структуру данных Дек"""

    def __init__(self, arg):
        """Конструктор класса Дек"""
        self.deque = list(arg)

    def __str__(self):
        """Метод возвращающий Дек в виде строки"""
        return str(self.deque)

    def is_empty(self):
        """Метод проверяющий содержит ли Дек элементы"""
        if len(self.deque) == 0:
            return True
        else:
            return False

    def add_start(self, obj):
        """Метод добавления элемента в начало Дека"""
        self.deque.insert(0,obj)

    def remove_start(self):
        """Метод удаления элемента из начала Дека"""
        if self.is_empty():
            return -1
        temp = self.deque[0]
        self.deque.remove(self.deque[0])
        return temp

    def add_end(self, obj):
        """Метод добавления элемента в конец Дека"""
        self.deque.append(obj)

    def remove_end(self):
        """Метод удаления элемента с конца дека"""
        return self.deque.pop()
