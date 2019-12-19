# 8. Random Number File Reader
# This exercise assumes you have completed Programming Exercise 7, Random Number File Writer. 
# Write another program that reads the random numbers from the file, display the numbers, and then display the following data:
# • The total of the numbers
# • The number of random numbers read from the file

# Define counter and total
count = 0
total = 0

# Open the file
infile = open("num.txt", 'r')

# Set readline
line = infile.readline()

# For aesthetics
print("\n")

# Display lines with data
while line != '':

    # Convert line to a int
    display = int(line)

    # Increment count and total
    count += 1
    total += display

    # Format and display data
    print(display)

    # Read the next line
    line = infile.readline()

# Print all the things
print(f"\n The average of the lines is {total/count:.2f}.."
    f"\n The total of the random numbers is {total:}.."
    f"\n The number of random numbers in the file is {count:}.\n"
    )