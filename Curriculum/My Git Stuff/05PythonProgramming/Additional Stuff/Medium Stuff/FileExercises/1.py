# 1. File Display
# Create a file containing a series of integers named numbers.txt. Write a program that displays all of the numbers in the file.

with open(r'numbers.txt', 'r') as file:

    line = file.readline()

    # As long as an empty string is not returned form readline, condinue processing
    while line != '':
        # Convert line to a float
        amount = int(line)
        # Format and display data
        print(amount)
        # Read the next line
        line = file.readline()