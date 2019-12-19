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

4. 
    (The sqrt function) Write a program that prints the following table
    using your knowledge of loops and the sqrt function in the math module.
    Make sure your table is neat by using print formatting methods we've learned. 

        Number  Square Root
        0       0.0000
        1       1.0000
        2       1.4142
        ...
        18      4.2426
        20      4.4721

"""
# import things
import math
# define maine
def main():
    # make an empty dict
    sqrt_dict = {}
    # do the range
    for i in range(20):
        # add the sqrt values to the dict
        sqrt_dict[i] = round(sqrtt(i), 4)
    # print the top part
    print("Number: Square Root")
    # print a neat formatted table
    print('\n'.join("{}:        {}".format(k, v) for k, v in sqrt_dict.items()))
# define a funtion to do the square root
def sqrtt(val1):
    return math.sqrt(val1)
# call main
main()