# define the class
class GeometricObject:
        # initialize and set the things
        def __init__(self, color = "green", filled = True):
            self.color = color
            self.filled = filled
        # set a getter
        def getColor(self):
            return self.color
        # set a setter
        def setColor(self, color):
            self.color = color
        # set a getter
        def isFilled(self):
            return self.filled
        # set a setter
        def setFilled(self, filled):
            self.filled = filled
        # use the __str__
        def __str__(self):
            return "color: " + self.color + " and filled: " + str(self.filled)
'''
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
'''
# define the class
class TriangleObject:
    # initialize the variables
    def __init__(self,  color = "green", filled = True, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        # set the parent
        GeometricObject.__init__(self, color, filled)
        # initialize the sides, perimeter and area
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.perimeter = (self.side1 + self.side2 + self.side3)/2
        self.area = (self.perimeter * (self.perimeter - self.side1) * (self.perimeter - self.side2) * (self.perimeter - self.side3)) ** (1/2.0)
    # Define the setters
    def set_side1(self, side1):
        self.side1 = side1

    def set_side2(self, side2):
        self.side2 = side2

    def set_side3(self, side3):
        self.side3 = side3
    # define the getters
    def get_side1(self):
        return self.side1

    def get_side2(self):
        return self.side2

    def get_side3(self):
        return self.side3

    def getPerimeter(self):
        self.perimeter = (self.side1 + self.side2 + self.side3)/2
        return self.perimeter

    def getArea(self):
        self.area = (self.perimeter * (self.perimeter - self.side1) * (self.perimeter - self.side2) * (self.perimeter - self.side3)) ** (1/2.0)
        return self.area
    # define the __str__
    def __str__(self):
        return f'A triangle is a 3 sided shape. The current sides have a length of {self.side1}, {self.side2}, and {self.side3}, the area is {self.area:.2f} and the perimiter is {self.perimeter}'


