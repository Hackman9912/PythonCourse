# 4. Item Counter
# Assume that a file containing a series of names (as strings) is named names.txt and exists on the computer’s disk. 
# Write a program that displays the number of names that are stored in the file. (Hint: Open the file and read every 
# string stored in it. Use a variable to keep a count of the number of items that are read from the file.)

# Define counter
count = 0

# Open the file
infile = open("names.txt", 'r')

# Set readline
line = infile.readline()

# Display first 5 lines
while line != '':
    # Convert line to a float
    display = str(line)
    # Increment count
    count += 1
    # Format and display data
    print(display)
    # Read the next line
    line = infile.readline()
# Print the count
print(f"\n There were {count:} lines read.")