# This program passes a Coin object as an argument to a function
import coin

def main():
    # create a Coin object
    my_coin = coin.Coin()

    # This will display 'Heads'
    print('Here is the coin before the flip', my_coin.get_sideup())
    # Pass the object to the flip function
    print('Tossing the coin....')
    flip(my_coin)
    # Display the coin
    print('Here is the toss: ', my_coin.get_sideup())

# The flip function flips a coin

def flip(coin_obj):
    coin_obj.toss()

# Call main
main()