# This programs prompts the user for sales amounts and writes those amounts to the sales2.txt file

def main():

    num_days = int(input("For how many days do you have sales? "))

    # Open a new file named sales2.txt
    sales_file = open('sales2.txt', 'w')

    # Get the amount of sales for each day and write it to the file

    for count in range(1, num_days+1):
        # Get the sales for a day
        sales = float(input("Ender the sales for day # "+\
                            str(count) + ': '))
        # write the sales amount to the file
        sales_file.write(str(sales) + '\n')
    # Close the file
    sales_file.close()
    print('Data written to sales2.txt')

# Call main
main()

