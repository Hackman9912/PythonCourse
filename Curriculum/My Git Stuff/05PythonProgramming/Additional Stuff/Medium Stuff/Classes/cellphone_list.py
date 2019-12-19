# This program creates five CellPhone objects and stores in a list

import cellphone

def main():
    # Get a list of CellPhone
    phones = make_list()

    # Display the data in the list
    print("Here is the data you entered: ")
    display_list(phones)

# THe make_list function gets data from the user for five phones. The funciton 
# returns a list of CellPhone object containing the data

def make_list():
    # Create an empty list
    phone_list = []

    print("Enter data for five phones: ")
    for count in range(1,6):
        # Get the phone data
        print('Phone number' + str(count) + ':')
        man = input('Enter the manufacterer: ')
        mod = input('Enter the model number: ')
        retail = float(input('Enter the retail price: '))
        print()

        # Create a new CellPhone object in memory and assign it to the new phone variable
        phone = cellphone.CellPhone(man, mod, retail)

        # Add the object to the list
        phone_list.append(phone)
    
    # Return the list
    return phone_list

# The display_list function accepts a list containing CellPhone objects as an argument
# and displays the data stored in each object

def display_list(phone_list):
    count = 0
    for phone in phone_list:
        print()
        count += 1
        print(f'Phone {count:}')
        print(phone.get_manufact())
        print(phone.get_model())
        print(phone.get_retail_price())
        print('***********************')

main()