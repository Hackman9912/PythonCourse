"""
    Task:
        Your task is to implement the Hangman game in Python.

    Program Specifications:
        1) Output a brief description of the game of hangman and how to play
        2) Ask the user to enter the word or phrase that will be guessed (have a friend enter the phrase 
            for you if you want to be surprised)
        3) Output the appropriate number of dashes and spaces to represent the phrase (make sure it’s clear 
            how many letters are in each word and how many words there are)
        4) Continuously read guesses of a letter from the user and fill in the corresponding blanks if the 
            letter is in the word, otherwise report that the user has made an incorrect guess.
        5) Each turn you will display the phrase as dashes but with any already guessed letters filled in, 
            as well as which letters have been incorrectly guessed so far and how many guesses the user has remaining.
        6) Your program should allow the user to make a total of k=6 guesses.

    Assignment Notes:
        If the letter has already been guessed, output a message to the player and ask for input again.
        If the guess entered is not an alphabetic letter, output a message and ask for input again.

        If the letter is present in the word to be guessed, fill in the blanks appropriately with this particular letter. 
        If the complete name has been guessed, the game is over  - player wins the game.  Output a message telling the 
        player they have won and quit the game.

        If the letter/digit is not present in the word to be guessed, give a message to the player indicating that the 
        guess is incorrect and remaining number of chances is one less. If remaining number of chances is 0 (zero), 
        the game is over  - player loses the game. Output a message that they have lost and what the correct word was.  Quit the game.

    Bonus:
        You can do one or both of the following:

        1) Using a file:
        Instead of asking for user input for the word, make a word bank in a file named hangman_words.txt. 
        Read in the contents of the file and choose a word at random.

        2) Forever alone option:
        You enter the word (or it is randomly chosen from the word bank) and have the computer try to guess the letters.

        3) Add some more functionality: 
            - Persist user profiles with scores
            - Prompt for which user is playing
            - Ask if the user wants to play a set of games
            - Build a leader board
            
        Have fun, get creative, and demonstrate what you've come up with.
"""
# import the important things
import sys
import time
import random
import pickle
# for making a smart computer
# from nltk.corpus import words
# make the dictionaries
hangman_dict = {}
# establish incorrect guess list
incorrect_guess = []
# establish complete
complete = False
# establish the answer board
answer = []
# establish the game board
board = []
# define main
def main():
    # establish my global variables
    global hangman_dict, complete, board, incorrect_guess
    # call the title screen
    titlescreen()
    # call the rules
    how_to_play()
    # load the dictionary from the file
    hangman_dict = pickle.load(open('hangmandict.dat', 'rb'))
    # call the function to allow the user to add a word or phrase to the list to possibly be able to use it this game
    addword()
    # select the word
    selection = random.randint(1, len(hangman_dict))
    # make the selection a unique variable for reasons
    word = hangman_dict[selection]
    # make the board from the word
    make_board(selection, hangman_dict)
    # make the while the game is not done then play it
    while complete == False:
        # if the answer board and the game board are the same then you won
        if board == answer:
            complete = True
            print("You won!")
            print("The answer was ", word)
        # if you get 6 incorrect guesses you lose
        elif len(incorrect_guess) > 5:
            print("You lost!")
            print("The answer was ", word)
            exit()
        # play the game
        else:
            # show the board
            print("Here is the board \n", "".join(board))
            # call the guessing function
            guess = guessing()
            # check to see if the guess is right
            right_wrong(guess)
    # When a complete statement is met the the game is done
    print("Game Over")
# define the wonderful print slow
def print_slow(txt):
    # for every letter in whatever text
    for letter in txt:
        # makes it print like typing
        sys.stdout.write(letter)
        # make it print right
        sys.stdout.flush()
        # give the user some time to read
        time.sleep(0.0003)
# define the title screen to print beautifully
def titlescreen():
    print_slow("  ######################################")
    print_slow("\n  #                                    #")
    print_slow("\n  #             Hang Man               #")
    print_slow("\n  #                                    #")
    print_slow("\n  ######################################")
# define the rules to print beautifully
def how_to_play():
    print_slow("\n \n             How to play                 ")
    print_slow(" \n The program will randomly select a word and \n you must guess the word letter by letter. You")
    print_slow("\n are allowed to have 6 mistakes before you lose!\n \n")
# define the function for the user to add a word
def addword():
    # call glbal
    global hangman_dict
    # set the flag
    x = 2
    # tell the user to make a choice
    print("To add a word or phrase to the word list press 1: ")
    x = int(input("To continue on to the game press 2: "))
    # if the user chooses 1 then let them add a word
    if x == 1:
        print("Enter the word or phrase to add to the hangman game")
        # sets variable y to be the number of actual entries
        y = len(hangman_dict) + 1
        # tell the user how many options
        print(f"There are {y - 1:} words in the dictionary now!")
        # get the word to enter
        word = input("Enter your word or phrase here: ")
        print(f"\n You entered:{word:} \n \n")
        # add the word to the dictionary
        hangman_dict[y] = word
        # write the dictionary to the file
        pickle.dump(hangman_dict, open('hangmandict.dat', 'wb'))
        # exit the loop
        x == 2
# defining the making of the board
def make_board(selected, dictionary):
    # define our global variables
    global board, answer
    # for every letter of the selected word
    for x in dictionary[selected]:
        # if the selection is a letter 
        answer.append(x.lower())
    # figure out the length of the list
    length = len(answer)
    # for the length of the list make underscores
    for i in range(0, length):
        board.append('_ ')
    # if non alphabetic characters exist then just auto fill them in
    for x in answer:
        if x.isalpha() != True:
            index = dupes(x)
            for i in index:
                board[i] = x
    # talk to the user
    print_slow("Get ready to go: \n")
    time.sleep(1)
    cls()
# define the function to print the man hanging as you lose
def hungman():
    global incorrect_guess
    lengthI = len(incorrect_guess)
    if lengthI == 1:
        cls()
        print("        _________________ ")
        print("       / ________________|")
        print("      / /         |       ")
        print("     | |          |")
        print("     | |")
        print("     | |")
        print("     | |")
        print("     | |")
        print("     | |")
        print("     | |")
        print("     | |")
        print("     | |_________________________")
        print("     | |                      | |")
        print("     | |                      | |")
        print("####################################################################")
        
    elif lengthI == 2:
        cls()
        print("        _________________ ")
        print("       / ________________|")
        print("      / /         |       ")
        print("     | |          |___   ")
        print("     | |         *|'.'|*")
        print("     | |           \\_/")
        print("     | |")
        print("     | |")
        print("     | |")
        print("     | |")
        print("     | |")
        print("     | |_________________________")
        print("     | |                      | |")
        print("     | |                      | |")
        print("####################################################################")

    elif lengthI == 3:
        cls()
        print("        _________________ ")
        print("       / ________________|")
        print("      / /         |       ")
        print("     | |          |___   ")
        print("     | |         *|'.'|*")
        print("     | |           \\_/")
        print("     | |           | |")
        print("     | |           |_|")
        print("     | |")
        print("     | |")
        print("     | |")
        print("     | |_________________________")
        print("     | |                      | |")
        print("     | |                      | |")
        print("####################################################################")
    elif lengthI == 4:
        cls()
        print("        _________________ ")
        print("       / ________________|")
        print("      / /         |       ")
        print("     | |          |___   ")
        print("     | |         *|'.'|*")
        print("     | |           \\_/")
        print("     | |      +----| |----+")
        print("     | |           |_|")
        print("     | |")
        print("     | |")
        print("     | |")
        print("     | |_________________________")
        print("     | |                      | |")
        print("     | |                      | |")
        print("####################################################################")
    elif lengthI == 5:
        cls()
        print("        _________________ ")
        print("       / ________________|")
        print("      / /         |       ")
        print("     | |          |___   ")
        print("     | |         *|'.'|*")
        print("     | |           \\_/")
        print("     | |      +----| |----+")
        print("     | |           |_|")
        print("     | |           | |")
        print("     | |           | |")
        print("     | |          _| |_")
        print("     | |_________________________")
        print("     | |                      | |")
        print("     | |                      | |")
        print("####################################################################")
    elif lengthI == 6:
        cls()
        print("        _________________ ")
        print("       / ________________|")
        print("      / /         |       ")
        print("     | |          |___   ")
        print("     | |         *|x.x|*")
        print("     | |           \\_/")
        print("     | |      +----| |----+")
        print("     | |           |_|")
        print("     | |           | |")
        print("     | |           | |")
        print("     | |          _| |_")
        print("     | |_________________________")
        print("     | |                      | |")
        print("     | |                      | |")
        print("####################################################################")
# a function to print the board
def print_board(board):
    print("           Here is your board: \n           ", "".join(board), "\n")           
# define the funtion to make the guess
def guessing():
    global board, incorrect_guess
    # make their answer the guess
    selected = input(f"\n \nEnter your guess: ")
    # if they select a letter then return it
    if selected.isalpha() == True:
        return selected
    # if they do not select a letter then make them select one
    else:
        print("Enter a single letter a to z")
        guessing()
# define the function to see if the guess is accurate
def right_wrong(guess):
    # define global variables
    global hangman_dict, incorrect_guess, answer, board
    # if the user has already tried a guess then tell them and don't count it. 
    if guess in board or guess in incorrect_guess:
        print("You already tried that, try again!")
    # see if the guess is in the answer
    elif guess in answer:
        # call the dupes function
        indexing = dupes(guess)
        # set the index to be whatever index was applicable
        for i in indexing:
            # add that to the board
            # board[i] = answer[i]
            board[i] = guess
    # add it to the incorrect guess list and tell user how many incorrect guesses they have. 
    else:
        incorrect_guess.append(guess)
        print(f"You have {len(incorrect_guess):} incorrect guesses. You lose at 6. ")
        # call the hungman function
        hungman()
# define the function to handle duplicates
def dupes(item):
    # call globals
    global answer, board
    # get the index of all the iterations of duplicate items in list
    return [i for i, x in enumerate(answer) if x.lower() == item]
def cls():
    print("\n" * 100)
# call main
main()