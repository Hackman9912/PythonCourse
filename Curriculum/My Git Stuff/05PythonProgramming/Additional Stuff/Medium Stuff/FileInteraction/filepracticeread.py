# This program reads and displays the contents of the philosophers.txt file

def main():
    # Open the file named philosophers.txt
    f = open('philosophers.txt', 'r')

    # Read the files contents
    f_contents = f.read()

    # Close the file
    f.close()

    # Print the data that was read into memory

    print(f_contents)

# Call the main function
main()