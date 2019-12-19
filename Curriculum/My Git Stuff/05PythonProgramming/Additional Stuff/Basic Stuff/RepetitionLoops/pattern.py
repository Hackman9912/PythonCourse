#***
#*****
#*****
#***
# This program displays a rectangular pattern of an asterisks
rows = int(input("How many rows? "))
cols = int(input("How many columns? "))

for row in range(rows):
    for column in range(cols):
        print("*", end"*")
    print()
