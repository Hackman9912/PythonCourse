# This program display the contents of a file
def main():
    # Get the name of a file
    filename = input("Enter a filename: ")
    # Tries to do the things and will except if has an error
    try:
        # Open the file
        infile = open(filename, 'r')

        # Read the files contents
        contents = infile.read()

        # Display contents
        print(contents)

        # CLose file
        infile.close()

    except IOError:
        print("\n An error occured trying to read")
        print("the file", filename, "\n")

# Call main
main()