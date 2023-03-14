class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def to_dict(self):
        return {'account_number': self.account_number, 'balance': self.balance}

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance

    def edit_balance(self, new_balance):
        self.balance = new_balance
        return self.balance

    def get_balance(self):
        return f'{self.balance}'

    def get_account(self):
        return len(self.account_number)

    def __str__(self):
        return f'Account number: {self.account_number}\nBalance: {self.balance}\n'

    def __repr__(self):
        return f'account_number={self.account_number},balance={self.balance}'
