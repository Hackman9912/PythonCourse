# This program displays property taxes

# calc property tax on multiple properties, loop using number 0 as a sentinel value

# TAX_FACTOR is used as a globa
TAX_FACTOR = .0065

# The main function

def main():

    print("Enter the property lot number or 0 to end")

    lot = int(input("Lot number: "))

    while lot != 0:
        show_tax()

        print("Enter the next lot number or enter 0 to end. ")
        lot = int(input("Lot number: "))


def show_tax():
    # get property value
    value = float(input("Enter the property value: "))
    tax = value * TAX_FACTOR
    print(f"Here is your property tax {tax:.2f}")

main()

