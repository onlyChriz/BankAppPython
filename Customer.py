from Account import Account


class Customer:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.account_list = []
        self.acc_count = 1
        self.logged_in = False

    def customer_to_dictionary(self):
        return {
            "user": self.user,
            "password": self.password,
            "acc_count": self.acc_count,
            "accounts": [
                {"Account_number": account.account_number, "Balance": account.balance}
                for account in self.account_list
            ],
        }

    def get_customer(self):  # for bank class
        return self.user

    def add_account(self, balance=0):
        self.account_list.append(Account(self.acc_count, balance))
        self.acc_count += 1

    def deposit(self, account_number, amount):
        for account in self.account_list:
            if account.account_number == account_number:
                account.deposit(amount)
                print(f"deposit success! \nBalance: {account.get_balance()}")

    def withdraw(self, account_number, amount):
        for account in self.account_list:
            if account.account_number == account_number:
                return f'amount left: {account.withdraw(amount)}'
        return "Account not found"

    def edit_balance(self, account_number, amount):
        for account in self.account_list:
            if account.account_number == account_number:
                account.edit_balance(amount)
                return f'edit balance success'

    def get_accounts(self):
        for account in self.account_list:
            print(account)

    def get_account(self, account_number):
        for account in self.account_list:
            if account.account_number == account_number:
                return account.get_balance()

        return "Account not found"

    def remove_account(self, account_number):
        for account in self.account_list:
            if account.account_number == account_number:
                self.account_list.remove(account)
                print(f'success in removing account: {account_number}')

    def __str__(self):
        return f'user: {self.user}\nPassword: {self.password}\n'

    def __repr__(self):
        return f'user={self.user}, password={self.password}'
