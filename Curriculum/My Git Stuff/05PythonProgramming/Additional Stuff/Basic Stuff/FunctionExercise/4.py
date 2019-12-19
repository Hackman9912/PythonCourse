# 4. Automobile Costs
# Write a program that asks the user to enter the monthly costs for the following expenses incurred from operating his or her automobile: 
# loan payment, insurance, gas, oil, tires, andmaintenance. 
# The program should then display the total monthly cost of these expenses,and the total annual cost of these expenses
loan = 0.0
insurance = 0.0
gas = 0.0
oil = 0.0
tire = 0.0
mx = 0.0

def main():
    global loan, insurance, gas, oil, tire, mx

    print("Enter the monthly loan cost")
    loan = getcost()
    print("Enter the monthly insurance cost")
    insurance = getcost()
    print("Enter the monthly gas cost")
    gas = getcost()
    print("Enter the monthly oil cost")
    oil = getcost()
    print("Enter the monthly tire cost")
    tire = getcost()
    print("Enter the monthly maintenance cost")
    mx = getcost()
    total()



def getcost():
    return float(input())


def total():
    monthly_amount = loan+insurance+gas+oil+tire+mx
    print("Your monthly costs are $", monthly_amount)
    annual_amount = monthly_amount*12
    print("Your annual cost is $", annual_amount)


main()