"""
1. Recursive Printing
    Design a recursive function that accepts an integer argument, n, and prints the numbers 1
    up through n.

"""
# define main
def main():
    # set up variables
    n = int(input('Enter the number you want the sequence to count through: '))
    # call counter()
    counter(n)
# define counter
def counter(n):
    # if n is greater than 0 then subtract n and pass back through the function
    if n > 0: counter(n - 1)
    # once n is to 0 then print the numbers
    print (n, sep=" ")


'''    # if the values equal eachoter then print
    if n == m:
        print(m)
    else:
        # If they do not print m then call the function again adding 1 to m so it increments
        print(m)
        return counter(n, m + 1)'''

# call main
main()