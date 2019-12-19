"""
6. Sum of Numbers
    Design a function that accepts an integer argument and returns the sum of all the integers from 1 up 
    to the number passed as an argument. For example, if 50 is passed as an argument, the function will 
    return the sum of 1, 2, 3, 4, . . . 50. Use recursion to calculate the sum.
"""

# Define main
def main():
    # desired = int(input('Enter the integer you want the sum of all numbers leading up to: '))
    desired = 8
    # pass all to the function
    print(adding(desired))
# define the adding function
def adding(x):
    # while x does not equal 0 then keep doing the thing
    while x != 0: return x + adding(x-1)
    # when x = 0 then return x
    return x
 
# call main
main()

'''
def main():
    desired = int(input('Enter the integer you want the sum of all numbers leading up to: '))
    count = 0
    sum = 0
    # pass all to the function
    adding(desired, count, sum)
# define the adding function
def adding(x, y, sum):
    # if y is greater than the desired number then print the sum
    if y > x:
        print(sum)
    # if not then add y to the sum
    else:
        # call the function again passing all the things and setting y plus 1 and adding y to the sum
        return adding(x, y + 1, sum + y)
# call main
main()
'''
