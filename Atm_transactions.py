users_credentials = {"Raj": 123, "Latha": 234, "Prasanth": 567, "Kavya": 906}

class SignIn:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        if self.name in users_credentials and users_credentials[self.name] == self.password:
            print("You're successfully logged in")
        else:
            print("The username or password is incorrect")

class SignUp:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        if self.name not in users_credentials:
            users_credentials[self.name] = self.password
            print("User successfully registered")
        else:
            print("Username already exists. Choose a different username.")

class BankAccount:
    def __init__(self, account_number):
        self.account_number = str(account_number)
        self.balance = 0

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def deposit(self, amount):
        self.balance += amount

def transfer_amount(account_1, account_2, amount):
    try:
        account_1.withdraw(amount)
        account_2.deposit(amount)
        return True
    except ValueError as e:
        print(str(e))
        return False

name = input("Enter your username: ")
password = int(input("Enter your password: "))
signIn_instance = SignIn(name, password)

if name not in users_credentials or users_credentials[name] != password:
    print("Please signUp")
    name = input("Enter a new username: ")
    password = int(input("Enter a new password: "))
    signUp_instance = SignUp(name, password)

print("Users acount details for transaction")
user_1_acc_no = input("Enter User 1 account number: ")
user_1_balance = int(input("Enter User 1 Balance amount: "))
user_2_acc_no = input("Enter User 2 account number: ")
user_2_balance = int(input("Enter User 2 Balance amount: "))
user_1 = BankAccount(user_1_acc_no)
user_2 = BankAccount(user_2_acc_no)
user_1.deposit(user_1_balance)
user_2.deposit(user_2_balance)
print("Amount to be transferred from user_1 to user_2")
transaction_amount = int(input("Enter the amount to be transferred: "))

print("Balance of User 1: {}/-".format(user_1.get_balance()))
print("Balance of User 2: {}/-".format(user_2.get_balance()))
print("Transfer result:", transfer_amount(user_1, user_2, transaction_amount))
print("Balance of User 1: {}/-".format(user_1.get_balance()))
print("Balance of User 2: {}/-".format(user_2.get_balance()))

