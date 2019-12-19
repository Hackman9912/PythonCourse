"""
3. Personal Information Class
    Design a class that holds the following personal data: name, address, age, and phone number. Write 
    appropriate accessor and mutator methods. Also, write a program that creates
    three instances of the class. One instance should hold your information, and the other two
    should hold your friends’ or family members’ information.

"""
# define our class for P I I
class Pii:
    # initialize all our variables
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number
    # define a function to set the needed data
    def set_name(self, name):
        self.__name = name
    # define a function to set the needed data
    def set_address(self, address):
        self.__address = address
    # define a function to set the needed data
    def set_age(self, age):
        self.__age = age
    # define a function to set the needed data
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    # define a function to return the data
    def get_name(self):
        return self.__name
    # define a function to return the data
    def get_address(self):
        return self.__address
    # define a function to return the data
    def get_age(self):
        return self.__age
    # define a function to return the data
    def get_phone_number(self):
        return self.__phone_number
    # define a function to return the data
    def __str__(self):
        return f'\nName: {self.__name:} \nAddress: {self.__address:} \nAge: {self.__age:} \nPhone Number: {self.__phone_number:}\n '