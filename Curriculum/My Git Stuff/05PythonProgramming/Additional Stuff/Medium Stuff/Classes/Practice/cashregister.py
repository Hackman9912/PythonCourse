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

class CashRegister:
    def __init__(self):
        self.__lists = []

    def purchase_item(self, desc, unit, price):
        self.__lists.append({'name' : desc, 'amount' : unit, 'price' : price})

    def get_total(self):
        price_list = []
        for index in range(len(self.__lists)):
            for key in self.__lists[index]:
                if key == 'price':
                    price_list.append(self.__lists[index][key])
        if sum(price_list) > 0:
            return f'${sum(price_list):.2f}'
        else:
            return 0



    def show_items(self):
        return self.__lists
    
    def clear(self):
        self.__lists = []
        return self.__lists