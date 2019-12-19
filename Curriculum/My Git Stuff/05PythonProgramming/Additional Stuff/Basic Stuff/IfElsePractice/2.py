# 2. Areas of Rectangles
# The area of a rectangle is the rectangle’s length times its width. Write a program that asks
# for the length and width of two rectangles. The program should tell the user which rectangle
# has the greater area, or if the areas are the same.

length_one = int(input("Please enter the length of your first rectangle: "))
width_one = int(input("Please enter the width of your first rectangle: "))
area_one =  length_one*width_one

length_two = int(input("Please enter the length of your second rectangle: "))
width_two = int(input("Please enter the width of your second rectangle: "))
area_two = length_two*width_two

if area_one > area_two:
    print("The first rectangle is bigger.")
elif area_one < area_two:
    print("The second rectangle is bigger.")
else:
    print("The rectangles are same same.")
    