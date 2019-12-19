# This program reads all of the values in the sales2.txt file

def main():
    # Open the sales2.txt for reading
    sales_file = open('sales2.txt', 'r')

    # Read the first line form the file, but do not convert to a number yet. We still need to test any empty stting
    line = sales_file.readline()

    # As long as an empty string is not returned form readline, condinue processing
    while line != '':
        # Convert line to a float
        amount = float(line)
        # Format and display data
        print(format(amount, '.2f'))
        # Read the next line
        line = sales_file.readline()
    # Close the file
    sales_file.close()
# Call main
main()