"""
3. Rainfall Statistics
Design a program that lets the user enter the total rainfall for each of 12 months into a list.
The program should calculate and display the total rainfall for the year, the average monthly
rainfall, and the months with the highest and lowest amounts.
"""

def main():

    rainFall = []
    total = 0 
    while len(rainFall) <= 11:
        print("Enter the rainfall for month", len(rainFall)+1)
        rain = int(input(": "))
        rainFall.append(rain)
    
    for num in rainFall:
        total += num

    average = total/12
    minimum = min(rainFall)
    maximum = max(rainFall)
    min_index = rainFall.index(minimum) + 1
    max_index = rainFall.index(maximum) + 1

    print("The total is: ", total)
    print(f"The average is {average:.2f}")
    print("Month ", min_index, "had the lowest amount of rain at: ", minimum, "inches.")
    print("Month ", max_index, "had the largest amount of rain at: ", maximum, "inches.")

main()