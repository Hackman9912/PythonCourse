# Write a program that displays the following information:
# • Your name
# • Your address, with city, state, and ZIP
# • Your telephone number
# • Your MOS

# Input data
name = input("Input your name here please ")
addy = input("Put in your address as: address, city, state, ZIP ")
phone = input("Put your phone number in now ")
MOS = input("Please put your MOS or AFSC in now ")

# Output data
print('{:>5}'.format("Your info is as follos: "), 
    name, addy, phone, MOS
    )

# A company has determined that its annual profit is typically 23 
# percent of total sales. Write a program that asks the user to enter 
# the projected amount of total sales, and then displays the profit 
# that will be made from that amount

# Get the sales
projected_sales=float(input("Input your projected amount of total sales: "))

# Calc the profit

profit=projected_sales*.23

# Output the data
print(f"Profit should be{profit}")


#  One acre of land is equivalent to 43,560 square feet. Write a 
# program that asks the user to enter the total square feet in a tract 
# of land and calculates the number of acres in the tract.

# Input the data
feet=float(input("Input the number of square feet in your tract of land "))

# Do the math
acre=feet/43560

print(f"You have {acre} acres in your land")

# A customer in a store is purchasing five items. Write a program that 
# asks for the price of each item, and then displays the subtotal of 
# the sale, the amount of sales tax, and the total. Assume the sales 
# tax is 6 percent.

# Set the tax

tax=float(".06")

# How many items
count = input("Enter the number of items you purchased")
# What you wrote
print(f"You purchased {count} items ")

# Input prices
item_one = float(input("Enter the price of item one: "))

item_two = float(input("Enter the price of item two: "))

item_three = float(input("Enter the price of item three: "))

item_four = float(input("Enter the price of item four: "))

item_five = float(input("Enter the price of item five: "))

# Add em up
sub_total = item_one + item_two + item_three + item_four + item_five

# Get sales tax
sales_tax = sub_total*tax

# Get total
total = sales_tax + sub_total

#Output the data
print(f"Your subtotal, sales tax and total are {sub_total, sales_tax, total}")


# Assuming there are no accidents or delays, the distance that a car travels down 
# the interstate can be calculated with the following formula:
# Distance = Speed * Time
# A car is traveling at 60 miles per hour. Write a program that displays the following:
# • The distance the car will travel in 5 hours
# • The distance the car will travel in 8 hours
# • The distance the car will travel in 12 hours

# Set speed
speed = 60

#Establish time
time = ""

#Establish math
distance = speed*time

# Do the math
five_hours = speed*5
eight_hours = speed*8
twelve_hours = speed*12


# Output the data
print(f"Your distance at 5, 8 and 12 hours is{five_hours, eight_hours, twelve_hours}")

# Write a program that will ask the user to enter the amount of a purchase. The program
# should then compute the state and county sales tax. Assume the state sales tax is 4 
# percent and the county sales tax is 2 percent. The program should display the amount 
# of the purchase, the state sales tax, the county sales tax, the total sales tax, and 
# the total of the sale (which is the sum of the amount of purchase plus the total 
# sales tax).

# Declare the important things

purchase = ""
state_tax = ""
county_tax = ""
total_tax = ""
total_sale = ""
state_sales = float(".04")
county_sales = float(".02")

# Get the input

purchase = float(input("Enter your purchase amount: "))

# Do the math

state_tax = purchase*state_sales
county_tax = purchase*county_sales
total_tax = county_tax+state_tax
total_sale = purchase+total_tax

# Print the outputs

print(f"Your purchase price is: {purchase:6.2f}")
print(f"Your state tax is: {state_tax:6.2f}")
print(f"Your county tax is: { county_tax:6.2f}")
print(f"Your total tax  is: { total_tax:6.2f}")
print(f"And your total sale price is: {total_sale :6.2f}")

# A car’s miles-per-gallon (MPG) can be calculated with the following formula: 
# MPG = Miles driven / Gallons of gas used
# Write a program that asks the user for the number of miles driven and the gallons of 
# gas used. It should calculate the car’s MPG and display the result.

# Declare important things

miles = ""
gallons = ""

# Get inputs
miles = float(input("Please put in the number of miles driven: "))
gallons = float(input("Please put in the number of gallons of gas used: "))

# Do the maths
mpg = miles/gallons

# Tell the user
print(f"Your car gets {mpg} MPG")


# Write a program that calculates the total amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the charge for the food, and then calculate 
# the amount of a 15 percent tip and 7 percent sales tax. Display each of these amounts 
# and the total.

# Declare the things
charge = ""
tip = ""
tax = ""
total = ""
tip_amount = .15
tax_amount = .07

# Get the initial charge
charge = float(input("Enter the amount for your food "))

# Do the math
tip = charge*tip_amount
tax = charge*tax_amount
total = charge+tip+tax

# Output data for the user
print(f"Your initial purchase price was{charge}")
print(f"Your tax is {tax}")
print(f"Your tip should be {tip}")
print(f"Your total cost will be {total}")


# Write a program that converts Celsius temperatures to Fahrenheit temperatures. The 
# formula is as follows:
#F = (9/5)C + 32
#The program should ask the user to enter a temperature in Celsius, and then display 
# the temperature converted to Fahrenheit.

# Enter the temp
celcius = float(input("Enter the temp in degrees C : "))

# Do the math
fahr = (9/5)*celcius+32

# Output the things
print(f"Your temp in fahrenheit is {fahr}")


# Last month Joe purchased some stock in Acme Software, Inc. Here are the details of the
# purchase:
# • The number of shares that Joe purchased was 1,000.
# • When Joe purchased the stock, he paid $32.87 per share.
# • Joe paid his stockbroker a commission that amounted to 2 percent of the amount he paid
# for the stock.
# Two weeks later Joe sold the stock. Here are the details of the sale:
# • The number of shares that Joe sold was 1,000.
# • He sold the stock for $33.92 per share.
# • He paid his stockbroker another commission that amounted to 2 percent of the amount
# he received for the stock.
# Write a program that displays the following information:
# • The amount of money Joe paid for the stock.
# • The amount of commission Joe paid his broker when he bought the stock.
# • The amount that Joe sold the stock for.
# • The amount of commission Joe paid his broker when he sold the stock.
# • Display the amount of money that Joe had left when he sold the stock and paid his
# broker (both times). If this amount is positive, then Joe made a profit. If the amount is
# negative, then Joe lost money


shares = 32.87
amount = 1000
bought = shares*amount
broker = .02*bought

share_sold = 33.92
sold = share_sold*amount
broker_sold = .02*sold

total_paid = broker+bought
total_broker = broker+broker_sold

final = bought - total_broker - sold

print("You bought the stock for", bought) 
print("Paid the broker", broker)
print("Then sold it for", sold)
print("and paid the broker", broker_sold) 
print(f"your bottom line is {final:6.2f}", )