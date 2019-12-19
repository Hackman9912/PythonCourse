# 5. Sum of Numbers
# Assume that a file containing a series of integers is named numbers.txt and exists on the computer’s disk. 
# Write a program that reads all of the numbers stored in the file and calculates their total.

# Define total
total = 0

# Open the file
infile = open("numbers.txt", 'r')

# Set readline
line = infile.readline()

# Display first 5 lines
while line != '':
    # Convert line to a float
    display = int(line)
    # Increment count
    total += display
    # Format and display data
    print(display)
    # Read the next line
    line = infile.readline()
print(f"\n The total of the lines is {total:}")