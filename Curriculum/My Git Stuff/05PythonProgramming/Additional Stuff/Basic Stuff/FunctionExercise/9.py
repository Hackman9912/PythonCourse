# 9. Paint Job Estimator
# A painting company has determined that for every 115 square feet of wall space, one gallon of paint and eight hours of laborwill be required. 
# The company charges $20.00 perhour for labor. Write a program that asks the user to enter the square feet of wall space tobe painted and the price of 
# the paint per gallon. The program should display the following data:
# • The number of gallons of paint required gallons
# • The hours of labor required hours
# • The cost of the paint paint total
# • The labor charges labor
# • The total cost of the paint job

def main():
    paint = lambda x : x/115
    sq_ft = float(input("Enter the number of square feet you need painted: "))
    paint_cost = float(input("Enter the cost of a gallon of the paint you would like to use: "))
    gallons = paint(sq_ft)
    paint_total = gallons*paint_cost
    hours = gallons * 8
    labor = hours * 20
    total = labor + paint_total
    print(f"Your paint cost is: {paint_total:.2f}","\n"
        f"Your labor cost is: {labor:.2f}","\n"
        f"Your total cost is: {total:.2f}"
        )

# function replaced with lambda above
# def paint(num1):
#     return num1/115




main()