# 3. Budget Analysis
# Write a program that asks the user to enter the amount that he or she has budgeted for amonth. 
# A loop should then prompt the user to enter each of his or her expenses for the month, and keep a running total. 
# When the loop finishes, the program should display theamount that the user is over or under budget.

def main():

    budget = float(input("Enter the amount you have budgeted this month: "))
    total = 0
    cont = "Y"
    
    while cont == "Y" or cont == "y":
        expense = float(input("Enter the expense amount you want tabulated from the budget: "))
        cont = str(input("Enter y to continue or any other key to quit: "))
        total += expense

    if total < budget:
        bottom_line = budget - total
        print(f"You are {bottom_line:.2f} under budget.")
    elif total > budget:
        bottom_line = total - budget
        print(f"You are {bottom_line:.2f} over budget.")
    else:
        print("Your expenses matched your budget.")

main()