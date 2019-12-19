# 11. Time Calculator
# Write a program that asks the user to enter a number of seconds, and works as follows:
# • There are 60 seconds in a minute. If the number of seconds entered by the user is greater
# than or equal to 60, the program should display the number of minutes in that many
# seconds.
# • There are 3,600 seconds in an hour. If the number of seconds entered by the user is
# greater than or equal to 3,600, the program should display the number of hours in that
# many seconds.
# • There are 86,400 seconds in a day. If the number of seconds entered by the user is greater
# than or equal to 86,400, the program should display the number of days in that many
# seconds

def main():

    seconds = float(input("Enter a number of seconds: "))
    convert(seconds)

def convert(num1):
    if num1 >= 60 and num1 < 3600:
        minutes = num1/60
        print (f"You entered {minutes:.2f} minutes.")
    elif num1 >= 3600 and num1 < 86400:
        hours = num1/3600
        print (f"You entered {hours:.2f} hours.")
    elif num1 >= 86400:
        days = num1/86400
        print (f"You entered {days:.2f} days.")
    else:
        print (f"You entered {num1:.2f} seconds. ")

main()