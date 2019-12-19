# 2. Calories Burned
# Running on a particular treadmill you burn 3.9 calories per minute. 
# Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30minutes.

def main():

    cal = [(i * 3.9) for i in range(10, 31, 5)]
    for x, y in enumerate(cal, 1):
        print(f'You burned {x} calories in {y} minutes.')
    
    
    # replaced with list comprehension and enumeration
    # min_cal = 3.9

    # for i in range(10, 31, 5):
    #     cal = i * min_cal
    #     print(f"You burned {cal:.2f} calories " f"in {i:} minutes")

main()