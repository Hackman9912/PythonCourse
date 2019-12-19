"""
5. RetailItem Class
Write a class named RetailItem that holds data about an item in a retail store. The class
should store the following data in attributes: item description, units in inventory, and price.
Once you have written the class, write a program that creates three RetailItem objects
and stores the following data in them:

            Description     Units in Inventory  Price
Item #1     Jacket          12                  59.95
Item #2     Designer Jeans  40                  34.95
Item #3     Shirt           20                  24.95
"""
# import the important things
import RetailItem
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
    print(item1, item2, item3)
# call main
main()