"""
2. ShiftSupervisor Class
    In a particular factory, a shift supervisor is a salaried employee who supervises
    a shift. In addition to a salary, the shift supervisor earns a yearly bonus when
    his or her shift meets production goals. Write a ShiftSupervisor class that is a 
    subclass of the Employee class you created in Programming Exercise 1. The 
    ShiftSupervisor class should keep a data attribute for the annual salary and a 
    data attribute for the annual production bonus that a shift supervisor has earned. 
    Demonstrate the class by writing a program that uses a ShiftSupervisor object.
"""
import worker

def main():
    supers = employees()
    displaystuff(supers)

def employees():
    name = input('Enter the supervisors name: ')
    number = int(input('Enter the supervisors number: '))
    salary = float(input('Enter the salary for the supervisor: '))
    bonus = float(input('Enter the annual bonus of the supervisor: '))
    supers =  worker.Supervisor(name, number, salary, bonus)
    return supers
def displaystuff(thingy):
    print()
    print('Name: ', thingy.get_name())
    print('Supervisors Employee Number: ', thingy.get_number())
    print(f'Supervisors Salary: ${thingy.get_salary():,.2f}')
    print(f'Supervisors hourly pay rate ${thingy.get_bonus():,.2f}')
    total = thingy.get_salary() + thingy.get_bonus()
    print(f'Supervisors total pay: ${total:,.2f}')

main()