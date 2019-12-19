# 5. Color Mixer
# The colors red, blue, and yellow are known as the primary colors because they cannot be
# made by mixing other colors. When you mix two primary colors, you get a secondary color,
# as shown here:
# When you mix red and blue, you get purple.
# When you mix red and yellow, you get orange.
# When you mix blue and yellow, you get green.
# Design a program that prompts the user to enter the names of two primary colors to mix.
# If the user enters anything other than “red,” “blue,” or “yellow,” the program should display an 
# error message. Otherwise, the program should display the name of the secondary color that results.

def main():
    color_one = color()
    checker(color_one)
    color_two = color()
    checker(color_two)
    blender(color_one, color_two)



def checker(color):
    if color == "red" or color == "blue" or color == "yellow":
        print("You chose", color)
    else:
        print("Choose one of the primary colors!")
        exit()
def color():
    return input("Enter 'red', 'blue', or 'yellow'. ")

def blender(first, second):
    if (first == "red" or second == "red") and (first == "blue" or second == "blue"):
        print("Your blend is purple")
    elif (first == "yellow" or second == "yellow") and (first == "blue" or second == "blue"):
        print("Your blend is green")
    elif (first == "red" or second == "red") and (first == "yellow" or second == "yellow"):
        print("Your blend is orange")
    else:
        print("Your colors were the same")

main()