"""
1. Employee and ProductionWorker Classes
    Write an Employee class that keeps data attributes for the following pieces of
     information:
        • Employee name
        • Employee number
    Next, write a class named ProductionWorker that is a subclass of the Employee 
    class. The ProductionWorker class should keep data attributes for the following 
    information:
        • Shift number (an integer, such as 1, 2, or 3)
        • Hourly pay rate
    The workday is divided into two shifts: day and night. The shift attribute will
    hold an integer value representing the shift that the employee works. The day 
    shift is shift 1 and the night shift is shift 2. Write the appropriate accessor 
    and mutator methods for each class. Once you have written the classes, write a 
    program that creates an object of the ProductionWorker class and prompts the user 
    to enter data for each of the object’s data attributes. Store the data in the 
    object and then use the object’s accessor methods to retrieve it and display it on 
    the screen.

"""
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
    
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

class ProdWork(Employee):
    def __init__(self, name, number, shift, pay):
        super().__init__(name, number)
        self.__shift = shift
        self.__pay = pay

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay(self, pay):
        self.__pay = pay

    def get_shift(self):
        if self.__shift == 1:
            return 'Day'
        elif self.__shift == 2:
            return 'Swings'
        elif self.__shift == 3:
            return 'Nights'
        else:
            return f'You entered {self.__shift:} which is not a good choice.'

    def get_pay(self):
        return self.__pay

class Supervisor(Employee):
    def __init__(self, name, number, salary, bonus):
        super().__init__(name, number)
        self.__salary = salary
        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus