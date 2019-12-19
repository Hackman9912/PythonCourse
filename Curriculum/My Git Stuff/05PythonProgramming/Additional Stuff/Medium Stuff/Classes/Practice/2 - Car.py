"""

2. Car Class
    Write a class named Car that has the following data attributes:
        • __year_model (for the car’s year model)
        • __make (for the make of the car)
        • __speed (for the car’s current speed)
        The Car class should have an __init__ method that accept the car’s year model and make
        as arguments. These values should be assigned to the object’s __year_model and __make
        data attributes. It should also assign 0 to the __speed data attribute.
        The class should also have the following methods:
        • accelerate
        The accelerate method should add 5 to the speed data attribute each time it is
        called.
        • brake
        The brake method should subtract 5 from the speed data attribute each time it is called.
        • get_speed
        The get_speed method should return the current speed.
    Next, design a program that creates a Car object, and then calls the accelerate method
    five times. After each call to the accelerate method, get the current speed of the car and
    display it. Then call the brake method five times. After each call to the brake method, get
    the current speed of the car and display it.

"""
# import the import-ant things
import Cars
import time
# define main
def main():
    # establish the variables
    year = int(input("Enter the year of the car: "))
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    speed = 0
    # set the things to the class
    car = Cars.Cars(year, make, model, speed)
    # get the speed we set for reasons
    speed = car.get_speed()
    # loop to accelerate
    for i in range(5):
        speed = car.accelerate()
        print(f"Accelerating step {i + 1:} speed is {speed:}")
        # simulate realism
        time.sleep(.5)
    print()
    # so fast
    print(f"You are moving at a blistering {speed:} of probably KPH")
    # traveling so far
    time.sleep(2)
    print('\n')
    # loop to brake
    for i in range(5):
        speed = car.brake()
        print(f"Braking step {i + 1:} speed is {speed:}")
        time.sleep(1)
# call main
main()


