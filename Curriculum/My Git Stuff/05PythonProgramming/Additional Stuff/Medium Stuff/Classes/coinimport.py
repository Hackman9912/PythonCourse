# This program imports the ocin module and creates an instance of the Coin Class
# needs to be the file name or file path if in a different directory
import coin

def main():
    # create an object from the ocin class
    # needs the filename.module
    my_coin = coin.Coin()

    # Display the side of the coin that is facing up
    print("This side is up: ", my_coin.get_sideup())

    # Toss the coin
    print(" I am tossing the coin ten times: ")
    for count in range(10):
        my_coin.toss()
        print(count+1, my_coin.get_sideup())

# Call the main function
main()