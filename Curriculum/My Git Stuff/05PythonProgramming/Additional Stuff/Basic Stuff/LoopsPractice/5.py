# 5. Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
# The program should first ask for the number of years. The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
# After all iterations,the program should display the number ofmonths, the total inches of rainfall, and the average rainfall per month for the entire period.

monthdict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
months = 0
years = int(input("Enter a number of years to enter rainfall data for: "))
total_rainfall = 0
 
for i in range(years):
    for key in monthdict:
        rainfall = float(input(f"Enter the rainfall for {monthdict.get(key):}: "))
        total_rainfall += rainfall
        months += 1

average = total_rainfall / months

print(f"The total rainfall per  for {months:} months is", total_rainfall, "\n"
f"The average rainfall a month is {average:}"
)