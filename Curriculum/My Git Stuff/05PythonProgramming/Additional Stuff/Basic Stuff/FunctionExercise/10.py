# 10. Monthly Sales Tax
# A retail company must file a monthly sales tax report listing the total sales for the month, and the amount of state and county sales tax collected. 
# The state sales tax rate is 4 percentand the county sales tax rate is 2 percent. Write a program that asks the user to enter the total sales for the month. 
# From this figure, the application should calculate and display thefollowing:
# • The amount of county sales tax
# • The amount of state sales tax
# • The total sales tax (county plus state)
def main():
    tax = lambda x, y : x * y
    total_sales = float(input("Enter the total sales for the month: "))
    county_tax = tax(.02, total_sales)
    state_tax = tax(.04, total_sales)
    total = county_tax + state_tax
    print("\n"
        f"Your county tax:  {county_tax:.2f}", "\n"
        f"Your State Tax is: {state_tax:.2f}", "\n"
        f"Your Total Tax is: {total:.2f}"
        )
# replaced this with lambda above
# def tax(num1, num2):
#     return num1 * num2

main()