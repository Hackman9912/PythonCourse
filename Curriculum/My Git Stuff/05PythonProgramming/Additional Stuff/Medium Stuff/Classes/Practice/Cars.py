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
# define the class of cars
class Cars:
    # define the init with all the variables
    def __init__(self, year, make, model, speed):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = speed
    # def setting the year of the car
    def set_year(self, year):
        self.__year = year
    # def function to set the make of the car
    def set_make(self, make):
        self.__make = make
    # def function to set the model of the car
    def set_model(self, model):
        self.__model = model
    # def function to accelerate
    def accelerate(self):
        self.__speed += 5
        return self.__speed
    # def function to begin braking
    def brake(self):
        self.__speed -= 5
        return self.__speed
    # define a function to get the speed
    def get_speed(self):
        return self.__speed
    # return the year
    def get_year(self):
        return self.__year
    # returns the make
    def get_make(self):
        return self.__make
    # return the model
    def get_model(self):
        return self.__model
