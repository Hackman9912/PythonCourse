# This program reads the contents of the philosophers.txt file one lind at a time

# Def main function
def main():

    # Open a file named philophers.txt
    f = open('philosophers.txt', 'r')

    # Read one line at a time
    line1 = f.readline().rstrip('\n')
    line2 = f.readline().rstrip('\n')
    line3 = f.readline().rstrip('\n')

    # Close the file

    f.close()

    # Print the data that was read
    print(line1)
    print(line2)
    print(line3)

# Different ways to stip the extra space if not using r strip above
 #   print(line1, end='')
 #   print(line2, end='')
 #   print(line3, end='')
 #   print(line1.rstrip('\n')
 #   print(line2.rstrip('\n')
 #   print(line3.rstrip('\n')

# Call main
main()