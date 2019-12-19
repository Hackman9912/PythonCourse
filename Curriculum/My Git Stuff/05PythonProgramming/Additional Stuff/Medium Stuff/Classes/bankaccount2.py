# The BankAccount class simulates a bank account

class BankAccount:

    # The __init__ method accepts an argument for the account's balance. It is assigned to the __balance attribute:
    def __init__(self, balance):
        self.__balance = balance

    # The deposit method makes a deposit into the account
    def deposit(self, amount):
        self.__balance += amount

    # The withdraw method withdraws an amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Error: Insufficient Funds.")

    # The get_balance method returns the account balance
    def get_balance(self):
        return self.__balance

    # The __str__ method returns a string indicating the objects state
    def __str__(self):
        return f'The balance is ${self.__balance:,.2f}'