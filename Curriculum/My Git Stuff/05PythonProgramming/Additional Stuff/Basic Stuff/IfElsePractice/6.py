# 6. Change for a Dollar Game 
# Create a change-counting game that gets the user to enter the number of coins required to make exactly one dollar. The program should prompt the user to enter the number of pennies, nickels,
#  dimes, and quarters. If the total value of the coins entered is equal to one dollar, the program should congratulate the user for winning the game. Otherwise, the program should display a 
# message indicating whether the amount entered was more than or less than one dollar.

PENNY = .01
NICKEL = .05
DIME = .10
QUARTER = .25
DOLLAR = 1.00

def main():
    
    print("Put the number of pennies, nickels, dimes and quarters needed to make exactly one dollar.")
    total = amount()

    if total == DOLLAR:
        print("Congratulations, you did the thing")
    elif total < DOLLAR:
        print(f"You entered, {total:.2f} which is less than a dollar.")
    else:
        print(f"You entered, {total:.2f} which is more than a dollar.")

def amount():
    pennies = float(input("Plese put the number of pennies you would use: "))*PENNY
    nickels = float(input("Please put the number of nickels you would use: "))*NICKEL 
    dimes = float(input("Please put the number of dimes you would use: "))*DIME
    quarters = float(input("Please put the number of quarters you would use:"))*QUARTER 
    return pennies+nickels+dimes+quarters

main()