# 8. Stadium Seating
# There are three seating categories at a stadium. For a softball game, Class A seats cost $15,Class B seats cost $12, and Class C seats cost $9. 
# Write a program that asks how many tickets for each class of seats were sold, and then displays the amount of income generated fromticket sales.


def main():

    a_seat = int(input("Enter the number of seats sold for section a: "))
    b_seat = int(input("Enter the number of seats sold for section b: "))
    c_seat = int(input("Enter the number of seats sold for section c: "))
     

    
        
        
    a_cost = cost(a_seat, 15)
    b_cost = cost(b_seat, 12)
    c_cost = cost(c_seat, 9)
    total = a_cost + b_cost + c_cost

    print("You sold $", total, "worth of tickets.")
def cost(num1, num2):
    return num1*num2

main()
