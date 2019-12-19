# 8. Sum of Numbers
# Write a program with a loop that asks the user to enter a series of positive numbers. The
# user should enter a negative number to signal the end of the series. After all the positive
# numbers have been entered, the program should display their sum.

check_sum = 0
sum = 0

while check_sum >= 0:
    check_sum = float(input("Enter positive numbers to be added together. When done enter a negative number: "))
    sum += check_sum

print(sum)