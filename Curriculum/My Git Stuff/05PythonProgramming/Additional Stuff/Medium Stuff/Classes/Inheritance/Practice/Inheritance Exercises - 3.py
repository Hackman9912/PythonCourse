"""
3. Person and Customer Classes
    Write a class named Person with data attributes for a person’s name, address, and 
    telephone number. Next, write a class named Customer that is a subclass of the 
    Person class. The Customer class should have a data attribute for a customer 
    number and a Boolean data attribute indicating whether the customer wishes to be 
    on a mailing list. Demonstrate an instance of the Customer class in a simple 
    program.
"""
import assets
import pprint
pppl_lst = []
cust_lst = []
def main():
    global pppl_lst, cust_lst
    pppl_num = int(input('Enter the number of people you need to add: '))
    setthelist(pppl_num)
    print("Not Customers: ")
    print_list(pppl_lst)
    print("Customers: ")
    print_list(cust_lst)

def setthelist(theamount):
    global pppl_lst, cust_lst
    for i in range(theamount):
        print("Person", i+1)
        customerinput = int(input('Is this person a customer? 1 for yes 0 for no: '))
        if customerinput == 1:
            name = input('Enter the persons name: ')
            address = input('Enter the address: ')
            phone = input('Enter the phone number for the person: ')
            cust_num = int(input('Enter the customer number: '))
            mail = 2
            while mail != 0 and mail != 1:
                mail = int(input('Does the customer want to be on the mailing list? 1 = yes 0 = no: '))
            print('mail', mail)
            customer = assets.Customer(name, address, phone, cust_num, bool(mail))
            cust_lst.append(customer)
        elif customerinput == 0:
            name = input('Enter the persons name: ')
            address = input('Enter the address: ')
            phone = input('Enter the phone number for the person: ')
            notcustomer = assets.Person(name, address, phone)
            pppl_lst.append(notcustomer)
def print_list(listss):
    if listss is pppl_lst:
        for i in listss:
            print('Name: ', i.get_name())
            print('Address: ', i.get_address())
            print('Phone: ', i.get_phone())
    elif listss is cust_lst:
        for i in listss:
            print('Name: ', i.get_name())
            print('Address: ', i.get_address())
            print('Phone: ', i.get_phone())
            print('Customer Number: ', i.get_cust_num())
            print('Is on mailing address: ', i.get_mail())

main()
