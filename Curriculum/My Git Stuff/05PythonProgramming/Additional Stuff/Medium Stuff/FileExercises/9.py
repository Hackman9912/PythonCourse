# 9. Exception Handing
# Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
# • It should handle any IOError exceptions that are raised when the file is opened and datais read from it.

# Define counter
count = 0

# Define total
total = 0

try:
    # Display first 5 lines
    
    # Open the file
    infile = open("numbers.txt", 'r')

    # Set readline
    line = infile.readline()

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

# If file doesn't exist, show this error message
except:
    print(f"\n An error occured trying to read numbers.txt")
    if count > 0:
        print(f" to include line {count:} \n")