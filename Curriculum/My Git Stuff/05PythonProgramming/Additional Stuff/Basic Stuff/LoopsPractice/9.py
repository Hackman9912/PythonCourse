#9. Write a program that uses nested loops to draw this pattern:
# *******
# ******
# *****
# ****
# ***
# **
# *

rows = 8
column = 7

for row in range(rows):
    for column in range (column):
        print("*", end="")
        
    print()
    
