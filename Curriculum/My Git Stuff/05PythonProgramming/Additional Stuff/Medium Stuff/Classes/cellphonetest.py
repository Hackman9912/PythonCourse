# This program tests the CellPhone Class
import cellphone as c

def main():
    # Get the phone data
    man = input("Enter the manufacturer: ")
    mod = input("Enter the model number: ")
    retail = float(input('Enter the reatail price: '))

    # Create an instance of the CellPhone class
    phone = c.CellPhone(man, mod, retail)

    # Display the datat that was entered
    print('Here is the data that you entered: ')
    print('Manufactuerer: ', phone.get_manufact())
    print('Model Number:', phone.get_model())
    print(f'Retail Price ${phone.get_retail_price():,.2f}')

# Call main
main()