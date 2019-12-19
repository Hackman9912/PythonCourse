# This program uses the recursive to print numbers from the Fibonacci series
# Define the main function
def main():
    print('The first 10 numbers in the')
    print('Fibonacci series are:')

    for number in range(0, 10):
        print(fibonacci(number))

# The fibonacci function returns the nth number in the fibonacci series
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# call main
main()