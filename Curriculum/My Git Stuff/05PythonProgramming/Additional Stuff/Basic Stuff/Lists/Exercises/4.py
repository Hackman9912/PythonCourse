"""
4. Number Analysis Program
Design a program that asks the user to enter a series of 20 numbers. The program should
store the numbers in a list and then display the following data:
• The lowest number in the list
• The highest number in the list
• The total of the numbers in the list
• The average of the numbers in the list
"""

def main():

    number = []
    total = 0 
    while len(number) <= 19:
        print("Enter a number for ", len(number)+1)
        num = int(input(": "))
        number.append(num)
    
    for count in number:
        total += count

    average = total/20
    minimum = min(number)
    maximum = max(number)
    min_index = number.index(minimum) + 1
    max_index = number.index(maximum) + 1

    print("The total is: ", total)
    print(f"The average is {average:.2f}")
    print("The place ", min_index, "on the list had the smallest number at: ", minimum)
    print("The place ", max_index, "on the list had the largest number at: ", maximum)

main()