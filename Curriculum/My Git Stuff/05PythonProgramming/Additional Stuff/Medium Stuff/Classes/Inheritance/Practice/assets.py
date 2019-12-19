class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

class Customer(Person):
    def __init__(self, name, address, phone, cust_num, mail):
        super().__init__(name, address, phone)
        self.__cust_num = cust_num
        self.__mail = mail
    
    def set_cust_num(self, cust_num):
        self.__cust_num = cust_num

    def set_mail(self, mail):
        self.__mail = mail

    def get_cust_num(self):
        return self.__cust_num

    def get_mail(self):
        return self.__mail