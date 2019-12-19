# 7. Pennies for Pay
# Write a program that calculates the amount of money a person would earn over a period
# of time if his or her salary is one penny the first day, two pennies the second day, and
# continues to double each day. The program should ask the user for the number of days.
# Display a table showing what the salary was for each day, and then show the total pay at
# the end of the period. The output should be displayed in a dollar amount, not the number of pennies.

def main():
    days = int(input("Enter the number of days to calculate for: "))

    pennies = 1

    for _ in range(1, days):
        pennies = pennies * 2

    if pennies < 100:
        print(f"You entered {pennies:} pennies.")
    else:
        dollars = pennies/100
        print(f"You entered {dollars:.2f} dollars.")

main()
