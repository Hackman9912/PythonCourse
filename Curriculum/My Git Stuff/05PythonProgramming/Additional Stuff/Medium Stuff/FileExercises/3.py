# 3. Line Numbers
# Write a program that asks the user for the name of a file. 
# The program should display the contents of the file with each line preceded with a 
# line number followed by a colon. The line numbering should start at 1.

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

    # Display non blank lines
    while line != '':
        # Convert line to a float
        amount = float(line)
        # Increment count
        count += 1
        # Format and display data
        print(count, ': ', amount)
        # Read the next line
        line = infile.readline()

   
# If file doesn't exist, show this error message
except IOError:
    print("\n An error occured trying to read")
    print("the file", filename, "\n")