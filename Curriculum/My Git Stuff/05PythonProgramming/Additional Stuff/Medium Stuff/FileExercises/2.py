# 2. File Head Display
# Write a program that asks the user for the name of a file. The program should display only the first five lines of the file’s contents. 
# If the file contains less than five lines, it should display the file’s entire contents.

# Define counter
count = 0

# Get file name
filename = input("Enter a filename: ")

# Tries to do the things and will except if has an error
try:

    # Open the file
    infile = open(filename, 'r')

    # Set readline
    line = infile.readline()

    # Display first 5 lines
    while count < 5:
        # Convert line to a float
        amount = float(line)
        # Increment count
        count += 1
        # Format and display data
        print(amount)
        # Read the next line
        line = infile.readline()

   
# If file doesn't exist, show this error message
except IOError:
    print("\n An error occured trying to read")
    print("the file", filename, "\n")