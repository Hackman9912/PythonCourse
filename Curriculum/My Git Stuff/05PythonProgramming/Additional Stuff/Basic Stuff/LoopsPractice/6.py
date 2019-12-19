# 6. Celsius to Fahrenheit Table
# Write a program that displays a table of the Celsius temperatures 0 through 20 and theirFahrenheit equivalents. 
# The formula for converting a temperature from Celsius toFahrenheit is
# F = (9/5)C + 32 where F is the Fahrenheit temperature and C is the Celsius temperature. 
# Your programmust use a loop to display the table.
fahr = [((9/5) * cel + 32) for cel in range(21)]
for x, y in enumerate(fahr):
    print(f'{x:} celcius is {y:.2f} fahrenheit.')


