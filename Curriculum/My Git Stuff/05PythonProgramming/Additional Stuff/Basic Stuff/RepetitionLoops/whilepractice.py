# Calc sales commisison

def main():
    # Create a var to control the loop
    keep_going = "y"

    while keep_going == "y":
        # Get a salesperson's sales and commission rate
        sales = float(input("Enter the amount of sales: "))
        comm_rate = float(input("Enter the comm rate: "))
        commission = sales * comm_rate

        # Display the commission
        print(f"The commission is ${commission:.2f}")

        # See if ther user wants to do another one

        keep_going = input("Do you want to calculate another " +\
            "comission (Enter y for yes): ")
main()