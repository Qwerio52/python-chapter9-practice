# 9.2 银行账户管理程序
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"{self.owner} 存款 {money} 元，当前余额：{self.balance}")
        else:
            print("存款金额必须大于0！")

    def withdraw(self, money):
        if 0 < money <= self.balance:
            self.balance -= money
            print(f"{self.owner} 取款 {money} 元，当前余额：{self.balance}")
        else:
            print("取款失败：余额不足或金额非法")

    def query(self):
        print(f"{self.owner} 当前余额：{self.balance}")
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.02):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.balance += interest
        print(f"结算利息：新增利息 {interest:.2f}，余额 {self.balance:.2f}")


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, over_draft=1000):
        super().__init__(owner, balance)
        self.over_draft = over_draft

    def withdraw(self, money):
        if 0 < money <= self.balance + self.over_draft:
            self.balance -= money
            print(f"{self.owner} 取款 {money} 元，余额 {self.balance}（允许透支上限：{self.over_draft}）")
        else:
            print("取款失败：超出可透支额度")


if __name__ == "__main__":
    sa = SavingsAccount("小明", 1000, 0.03)
    sa.add_interest()
    ca = CheckingAccount("小红", 500, 800)
    ca.withdraw(1000)