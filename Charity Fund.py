class Charity_Fund:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        if self.balance < 0:
            print('You got a deficit of ' + str(self.balance))
        return self.balance

    def spend_fund(self, amount):
        self.balance -= amount

    def save_fund(self, amount):
        self.balance += amount

    def invest(self, amount):
        self.balance *= (1 + amount)

    def is_danger(self):
        if self.balance < 5000:
            print('Danger you have ' + str(self.balance) + ' left')
            return self.balance < 5000


charity = Charity_Fund(1000)
charity.spend_fund(200)
print(charity.get_balance())
charity.save_fund(300)
print(charity.get_balance())
charity.invest(0.5)
print(charity.get_balance())