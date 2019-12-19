"""
5. RetailItem Class
Write a class named RetailItem that holds data about an item in a retail store. 
The class
should store the following data in attributes: item description, units in inventory, 
and price.
Once you have written the class, write a program that creates three 
RetailItem objects
and stores the following data in them:

            Description     Units in Inventory  Price
Item #1     Jacket          12                  59.95
Item #2     Designer Jeans  40                  34.95
Item #3     Shirt           20                  24.95
"""
class RetailItem:

    def __init__(self, item_description, units, price):
        self.__item_description = item_description
        self.__units = units
        self.__price = price
# define a function to set the needed data
    def set_name(self, item_description):
        self.__item_description = item_description
    # define a function to set the needed data
    def set_units(self, units__units):
        self.__units = units__units
    # define a function to set the needed data
    def set_price(self, price):
        self.__price = price
    # define a function to return the data
    def get_ItemDescription(self):
        return self.__item_description
    # define a function to return the data
    def get_units(self):
        return self.__units
    # define a function to return the data
    def get_price(self):
        return self.__price
    # define a function to return the data
    def __str__(self):
        return f'\nItem Description: {self.__item_description:} \nUnits in inventory: {self.__units:} \nPrice: ${self.__price:.2f} \n'