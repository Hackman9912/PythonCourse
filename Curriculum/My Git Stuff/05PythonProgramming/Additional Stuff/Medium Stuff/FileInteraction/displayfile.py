# This program display the contents of a file
def main():
    # Get the name of a file
    filename = input("Enter a filename: ")

    # Open the file
    infile = open(filename, 'r')

    # Read the files contents
    contents = infile.read()

    # Display contents
    print(contents)

    # CLose file
    infile.close()
# Call main
main()