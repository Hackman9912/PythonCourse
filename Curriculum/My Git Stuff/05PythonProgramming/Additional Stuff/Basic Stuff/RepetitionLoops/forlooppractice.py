# this program demonstrates a simple for loop using a list of numbers

def main():
    print("I will display a list of numbers 1 to 5.")
    for i in range(5, 10, 2):
        print(i)

    # calc a sum of a series of num entered by user

    MAX = 5

    # set accumulator

    total = 0.0 

    print(f"This program calculates the sum of {MAX:} numers you will enter")
    for counter in range(MAX):
        number = int(input("Enter a number: "))
        total = total + number
    
    # display total
    print("The total is", total)




main()