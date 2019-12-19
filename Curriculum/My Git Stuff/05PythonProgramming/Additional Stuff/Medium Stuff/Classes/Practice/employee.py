"""
4. Employee Class
    Write a class named Employee that holds the following data about an employee in 
    attributes: 
    name, ID number, department, and job title.
    Once you have written the class, write a program that creates three Employee 
    objects to
    hold the following data:

Name            ID Number       Department      Job Title
Susan Meyers    47899           Accounting      Vice President
Mark Jones      39119           IT              Programmer
Joy Rogers      81774           Manufacturing   Engineer

The program should store this data in the three objects and then display the data for each
employee on the screen.
"""
class Employee:

    def __init__(self, name, id_number, department, job):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job = job
# define a function to set the needed data
    def set_name(self, name):
        self.__name = name
    # define a function to set the needed data
    def set_id_number(self, id_number):
        self.__id_number = id_number
    # define a function to set the needed data
    def set_department(self, department):
        self.__department = department
    # define a function to set the needed data
    def set_job(self, job):
        self.__job = job
    # define a function to return the data
    def get_name(self):
        return self.__name
    # define a function to return the data
    def get_id_number(self):
        return self.__id_number
    # define a function to return the data
    def get_department(self):
        return self.__department
    # define a function to return the data
    def get_job(self):
        return self.__job
    # define a function to return the data
    def __str__(self):
        return f'\nName: {self.__name:} \nEmployee ID: {self.__id_number:} \nDepartment: {self.__department:} \nJob Title: {self.__job:}\n '