class A:
    def __init__(self, number: int, balance: int):
        self.number = number
        self.balance = balance

    def set_a(self, summ: int):
        self.balance += summ

    def get_a(self):
        return self.balance


a1 = A(1, 0)
a1.set_a(100)
print(a1.get_a())