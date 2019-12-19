"""
4. Employee Class
    Write a class named Employee that holds the following data about an employee in attributes: 
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
# import the important things
import employee
import pickle
# make the employee dictionary
employee_dict = {1 : {'Name':'Susan Meyers', 'ID Number' : '47899', 'Department' : 'Accounting', 'Job Title' : 'Vice President'},
                2 : {'Name':'Mark Jones', 'ID Number' : '39119', 'Department' : 'IT', 'Job Title' : 'Programmer'},
                3 : {'Name':'Joy Rogers', 'ID Number' : '81774', 'Department' : 'Manufacturing', 'Job Title' : 'Engineer'}}
# define the main fucntion
def main():
    # set the variable to call the class using the dictionary to establish the values
    employee1 = employee.Employee(employee_dict[1]['Name'], employee_dict[1]['ID Number'], employee_dict[1]['Department'], employee_dict[1]['Job Title'])
    employee2 = employee.Employee(employee_dict[2]['Name'], employee_dict[2]['ID Number'], employee_dict[2]['Department'], employee_dict[2]['Job Title'])
    employee3 = employee.Employee(employee_dict[3]['Name'], employee_dict[3]['ID Number'], employee_dict[3]['Department'], employee_dict[3]['Job Title'])
    # print the data
    print(employee1, employee2, employee3)
# call main
main()