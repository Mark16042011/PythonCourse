class BankAccount:
    def __init__(self, account_number: int, balance: int):
        self.account_number = account_number
        self.balance = balance

    def add(self, amount: int):
        return self.balance + amount

    def withdraw(self, amount: int):
        if self.balance >= amount:
            return self.balance - amount
        else:
            return "Недостаточно средств"


ivan = BankAccount(1,1000)


print(ivan.withdraw(1001))
