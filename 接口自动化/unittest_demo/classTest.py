__author__ = 'Administrator'

class Test:
    pass

class Test01:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multi(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

class Test02(Test01):
    pass
