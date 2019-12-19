#  7. Random Number File Writer
# Write a program that writes a series of random numbers to a file. Each random number should be in the range of 1 through 100. 
# The application should let the user specify howmany random numbers the file will hold.
import random

num_num = int(input("How many random numbers do you want to enter between the range of 1 and 100? "))

# Open a new file named sales2.txt
num_file = open('num.txt', 'w')

# Get the amount of sales for each day and write it to the file

for count in range(1, num_num+1):
    # Get the sales for a day
    number = random.randint(1, 101)
    write = str(number) + "\n"
    # write the sales amount to the file
    num_file.write(write)
# Close the file
num_file.close()
print('Data written to num.txt')