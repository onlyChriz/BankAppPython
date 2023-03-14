import json
from Customer import Customer
from Account import Account


class Bank:
    def __init__(self):
        self.customers = []
        self.current_user = None

    def save_customers(self):
        file_write = open("bank.txt", "w")

        for customer in self.customers:
            j_dict = customer.customer_to_dictionary()
            j_string = json.dumps(j_dict)

            file_write.write(j_string)
            file_write.write("\n")
        file_write.close()

    def clear_list(self):
        self.customers.clear()
        return

    def load_customer(self):
        self.customers.clear()
        file = open("bank.txt", "r")
        content = file.readlines()
        if len(content) > 0:
            for each in content:
                j_string = json.loads(each)
                customer = Customer(j_string["user"], j_string["password"])
                self.customers.append(customer)
                for acc in j_string["accounts"]:
                    account_number = acc["Account_number"]
                    balance = acc["Balance"]
                    customer.account_list.append(Account(account_number, balance))
        file.close()

    def get_customers(self):
        if not self.customers:
            print("No customers in this Bank")
            return
        for cust in self.customers:
            print(f'{cust}')

    def get_customer(self, user=None):
        if user is None and self.current_user is not None:
            print(self.current_user)
            for acc in self.current_user.account_list:
                print(acc)
            return
        for cust in self.customers:
            if cust.user == user:
                print(cust)
                for acc in cust.account_list:
                    print(acc)
        if user is None:
            return "set a user!"

    def change_customer_password(self, user, new_password):
        for cust in self.customers:
            if cust.user == user:
                cust.password = new_password
                print("password successfully changed")
                return True
        return False

    def add_customer(self, user, password):
        return self.customers.append(Customer(user, password))

    def remove_customer(self, user):
        for name in self.customers:
            if name.user == user:
                self.customers.remove(name)
                print(f'success in removing account: {user}')
                return True
        return False

    def login(self, username, password):
        if self.current_user is None:
            for customer in self.customers:
                if customer.user == username and customer.password == password:
                    self.current_user = customer
                    customer.logged_in = True
                    print("Logged in successfully")
                    return True
            print("Incorrect login information")
            return False
        return f'log out first user first'

    def logout(self):
        if self.current_user:
            self.current_user.logged_in = False
            self.current_user = None
            print('Logged out successfully')
            return True
        else:
            print('No user is currently logged in')
            return False

    def add_account(self, balance=0):
        return self.current_user.add_account(balance)

    def deposit(self, account_number, amount):
        return self.current_user.deposit(account_number, amount)

    def withdraw(self, account_number, amount):
        return self.current_user.withdraw(account_number, amount)

    def edit_balance(self, account_number, amount):
        return self.current_user.edit_balance(account_number, amount)

    def get_accounts(self):
        return self.current_user.get_accounts()

    def get_account(self, account_number):
        print(f'account: {account_number}\nbalance: {self.current_user.get_account(account_number)}')
        return

    def remove_account(self, account_number):
        return self.current_user.remove_account(account_number)
