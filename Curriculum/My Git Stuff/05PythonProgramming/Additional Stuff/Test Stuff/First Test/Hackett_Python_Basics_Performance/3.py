"""
12.5/25 points
For this I wanted you guys to set up inheritance. You were close but didn't quite get there.
Also, your sides don't update to what the user inputs. 
"""

"""
Python Basics Performance Exam

    This exam is open note, open book, and open internet. Feel free to use any resources
    you can (other than someone else) to solve the following problems. Direct collaboration with another
    individual will result in immediate failure and consequences to follow. If you are unsure about 
    whether or not you can use a resource please ask me. If you are unsure about any of the prompts I can clarify. 

    Comments are necessary. 

    Each problem will weigh the same towards the final grade. 4 Problems at 25% each. 

    Please send each problem as a .py file separately. Please direct message them to me (Daniel Curran) 
    through slack. If there are supporting files for a problem then please send them with the .py file 
    as a zipped folder. 

    You will have 3 hours to complete this exam. If you complete this portion early and I have verified
    I have everything needed to grade your exam then you will be released.

    Happy Thanksgiving. 

3. 
(The Triangle class) Design a class named Triangle that extends the
GeometricObject class defined below. The Triangle class contains:
    - Three float data fields named side1, side2, and side3 to denote the three
    sides of the triangle.
    - A constructor that creates a triangle with the specified side1, side2, and
    side3 with default values 1.0.
    - The accessor methods for all three data fields.
    - A method named getArea() that returns the area of this triangle.
    - A method named getPerimeter() that returns the perimeter of this triangle.
    - A method named __str__() that returns a string description for the triangle.


    class GeometricObject:
        def __init__(self, color = "green", filled = True):
            self.color = color
            self.filled = filled

        def getColor(self):
            return self.color

        def setColor(self, color):
            self.color = color

        def isFilled(self):
            return self.filled

        def setFilled(self, filled):
            self.filled = filled
    
        def toString(self):
            return "color: " + self.color + " and filled: " + str(self.filled)


    Write a test program that prompts the user to enter the three sides of the 
    triangle, a color, and 1 or 0 to indicate whether the triangle is filled. 
    The program should create a Triangle object with these sides and set the 
    color and filled properties using the input. The program should display the 
    triangle’s area, perimeter, color, and True or False to indicate whether the 
    triangle is filled or not.

"""
# Import the things
from shapes1 import GeometricObject as go 
from shapes1 import TriangleObject as tr
# Define the mian function
def main():
    # get the values to set
    side1 = float(input("Enter the length of side 1: "))
    side2 = input("Enter the length of side 2: ")
    side3 = input("Enter the length of side 3: ")
    color = input("Enter the color you want the shape to be: ")
    filled = input("Enter 1 if you want the shape filled and 0 if you do not: ")
   # set the values
    tr.set_side1 = side1
    tr.set_side2 = side2
    tr.set_side3 = side3
    go.setColor = color
    # if the user picks a goot selection then set it. If not then default
    if filled == "1":
        go.setFilled = True
    elif filled == "0":
        go.setFilled = False
    else:
        print("You did not enter appropriate input for filling the shape so we will default: ")
        go.setColor = True
    # Display the data
    print(tr())
    print(go())
    
    


main()