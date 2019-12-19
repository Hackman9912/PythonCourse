"""
7. (Largest rows and columns) Write a program that randomly fills in 0s and 1s into
a matrix, prints the matrix, and finds the rows and columns with the most
1s. Here is a sample run of the program:
0011
0011
1101
1010
The largest row index: 2
The largest column index: 2, 3
"""
# Import the randomizer
import random

# Establish constants
ROWS = 4
COLUMNS = 4
flatlist = []
nameRow = "row"
nameColumn = "column"
# define main
def main():

    # Establish 2d list
    values = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

    # Randomize the contents of values 
    for r in range(ROWS):
        for c in range(COLUMNS):
            values[r][c] = random.randint(0, 1)
            print(values[r][c], end = " ")

        print()
# Print values for helping the solving
    '''
    print(values[0:1], "\n",
        values[1:2], "\n",
        values[2:3], "\n",
        values[3:4], "\n",
        )
    '''
    
    row1 = [sum(count) for count in values[0:1]]

    row2 = [sum(count) for count in values[1:2]]

    row3 = [sum(count) for count in values[2:3]]

    row4 = [sum(count) for count in values[3:4]]


    compare(nameRow, row1, row2, row3, row4)

    
    removeNesting(values)
    # print("Here is flat list", flatlist)

    column1 = sum(flatlist[::4])
    # print("Column1", column1)
    column2 = sum(flatlist[1::4])
    # print('Column2', column2)
    column3 = sum(flatlist[2::4])
    # print('Column3', column3)
    column4 = sum(flatlist[3::4])
    # print('Column4', column4)

    compare(nameColumn, column1, column2, column3, column4)
def compare(name, num1, num2, num3, num4):
    if num1 > num2 and num1 > num3 and num1 > num4:
        print("The largest", name, "is", name, "1")
    elif num2 > num1 and num2 > num3 and num2 >num4:
        print("The largest", name, "is", name, "2")
    elif num3 > num1 and num3 > num2 and num3 >num4:
        print("The largest", name, "is", name, "2")
    elif num4 > num1 and num4 > num2 and num4 >num3:
        print("The largest", name, "is", name, "2")
    elif num1 == num2 and num1 > num3 and num1 > num4:
        print("The largest", name, "is 1 and 2")
    elif num1 == num3 and num1 > num2 and num1 > num4:
        print("The largest", name, "is 1 and 3")
    elif num1 == num4 and num1 > num2 and num1 > num3:
        print("The largest", name, "is 1 and 4")
    elif num2 == num3 and num2 > num1 and num2 > num4:
        print("The largest", name, " is 2 and 3")
    elif num2 == num4 and num2 > num1 and num2 > num3:
        print("The largest", name, "is 2 and 4")
    elif num3 == num4 and num3 > num1 and num3 > num2:
        print("The largest", name, "is 3 and 4")
    elif num1 == num3 and num1 == num2 and num1 > num4:
        print("The largest", name, "is 1, 2, and 3")
    elif num1 == num2 and num1 == num4 and num1 > num3:
        print("The largest", name, "is 1, 2, and 4")
    elif num1 == num3 and num1 == num4 and num1 > num2:
        print("The largest", name, "is 1, 3, and 4")
    elif num2 == num3 and num2 == num4 and num2 > num1:
        print("The largest", name, "is 2, 3, and 4")
    elif num1 == num2 and num1 == num4 and num1 > num3:
        print("The largest", name, "is 1, 2, and 4")
    elif num1 == num2 and num1 == num3 and num1 == num4:
        print("All the", name, "s are the same.")
    else:
        print("I quit.")

def removeNesting(y):
    for i in y:
        if type(i) == list:
            removeNesting(i)
        else:
            flatlist.append(i)
main()