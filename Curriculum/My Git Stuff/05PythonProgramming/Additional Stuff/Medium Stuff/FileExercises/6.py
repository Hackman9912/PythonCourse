# 6. Average of Numbers 
# Assume that a file containing a series of integers is named numbers.txt and exists on thecomputer’s disk. 
# Write a program that calculates the average of all the numbers stored in the file.

# Define counter
count = 0

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
    # Increment count and total
    count += 1
    total += display
    # Format and display data
    print(display)
    # Read the next line
    line = infile.readline()
print(f"\n The average of the lines is {total/count:.2f}")