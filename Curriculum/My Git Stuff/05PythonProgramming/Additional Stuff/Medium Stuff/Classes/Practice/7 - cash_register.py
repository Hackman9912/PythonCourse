"""
7. Cash Register
    This exercise assumes that you have created the RetailItem class for Programming
    Exercise 5. Create a CashRegister class that can be used with the RetailItem class. The
    CashRegister class should be able to internally keep a list of RetailItem objects. The
    class should have the following methods:
        • A method named purchase_item that accepts a RetailItem object as an argument.
        Each time the purchase_item method is called, the RetailItem object that is passed as
        an argument should be added to the list.
        • A method named get_total that returns the total price of all the RetailItem objects
        stored in the CashRegister object’s internal list.
        • A method named show_items that displays data about the RetailItem objects stored
        in the CashRegister object’s internal list.
        • A method named clear that should clear the CashRegister object’s internal list.
    Demonstrate the CashRegister class in a program that allows the user to select several
    items for purchase. When the user is ready to check out, the program should display a list
    of all the items he or she has selected for purchase, as well as the total price.
"""

import RetailItem
import cashregister
import time
import pprint
# establish the dictionary with the data
item_dict = {1 : { 'description' : 'Jacket', 'units' : 12, 'price' : 59.95},
            2 : { 'description' : 'Designer Jeans', 'units' : 40, 'price' : 34.95},
            3 : { 'description' : 'Shirt', 'units' : 20, 'price' : 24.95}}
# define the main function
def main():
    # set the variable to call the class and use dictionary info to populate it
    item1 = RetailItem.RetailItem(item_dict[1]['description'], item_dict[1]['units'], item_dict[1]['price'])
    item2 = RetailItem.RetailItem(item_dict[2]['description'], item_dict[2]['units'], item_dict[2]['price'])
    item3 = RetailItem.RetailItem(item_dict[3]['description'], item_dict[3]['units'], item_dict[3]['price'])
    # display the data
    print("\n" * 100)
    print(f'\n----Here are the items for sale:-----')
    time.sleep(1)
    print(item1, item2, item3)
    purchase_list = cashregister.CashRegister()
    time.sleep(1)
    choice = decide()
    while choice != 0:
        if choice == 1:
            amount = int(input("Enter the number of Jackets you want: "))
            price = item1.get_price() * amount
            purchase_list.purchase_item(item1.get_ItemDescription(), amount, price)
            choice = decide()
        elif choice == 2: 
            amount = int(input("Enter the number of Designer Jeans you want: "))
            price = item2.get_price() * amount
            purchase_list.purchase_item(item2.get_ItemDescription(), amount, price)
            choice = decide()
        elif choice == 3:
            amount = int(input("Enter the number of Shirts you want: "))
            price = item3.get_price() * amount
            purchase_list.purchase_item(item3.get_ItemDescription(), amount, price)
            choice = decide()        
        elif choice == 4:
            pprint.pprint(purchase_list.show_items(), indent = 2, sort_dicts = False)
            choice = decide()
        elif choice == 5:
            print(purchase_list.get_total())
            choice = decide()
        elif choice == 6:
            purchase_list.clear()
            choice = decide()
        else:
            choice = decide()
    print("\n" * 100)
    print("Here is what you purchased: ")
    pprint.pprint(purchase_list.show_items(), indent = 2, sort_dicts = False)
    print("Here is your total:")
    print(purchase_list.get_total())
    print("Thanks for shopping. Have a great day!")


def decide():
    print("Please choose an item to purchase, 1 for Jacket, 2 for Jeans and 3 for Shirt,")
    print("Press 4 to view your cart, 5 to view the total, 6 to clear the cart and 0 to quit: ")
    return int(input(": "))

# call main
main()