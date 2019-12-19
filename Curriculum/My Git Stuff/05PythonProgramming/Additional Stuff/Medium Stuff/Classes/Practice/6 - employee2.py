"""
6. Employee Management System
    This exercise assumes that you have created the Employee class for Programming Exercise 4.
    Create a program that stores Employee objects in a dictionary. Use the employee 
    ID number as the key. The program should present a menu that lets the user 
    perform the following actions:
        • Look up an employee in the dictionary
        • Add a new employee to the dictionary
        • Change an existing employee’s name, department, and job title in the
         dictionary
        • Delete an employee from the dictionary
        • Quit the program
    When the program ends, it should pickle the dictionary and save it to a file.
     Each time the
    program starts, it should try to load the pickled dictionary from the file. 
    If the file does not
    exist, the program should start with an empty dictionary.

"""
import pickle
import os
import employee
import pprint

blank_dict = {}
def main():
    global blank_dict
    employee_dict = read_or_new_pickle('employee.dat', blank_dict)
    selection = selection_menu()
    take_action(selection, employee_dict)
def take_action(var1, dict_1):
    if var1 == 5:
        exit()
    elif var1 == 4:
        emp_id = int(input("Enter the employee ID you would like to delete: "))
        try: 
            del dict_1[emp_id]
            print("Success")
            output_file = open('employee.dat', 'wb')
            pickle.dump(dict_1, output_file)
            output_file.close()
        except KeyError:
            print(f'Employee {emp_id:} was not found.')
    elif var1 == 3:
        emp_id = int(input("Enter the employee ID you would like to make changes to: "))
        slave = employee.Employee(dict_1[emp_id]['Name'], dict_1[emp_id]['ID Number'], dict_1[emp_id]['Department'], dict_1[emp_id]['Job Title'])
        print(f"Here is the current data {slave:}")
        slave.set_name(input("Enter the updated name: "))
        slave.set_department(input("Enter the updated department: "))
        slave.set_job(input("Enter the updated job title: "))
        dict_1.update({emp_id : {'Name' : slave.get_name(), 'ID Number' : slave.get_id_number(), 'Department' : slave.get_department(), 'Job Title' : slave.get_job()}})
        print(f"Here is your updated info:\n{slave:}")
        output_file = open('employee.dat', 'wb')
        pickle.dump(dict_1, output_file)
        output_file.close()
    elif var1 ==2:
        emp_id = int(input("Enter the employee ID you would like to enter: "))
        name = input("Enter the name: ")
        department = input("Enter the department: ")
        job = input("Enter the  job title: ")
        slave = employee.Employee(name, emp_id, department, job)
        print(f"Here is the current data {slave:}")
        dict_1.update({emp_id : {'Name' : slave.get_name(), 'ID Number' : slave.get_id_number(), 'Department' : slave.get_department(), 'Job Title' : slave.get_job()}})
        print(f"Here is entered info:\n{slave:}")
        output_file = open('employee.dat', 'wb')
        pickle.dump(dict_1, output_file)
        output_file.close()
    elif var1 == 1:
        lookup = int(input("Enter the employee ID of the person you want to look up if you don't know it type 0: "))
        if lookup == 0:
            pprint.pprint(dict_1, sort_dicts = False)
        elif lookup in dict_1:
            print(dict_1[lookup])
        else:
            print("There was an issue: ")
    else:
        exit()
def read_or_new_pickle(path, default):
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            try:
                return pickle.load(f)
            except Exception:
                pass
    with open(path, 'wb') as f:
        pickle.dump(default, f)
    return default
def selection_menu():
    print("\n" * 100)
    print("What would you like to do press the right button?")
    print("1: Look up an employee:\n2: Add a new employee:\n3: Change an employee's name, department, and job title:")
    print("4: Delete an employee:\n5: Quit the program:")
    return int(input(": "))
    


main()