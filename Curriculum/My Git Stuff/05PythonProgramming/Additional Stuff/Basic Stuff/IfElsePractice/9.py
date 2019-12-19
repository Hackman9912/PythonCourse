# 9. Shipping Charges
# The Fast Freight Shipping Company charges the following rates:
# Weight of Package Rate per Pound
# 2 pounds or less                              $1.10
# Over 2 pounds but not more than 6 pounds      $2.20
# Over 6 pounds but not more than 10 pounds     $3.70
# Over 10 pounds                                $3.80
# Write a program that asks the user to enter the weight of a package and then displays the
# shipping charges.

def main():
    pound = float(input("Enter the weight of your package in pounds: "))
    calc(pound)

def calc(num1):
    if num1 <= 2:
        total = num1*1.1
    elif num1 > 2 and num1 <= 6:
        total = num1*2.2
    elif num1 > 6 and num1 <= 10:
        total = num1*3.7
    else:
        total = num1*3.8
    print(f"The shipping charge for your package is: {total:.2f}")

main()