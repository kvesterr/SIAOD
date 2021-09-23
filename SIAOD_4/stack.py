class stack:

    def __init__(self, arg):
        self.stack = list(arg)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def add(self, obj):
        self.stack.insert(0,obj)

    def remove(self):
        if len(self.stack) == 0:
            return -1
        else:
            temp = self.stack[0]
            self.stack.remove(self.stack[0])
            return temp

    def look(self):
        temp = self.remove()
        if not (temp == -1):
            self.add(temp)
        return temp