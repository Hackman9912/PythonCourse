# 8. So)ware Sales
# A software company sells a package that retails for $99. Quantity discounts are given according to the following table:
# ______________________
# |Quantity    |Discount|
# |10-19       |20%     |
# |20-49       |30%     |
# |50-99       |40%     |
# |100 or more |50%     |
# ______________________
# Write a program that asks the user to enter the number of packages purchased. The program should then display the amount 
# of the discount (if any) and the total amount of the purchase after the discount

package_price = 99
packages = 0
def main():
    global packages
    packages = int(input("Enter the number of packages you purchased "))
    discount()

def discount():
    if packages >= 10 and packages <= 19:
        discount = .8
        print("You qualify for a 20% discount")
        cost = (99*discount)*packages
        print("Your cost is $", cost)
    elif packages >= 20 and packages <=49:
        discount = .7
        print("You qualify for a 30% discount")
        cost = (99*discount)*packages
        print("Your cost is $", cost)
    elif packages >= 50 and packages <= 99:
        discount = .6
        print("You qualify for a 40% discount")
        cost = (99*discount)*packages
        print("Your cost is $", cost)
    elif packages >= 100:
        discount = .5
        print("You get a whopping 50% discount!")
        cost = (99*discount)*packages
        print("Your cost is $", cost)
    else:
        discount = 0
        print("Not enough packages for a discount.")


main()