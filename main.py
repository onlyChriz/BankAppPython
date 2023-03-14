from Bank import Bank

# Creation of bank and accounts
b = Bank()
b.add_customer("username", "password")
b.add_customer("k", "hej")

print("'account for username'\n")

b.login("username", "password")
b.add_account(200)
b.add_account(200)
b.add_account(200)
b.deposit(1, 100)
print("")
b.get_customer()

print("___________________________\n")
print("'account for k'\n")

b.logout()
b.login("k", "hej")

b.add_account(2)
b.add_account(5)
b.add_account(2000)
b.deposit(1, 100)
b.withdraw(3, 4)
print("")
b.get_customer()
print("___________________________\n")
print("'change password for user k'\n")
b.change_customer_password("k", "då")
print("___________________________\n")

b.get_customers()

print("___________________________\n")
print("'balance change account k'\n")
b.edit_balance(3, 100)
b.get_accounts()

print("___________________________\n")
print("'balance for k'\n")

b.get_account(3)
print("___________________________\n")
print("'saving customers, accounts then clearing the customer list and printing the list'\n")

b.save_customers()
b.clear_list()
b.get_customers()

print("___________________________\n")
print("'loading customers and accounts'\n")
b.load_customer()
b.get_customers()

print("___________________________\n")
print("'removing customer k'\n")
b.remove_customer("k")
print("___________________________\n")
print("'fetching all customers'\n")
b.get_customers()
