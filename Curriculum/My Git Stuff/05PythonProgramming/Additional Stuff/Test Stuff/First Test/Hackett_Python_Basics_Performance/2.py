"""
20/25 points
You definitely nailed the nested loop portion of this one however the prompt asks for user input.
You hard coded your 2d list. 
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


2.
    (Locate the largest element) Write the following function that returns the location
    of the largest element in a two-dimensional list:
    
    def locateLargest(a):
        The return value is a one-dimensional list that contains two elements. These
        two elements indicate the row and column indexes of the largest element in the
        two-dimensional list. Write a test program that prompts the user to enter a 
        two-dimensional list and displays the location of the largest element in the list. 
    
    Here is a sample run(You don't have to mimic this, this is just a guide):

        Enter the number of rows in the list: 3
        Enter a row: 23.5  35  2    10
        Enter a row: 4.5   3   45   3.5
        Enter a row: 35    44  5.5  11.6
        The location of the largest element is at (1,2)
"""
# define main
def main():
    # build the list of values
    values = [[235, 35, 2, 10], [4.5, 3, 45, 3.5], [100, 44, 5.5, 11.6]]
    # set x
    x = 0
    # iterate through the lists
    for i in values:
        # iterate through the lists of lists
        for r in i:
            # if x is less than r then replace x
            if x <= r:
                x = r
    # call the function to get the index
    position = index(values, x)
    # Tell the user
    print(f'The largest number is {x} and its index is {position}')
# Define the funciton to get the index
def index(data, search):
    # enumerate the data
    for i, e in enumerate(data):
        # try to get the value
        try:
            # send back the index after enumerating through and getting the position
            return i, e.index(search)
        # if it will not work then just pass
        except ValueError:
            pass
    # tell the user if there is a value error
    raise ValueError("{} is not in list".format(repr(search)))
# call main          
main()