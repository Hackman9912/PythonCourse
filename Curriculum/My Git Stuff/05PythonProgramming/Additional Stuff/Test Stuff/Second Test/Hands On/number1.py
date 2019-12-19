'''
1. Recursion
    Have a user input a list of at least 5 integers. Write a function to find the 
    GCD (greatest common divisor) of two randomly selected numbers from the list by 
    using recursion. Output the answer to the terminal.

    The greatest common divisor of two or more integers, which are not all zero, is 
    the largest positive integer that divides each of the integers. For example, the 
    gcd of 8 and 12 is 4.
'''
# import random
import random
# define the main function
def main():
    # Make an empty list
    list1 = []
    # do this 5 times
    for i in range(5):
        # try to append to the list, if it will not then pass to the except
        try:
            list1.append(int(input(f'Enter a positive whole number for number {i + 1} of 5 to find a gcd of 2 random numbers of the 5 you enter:')))
        # scold the user and call back to main
        except:
            print('Enter a whole positive number.')
    var1 = list1.pop(random.randint(0, len(list1)-1))
    var2 = list1.pop(random.randint(0, len(list1)-1))
    # use print to call the function to randomly spit out list items and send to the function gcd
    print(f'The GCD for {var1} and {var2} is: {gcd(var1, var2)}')

# define the fcd function
def gcd(a, b):
    # if b is 0 then you return a
    if b == 0:
        return a
    # if not then send it back through the recursive function for math
    else:
        return gcd(b, a % b)

main()