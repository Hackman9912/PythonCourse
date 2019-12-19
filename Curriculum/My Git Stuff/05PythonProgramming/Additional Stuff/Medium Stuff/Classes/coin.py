import random

# The Coin class simulates a coin that can be flipped

class Coin:

    # the __init__ method initilizes the sideup data attribute with 'Heads'.
    def __init__(self):
        self.__sideup = 'Heads'
    # The toss method generates a random number in the range of 0 through 1. If the number is 0, then sideup is set to 'Heads'
    # Otherwise, sidup is set to 'Tails'.
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    
    # The get_sideup method returns the Value referenced by sidup
    def get_sideup(self):
        return self.__sideup

# # The main funciton
# def main():
#     # Create an object from the Coin Class
#     my_coin = Coin()
#     print(type(my_coin))
   
#    # Display the side of the coin that is showing
#     print("This side is up: ", my_coin.get_sideup())

#     print("I am tossing the coin..")
#     for count in range(10):
#         my_coin.toss()
#         print(my_coin.get_sideup())

#     print("This side is now up: ", my_coin.get_sideup())



# main()