# Chris owns an auto repair business and has several emplyees. If
#  any employee works over 40 hours in a week, he must pay them 
# 1.5 times their regular hourly pay rate for all hours over 40.
#  He has asked you to design a simple payroll program that 
# calculates an employees gross pay, including any overtime wages. 

base_hours = 40
overtime_pay = 1.5
extra_pay = 0

hours = float(input("Insert the number of hours you have worked "))
base_pay = float(input("Enter your hourly pay "))

pay = base_hours*base_pay

if hours > base_hours:
    overtime_hours = hours - base_hours
    extra_pay = (overtime_pay*base_pay)*overtime_hours
    gross_pay = pay + extra_pay
else: 
    gross_pay = pay + extra_pay

print("Your gross pay is: $", gross_pay)


# Global constants

# BASE_HOURS = 40
#OT_MULTIPLIER = 1.5

# The main function gets the number of hours worked and the 
# hourly pay rate. It calls some functions to calculate and 
# display gross pay and OT

# def main():
    # Get hours worked and hourly payrate
    # hours_worked = float(input("Enter the number of hours worked: "))
    # pay_rate = float(input("Enter the hourly pay rate: "))


    # if hours_worked > BASE_HOURS:
        # overtime_pay = pay_rate * OT_MULTIPLIER * (hours_worked - BASE_HOURS)
        # Calculate the overtime pay
        # calc_pay_with_OT(hours_worked, pay_rate)
    # else:
        # Calc gross pay as usual
        # calc_reg_pay(hours_worked, pay_rate)

# def calc_pay_with_OT(hours, rate):
    # Calc overtime hours worked
    # overtime_hours = hours - BASE_HOURS

    # Calc the amount of overtime pay
    # overtime_pay = overtime_hours * OT_MULTIPLIER * rate

    # Calc the gross pay
    # gross_pay = BASE_HOURS*rate + overtime_pay

    # Display the gross pay
    # print("The gross pay is ${:.2f}  ".format(gross_pay))

# def calc_reg_pay(hours, rate):
    # Calc gross pay
    # gross_pay = hours*rate

    # Displays the gross pay
    # print("The gross pay is ${:.2f}  ".format(gross_pay))

# main()
