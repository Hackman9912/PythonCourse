"""
7. Recursive Power Method
    Design a function that uses recursion to raise a number to a power. The function should
    accept two arguments: the number to be raised and the exponent. Assume that the exponent is a 
    nonnegative integer.
"""
# define main
def main():
    # Establish vars
    int1 = int(input("Enter the first integer: "))
    int2 = int(input("Enter the second integer: "))
    # pass to function
    exp(int1, int2, 1)
# define exponent
# def exp(x, y, z, a):

    # if z is greater than the exponent then print the formatted number
    # if z > y:
    #     print(f'{a:,.2f}')
    # # If not cal lthe function again passing z, y and z plus 1 and the total times the base number 
    # else:
    #     return exp(x, y, z + 1, a * x)
# A better way less lines, simpler
def exp(x, y, a):
    # While y is greater than 0 call the function again passing x, y - 1 and a (the total) times the base number 
    while y > 0: return exp(x, y - 1, a * x)
    print(f'{a:,.2f}')
# call main
main()


# 7. 
# def power(x,y):
#     if y == 0:
#         return 1
#     else:
#         return x * power(x, y - 1)
# print(power(3,3))