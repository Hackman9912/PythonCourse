"""
1. The list method reverse reverses the elements in the list. Define a function named reverse that 
reverses the elements in its list argument (without using the method reverse). Try to make this 
function as efficient as possible, and state its computational complexity using big-O notation. 

"""
'''
# O(n)
# define the funciton to reverse the list
def reverselist(my_list, new_list, in2):
    # If in2 is greater than 0
    if in2 >= 0:
        # append to the new list the my_list item at index of in2
        new_list.append(my_list[in2])
        # send everything back through but subtract 1 from in2
        reverselist(my_list, new_list, in2 - 1)
    # when in2 is no longer a valid index then return the new list
    return new_list
# define the function to get a list
def get_list(num, count, list1):
    # while the count is less than the length of the list the user wants
    if count < num:
        # append to the list what the user wants
        list1.append(input('Enter an item to be on the list: '))
        # pass to the function and add 1 to count
        get_list(num, count + 1, list1)
    # When the count is equal to the num the user wants then return the list
    return list1

# define the main function
def main():
    # get how big the user wants the list to be
    num = int(input('Enter the length you want the list to be: '))
    # get a list
    my_list = get_list(num, 0, [])
    # print the list to show it all fancy like
    print(my_list)
    # set my_list to be the original list sent to the function
    my_list = reverselist(my_list, [], len(my_list)-1)
    # print the new my list
    print(my_list)
# call main
main()
'''
'''
# O(n log n)
def quicksort(my_list):
    quicksortHelper(my_list, 0, len(my_list) - 1)
 
# recursive function to hide extra arguments for the endpoints of a sublist
def quicksortHelper(my_list, left, right):
    if left < right:
        pivotlocation = partition(my_list, left, right)
        # recursively calls quicksortHelper for the left of the partition
        quicksortHelper(my_list, left, pivotlocation - 1)
        # recursively calls quicksortHelper for the right of the partition
        quicksortHelper(my_list, pivotlocation + 1, right)
 

def partition(my_list, left, right):
    # find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = my_list[middle]
    my_list[middle] = my_list[right]
    my_list[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if my_list[index] > pivot:
            swap(my_list, index, boundary)
            boundary += 1
    # exchange the pivot item and the boundary item
    swap(my_list, right, boundary)
    return boundary

# The swap function
def swap(my_list, i, j):
    # exchanges the position of i and j
    temp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = temp

import random

def main(size = 35, sort_this = quicksort):
    my_list = []
    for _ in range(size):
        my_list.append(random.randint(1, size + 1))
    print(f'Unsorted list: \n{my_list}')
    sort_this(my_list)
    print(f'Sorted list: \n{my_list}')


main()
'''
"""
2. Python’s pow function returns the result of raising a number to a given power. Define a function 
expo that performs this task and state its computational com-plexity using big-O notation. The first 
argument of this function is the number, and the second argument is the exponent (nonnegative numbers only). 
You can use either a loop or a recursive function in your implementation, but do not use Python’s ** operator 
or pow function. 

O(k^n)
"""
'''
# This function asks the user for 2 numbers and raises the first number to the power of the second
# define the exponent function
def exp(num, power):
    # establish our local variable
    num1 = num
    # While the power is greater than 1
    while power > 1:
        # multiply the things together
        num1 = num1 * num
        # subtract 1 from power
        power -= 1
    # send num1 back
    return num1
# define the main fucntion
def main():
    # set our numbers to be negatives
    num = -1
    power = -1
    # while the numbers are not positive ask the user for input
    while num < 0 or power < 0:
        # try to get the proper inputs. If the user puts in something wrong then keep trying
        try:
            num = float(input("Enter a number 0 or greater to raise to a power: "))
            power = float(input("Enter a number 0 or greater to raise a number by: "))
        except:
            num = -1
            power = -1
    # print the number
    print(exp(num, power))
# call main
main()
'''
'''
# define main
def main():
    # Establish vars
    int1 = int(input("Enter the first integer: "))
    int2 = int(input("Enter the second integer: "))
    count = 1
    tot = 1
    # pass to function
    exp(int1, int2, count, tot)
# define exponent
def exp(x, y, z, a):
    # if z is greater than the exponent then print the formatted number
    if z > y:
        print(f'{a:,.2f}')
    # If not cal lthe function again passing z, y and z plus 1 and the total times the base number 
    else:
        return exp(x, y, z + 1, a * x)
# call main
main()
'''