"""
3. Recursive Lines
    Write a recursive function that accepts an integer argument, n. The function should display
    n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line
    showing 2 asterisks, up to the nth line which shows n asterisks.
"""
# define stuff
def stuff():
    # make empty list
    list = []
    # set variables
    y = 1
    ast = int(input('Enter the number of asterisk and lines that you want to see: '))
    # pass to function
    printLines(ast)
    lines(ast, list, y)
# define lines
def lines(x, list, y):
    # if x is 0 print the list
    if x == 0:
        print(*list, sep = '\n')
    # if not add the astericks and subtract from X
    else:
        list.append('*' * y)
        return lines(x - 1, list, y + 1)
################################ ALTERNATE ############################
# Alternate method
def printLines(n):
    if n > 1:
        printLines(n - 1)
    for _ in range(n):
        print ("*",end=""),
    print()


stuff()