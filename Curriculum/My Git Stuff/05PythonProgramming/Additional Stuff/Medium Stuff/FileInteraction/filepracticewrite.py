# file_variable = open(filename, mode)

# This program writes 5lines of data to a file

def main():
    # Open a file (will make a new one if it doesnt exist)
    f = open(r'C:\Users\student\Documents\sales.txt', 'w')

    # Write the data \n is new line
    f.write('1000.0\n2000.0\n3000.0\n4000.0\n5000.0\n')

    # Close the file
    f.close()

# Call the main function
main()