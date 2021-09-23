class deque:

    def __init__(self, arg):
        self.deque = list(arg)

    def __str__(self):
        return str(self.deque)

    def is_empty(self):
        if len(self.deque) == 0:
            return True
        else:
            return False

    def add_start(self, obj):
        self.deque.insert(0,obj)

    def remove_start(self):
        if self.is_empty():
            return -1
        temp = self.deque[0]
        self.deque.remove(self.deque[0])
        return temp

    def add_end(self, obj):
        self.deque.append(obj)

    def remove_end(self):
        return self.deque.pop()