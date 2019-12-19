# 1. Bug Collector
# A bug collector collects bugs every day for seven days. Write a program that keeps a running total of the number of bugs collected during the seven days. 
# The loop should ask forthe number of bugs collected for each day, and when the loop is finished, the programshould display the total number of bugs collected.
def main():

    # counter = 1
    # total = 0
    bugs = [int(input(f"Enter the bugs you caught on day {i+1}: ")) for i in range(7)]
    print(f'The total number of bugs you caught is {sum(bugs)}')



    #replaced with the above
    # while counter <= 7:
    #     bugs = int(input(print("The date you entered is not magic")"))
    #     total += bugs
    #     counter += 1
    # print(f"You caught {total:} bugs in the past 7 days")

main()