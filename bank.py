class bank:
    def __init__(self):
        self.acc_num=3456767463
        self.balance=0
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self, amount):
        if(amount>self.balance):
            print("Insufficient balance")
        else:
            self.balance-=amount
    def display_balance(self):
        print("Account balance=",self.balance)
user1=bank()
user1.deposit(1000)
user1.display_balance()
user1.withdraw(2000)
user1.withdraw(500)
user1.display_balance()
