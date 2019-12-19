"""
2. Lottery Number Generator
Design a program that generates a seven-digit lottery number. The program should 
generate seven random numbers, each in the range of 0 through 9, and assign each 
number to a list element. Then write another loop that displays the contents of the 
list.

"""

import random

def main():
    lotto = []
    count = 0 

    while count <= 6:
        number = random.randint(0, 9)
        lotto.append(number)
        count += 1
    
    print(lotto)

main()