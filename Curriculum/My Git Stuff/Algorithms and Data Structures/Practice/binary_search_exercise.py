'''
1. Suppose that a list contains the values 20, 44, 48, 55, 62, 66, 74, 88, 93, 99 
at index positions 0 through 9. Trace the values of the variables left, right, and 
midpoint in a binary search of this list for the target value 90. Repeat for the 
target value 44.
'''
"""
# define the funciton
def binarySearch(target, sortedList):
    # establish the two variables
    left = 0
    right = len(sortedList) - 1
    # make a while loop to search the list for the target value
    while left <= right:
        # set a mid point
        midpoint = (left + right) // 2
        # use print to trace the value
        print(f'The midpoint on my quest is {sortedList[midpoint]} the left is {left} and the right is {right}')
        # see if target matches the midpoint, if it does not then adjust the left and right bounds
        if target == sortedList[midpoint]:
            return midpoint
        elif target < sortedList[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    # if nothing can be found then send this back
    return 'not available. The number was not found'
# define list
my_list = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99 ]
# print the things and call the function
print('The search for 90.....')
print(f'The index for the selected number is {binarySearch(90, my_list)}')
print('The search for 44.....')
print(f'The index for the selected number is {binarySearch(44, my_list)}')
"""
'''
2(challenge). The method that’s usually used to look up an entry in a phone book is not 
exactly the same as a binary search because, when using a phone book, you don’t always go 
to the midpoint of the sublist being searched. Instead, you estimate the position of the 
target based on the alphabetical position of the first letter of the person’s last name. 
For example, when you are looking up a number for “Smith,” you look toward the middle of 
the second half of the phone book first, instead of in the middle of the entire book. 
Suggest a modification of the binary search algorithm that emulates this strategy for a 
list of names. Is its computational complexity any better than that of the standard 
binary search? 
'''
import re
def phoneLookup(name, phoneBook):
    left = 0
    right = len(phoneBook) - 1
    target = name.split()
    first_Letter = [targets[0] for targets in target]
    group1 = re.compile('[a-hA-H]').search
    group2 = re.compile('[i-pI-P]').search
    group3 = re.compile('[q-zQ-Z]').search
    if bool(group1(str(first_Letter))) == True:
        right = right - 2
    elif bool(group2(str(first_Letter))) == True:
        right = right -1
        left = left + 1
    elif bool(group3(str(first_Letter))) == True:
        left = left + 2
    else:
        print('That was a bad choice')
        exit()

    while left <= right:
            # set a mid point
            midpoint = (left + right) // 2
            # use print to trace the value
            print(f'The midpoint on my quest is {phoneBook[midpoint]} the left is {left} and the right is {right}')
            # see if target matches the midpoint, if it does not then adjust the left and right bounds
            mid = phoneBook[midpoint][0].split()
            midFLetter = [mid[0] for letters in mid]
            if str(name) == str(phoneBook[midpoint][0]):
                return phoneBook[midpoint]
            elif str(first_Letter) < str(midFLetter):
                right = midpoint - 1
            else:
                left = midpoint + 1
    # if nothing can be found then send this back
    return 'not available. The number was not found'

def main():
    phonebook = [['Avery', '123-123-1234'], ['Alex', '123-123-1234'], ['Bill', '123-123-1234'], ['Brady', '123-123-1234'], ['Brandy', '123-123-1234'], ['Chucky', '123-123-1234'], ['Champ', '123-123-1234'],
                ['Derek', '123-123-1234'], ['Danny', '123-123-1234'], ['Eustace', '123-123-1234'], ['Frank', '123-123-1234'], ['George', '123-123-1234'], ['Harry', '123-123-1234'], ['Terence', '123'], ['Zane', '123']]
    print(phoneLookup('Bill', phonebook))

main()