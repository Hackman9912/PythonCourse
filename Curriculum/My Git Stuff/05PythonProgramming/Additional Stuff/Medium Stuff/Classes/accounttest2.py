# This program demonstrates the BankAccount clss
import bankaccount2

def main():
     # Get the starting balance
     start_balance = float(input("Enter your starting balance: "))

     # Create a BankAccount object:
     savings = bankaccount2.BankAccount(start_balance)

     # Deposit the users paycheck
     pay = float(input("How much were you paid this week? "))
     print("I will deposit that into your account. ")
     savings.deposit(pay)

     # Display the balance the ,.2f shows commas in thousands and only 2 decimals
     print(savings)

     # Get the amount to withdraw
     cash = float(input('Enter the amount of money you want to withdraw. '))
     print('I will withdraw that from your account')
     savings.withdraw(cash)

     # Display the balance the ,.2f shows commas in thousands and only 2 decimals
     print(savings)

# Call main
main()