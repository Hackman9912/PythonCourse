# Built in functionality for lists

# Append

def main():
    name_list = []

    # Create a variable to control our loop
    again = "y"

    # Add some names to the list
    while again == "y":
        # Get a name from the user
        name = input("Enter a name: ")

        name_list.append(name)

        print("Do you want to add another name? ")
        again = input("y = yea, anything else = no: ")

        print()

    print("Here are the names you entered: ")
    for name in name_list:
        print(name)


# Index function

# This program shows how to get the index of an item in a list and then replace that item with a new item

def main():

    food = ["pizza", "burgers", "chips"]

    print("Here are the items in the food list: ")
    print(food)
    item = input("Which item should I change? ")

    try:
        # Get the item index in the list
        item_index = food.index(item)

        # Get the value to replace it with
        new_item = input("Enter a new value: ")

        # Replace the old item with the new item
        food[item_index] = new_item

        print("Here is the revised list: ")
        print(food)

    except:
        # User entered the wrong thing
        print("That item was not found in the list.")

main()



# This program demonstrates the insert method

def main():

    names = ["James", "Kathy", "Bill"]

    # Display the list
    print("This list before insert: ")

    print(names)

    names.insert(0, "Joe")

    print("This list after the insert: ")

    print(names)


main()


# Sort method on lists

my_list = [9, 5, 7, 3, 2, 1, 0]

print("Original order: ", my_list)
my_list.sort()
print("Sorted order: ", my_list)

# Sorted - not permanent and list.sort is faster

my_list2 = [9, 5, 7, 3, 2, 1, 0]
print("Before sort", my_list2)
print(sorted(my_list2))
print("After sort", my_list2)


# This program shows how to use the romove method from a list

def main():

    food = ['pizza', 'burgers', 'chips']

    print("Here are the foods ", food)

    item  = input("Which item would I remove: ")

    try:

        food.remove(item)

        print('Here is the revised list ', food)

    except ValueError:
        print(' That item was not found: ')

main()


# The reverse method

my_list = [1, 2, 3, 4, 5, 6]
print('Original order: ', my_list)

my_list.reverse()

print('Reversed', my_list)

# The delete statement: for specific elements

my_list = [1, 2, 3, 4, 5]

print('Here is the list: ', my_list)

del my_list[2]
print('After deletion: ', my_list)


# min and max funciton

my_list = [5, 4, 7, 8, 3, 2, 0, 9, 1]
print("The lowest value is: ", min(my_list))

print('The highest value is: ', max(my_list))


# copyting lists in python

list1 = [1, 2, 3, 4, 5]


# assign the list to the list to variable
list2 = list1

print(list1)
print(list2)

# Replace part of the list

list1[0] = 99
print(list1)
print(list2)

# copoy of the list that references two separate but identical lists

list3 = [1, 2, 3, 4, 5]
list4 = []

print("OG list 3", list3)
print("OG 4", list4)

for item in list3:
    list4.append(item)

print("step 2", list3)
print("step 2", list4)

list3[0] = 99

print("step 3", list3)
print("step 3", list4)

# pass list to an argument as a funciton

# calc total value of the list

def main():
    numbers = [2, 4, 6, 8, 10]
    print("The total is", get_total(numbers))



# The get_total function accepts a list as an argument

def get_total(value_list):
    # Create an accumulator
    total = 0

    for num in value_list:
        total += num

    return total


main()


# files and lists

# This program uses the writelines method to save a list of string to a file

def main():
    # Create a lis of strings
    cities = ['New York\n', 'Austin\n', 'Boston\n', 'Atlatna\n', 'Dallas\n']

    outfile = open('cities.txt', 'w')

    for item in cities:
        outfile.writelines(item)

    outfile.close()

main()


# This program reads the contents

def main():
    infile = open('cities.txt', 'r')

    cities_read_in = infile.readlines()

    infile.close()

    index = 0

    while index < len(cities_read_in):
        cities_read_in[index] = cities_read_in[index].rstrip('\n')
        index += 1

    print(cities_read_in)

main()



# 2 dimensional list (nested lists or lists within lists)

students = [['joe', 'kim'], ['Sam', 'Sue'], ['Kelly', 'Christ']]
print(students)

print(students[0])
# Print Joe
print(students[0][0])
# Print Sue
print(students[1][1])


# This program assigns random numbers to a 2-D list

import random


# Constants for rows an collumnds

ROWS = 3
COLUMNS = 4

def main():
    # Create 2D list
    values = [[0, 0, 0 , 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    
    # Fill the list with random numbers
    for r in range(ROWS):
        for c in range(COLUMNS):
            values[r][c] = random.randint(1, 100)

    print(values)

main()