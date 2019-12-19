"""
 1. Total Sales
Design a program that asks the user to enter a store’s sales for each day of the week. The
amounts should be stored in a list. Use a loop to calculate the total sales for the week and
display the result.
"""
def main():

    sales = []

    input_more = "y"

    total = 0

    count = 0

    while input_more == "y":

        count += 1
        print("Enter the total for day", count)
        amount = int(input(": "))

        sales.append(amount)

        print("Do you want to add another sales amount?")
        input_more = input("y is yes, anything else is no: ")

    for num in sales:
        total += num

    print("Your total sales this week is: ", total)

main()