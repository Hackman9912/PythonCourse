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
import random
hangman_dict = {1 : "word", 2 : "apple", 3 : "superb", 
                4 : "python", 5 : "computer", 6 : "water bottle"
    }
y = ""
z = ""
turn = 1
complete = False
board = ""
incorrect = 0
correct = 0

def main():
    global hangman_dict, y, turn, complete, board, incorrect
    titlescreen()
    how_to_play()
    selection = random.randint(1, len(hangman_dict))
    print(selection)
    print(hangman_dict[selection])
    board = make_board(selection, hangman_dict)
    while complete == False:
        print_board(board)
        if board == hangman_dict[selection]:
            complete = True
            print("You win!")
        elif incorrect > 6:
            complete = True
            print("You lose!")
        else:
            guess = guessing()
            print("You guessed: ", guess)
            game(guess, hangman_dict, selection)
            print_board(board)



def titlescreen():
    print("  ######################################")
    print("  #                                    #")
    print("  #             Hang Man               #")
    print("  #                                    #")
    print("  ######################################")
def how_to_play():
    print("\n               How to play                 ")
    print(" \n The program will randomly select a word and you \n must guess the word letter by letter.")
    print("\n You are allowed to have 6 mistakes before you lose!\n \n")
def make_board(selected, dictionary):
    global y
    for x in dictionary[selected]:
        if x.isalpha() == True:
            y += x.replace(x, "_ ")
    return y
def guessing():
    selection = input(f"Enter your guess: ")
    if selection.isalpha() == True:
        print("good job")
        return selection
    else:
        print("Enter a single letter a to z")
        guessing()
def game(guess, dict, selection):
    global z, board, incorrect, correct
    print("guess in function", guess)
    if guess in dict[selection]:
        correct += 1
    else:
        incorrect += 1
    for x in dict[selection]:
        if x == guess:
            z += x + " "
        else:
            z += "_ "
    board = z
    print("board in function: \n", board)
def print_board(board):
    print("           Here is your board: \n           ", board, "\n")           




main()

