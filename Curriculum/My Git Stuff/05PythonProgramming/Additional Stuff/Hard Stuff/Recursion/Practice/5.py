"""
5. Recursive List Sum
    Design a function that accepts a list of numbers as an argument. The function should recursively 
    calculate the sum of all the numbers in the list and return that value.
"""
# Define main
def main():
    # Establish the list and variables
    list1 = [100,25,63,99,85]
    # pass all to the function
    largest(list1, 0, 0)
# define the largest function
def largest(x, y, sum):
    # if y is the same as the length of the list then print the sum
    if y == len(x):
        print(sum)
    # if not then see if big is bigger then the selected item on the list
    else:
        # call the function again passing all the things and setting the counter plus 1 and adding the sum
        return largest(x, y + 1, sum + x[y])

main()

# 5.
# numList = [3,4,5,6]
# def sum_nums(numlist):
#     n = len(numlist)
#     if len(numlist) == 1:
#         return numlist[0]
#     else:
#         return numlist[n-1] + sum_nums(numlist[0:n-1])

# print(sum_nums(numList))