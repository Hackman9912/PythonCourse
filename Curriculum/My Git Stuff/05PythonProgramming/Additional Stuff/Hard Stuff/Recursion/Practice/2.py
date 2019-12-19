"""
2. Recursive Multiplication
    Design a recursive function that accepts two arguments into the parameters x and y. The
    function should return the value of x times y. Remember, multiplication can be performed
    as repeated addition as follows:
    7 X 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4
    (To keep the function simple, assume that x and y will always hold positive nonzero
    integers.)
"""

# define the main function
def main():
    # get our values
    val1 = int(input('Enter the first value to be multiplied: '))
    val2 = int(input('Enter the second value to be multiplied: '))
    # pass the values to the function
    print(mult(val1, val2))

# define mult()
def mult(x, y):
    # if y or x is 0 just print the sum, which is 0
    if x == 0 or y == 0:
        return 0
    # if not then recursively pass x + and then the function
    else:
        return x + mult(x, y - 1)
# call main
main()



