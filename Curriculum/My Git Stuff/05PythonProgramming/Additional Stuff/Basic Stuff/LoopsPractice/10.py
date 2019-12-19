# 10. Write a program that uses nested loops to draw this pattern:
# ##
# # #
# #  #
# #   #
# #    #
# #     #
# (add a space in between the symbol every row after the first row)
rows = 6
column = 7
for row in range(1, rows):
    count = ""
    print("#", count, "#")
    for column in range (column):
        if column <= rows:
            count += ""
 #           print(count, end="")
        else:
            count += " #"
    

    print(" ")
       
