"""
1. Employee and ProductionWorker Classes
    Write an Employee class that keeps data attributes for the following pieces of information:
        • Employee name
        • Employee number
    Next, write a class named ProductionWorker that is a subclass of the Employee class. The
    ProductionWorker class should keep data attributes for the following information:
        • Shift number (an integer, such as 1, 2, or 3)
        • Hourly pay rate
    The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing the shift that the employee works. The day shift is shift 1 and the
    night shift is shift 2. Write the appropriate accessor and mutator methods for each class.
    Once you have written the classes, write a program that creates an object of the
    ProductionWorker class and prompts the user to enter data for each of the object’s data
    attributes. Store the data in the object and then use the object’s accessor methods to retrieve
    it and display it on the screen.

"""
import worker

def main():
    shift1 = employees()
    shift2 = employees()
    shift3 = employees()
    displaystuff(shift1)
    displaystuff(shift2)
    displaystuff(shift3)
def employees():
    name = input('Enter the employees name: ')
    number = int(input('Enter the employee number: '))
    shift = int(input('Enter the shift number for the employee, 1 - Days, 2 - Swings, 3 - Mids: '))
    pay = float(input('Enter the hourly pay rate of the employee: '))
    return worker.ProdWork(name, number, shift, pay)
def displaystuff(thingy):
    print()
    print('Name: ', thingy.get_name())
    print('Employee Number: ', thingy.get_number())
    print('Employees Shift: ', thingy.get_shift())
    print(f'Employees hourly pay rate ${thingy.get_pay()}')

main()