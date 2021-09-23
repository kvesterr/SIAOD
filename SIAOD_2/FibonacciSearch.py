class FibonacciSearch:
    def __init__(self):
        self.i = 0
        self.q = 0
        self.p = 0
        self.stop = False

    #FibonacciNum
    def F(self, val):
        a = val
        if val > 1:
            a = 0
            arr = [0, 1]
            for i in range(2, val + 1):
                a = arr[i - 2] + arr[i - 1]
                arr.append(a)
        return a

    def startInit(self, array):
        self.stop = False
        k = 0
        n = len(array)
        while (self.F(k+1) < n):
            k += 1
        m = self.F(k+1)-(n+1)
        self.i = self.F(k)
        self.q = self.F(k-2)
        self.p = self.F(k-1)

    def upIndex(self):
        if self.p == 1:
            self.stop = True
        self.i = self.i + self.q
        self.p = self.p - self.q
        self.q = self.q - self.p

    def downIndex(self):
        if self.q == 0:
            self.stop = True
        self.i = self.i - self.q
        temp = self.q
        self.q = self.p - self.q
        self.p = temp

    def search(self, array, value):
        self.startInit(array)
        result_index = -1
        while not self.stop:
            if self.i < 0:
                self.upIndex()
            elif self.i >= len(array):
                self.downIndex()
            elif array[self.i] == value:
                result_index = self.i
                break
            elif value < array[self.i]:
                self.downIndex()
            elif value > array[self.i]:
                self.upIndex()
        return result_index