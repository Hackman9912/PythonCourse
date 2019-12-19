"""

(Game: play a tic-tac-toe game) In a game of tic-tac-toe, two players take turns
marking an available cell in a grid with their respective tokens (either X or
O). When one player has placed three tokens in a horizontal, vertical, or diagonal
row on the grid, the game is over and that player has won. A draw (no winner)
occurs when all the cells in the grid have been filled with tokens and neither player
has achieved a win. Create a program for playing tic-tac-toe.
The program prompts two players to alternately enter an X token and an O
token. Whenever a token is entered, the program redisplays the board on the
console and determines the status of the game (win, draw, or continue).

"""

import sys

def main():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    displayBoard(board)

    while True:
        # Prompt the first player
        makeAMove(board, 'X')
      
        displayBoard(board)

        # Did first player win?
        if isWon('X', board):
            print("X player won")
            sys.exit()
        elif isDraw(board):
            print("No winner")
            sys.exit()

        # Prompt the second player
        makeAMove(board, 'O')
        displayBoard(board)

        # Did 2nd player win?
        if isWon('O', board):
            print("O player won")
            sys.exit()
        elif isDraw(board):
            print("No winner")
            sys.exit()

# Function that takes a player input for row and column and places it on the board
def makeAMove(board, player):
    done = False
    
    while not done:
        row = eval(input("Enter a row for player " + player + ": "))
        column = eval(input("Enter a column for player " + player + ": "))
    
        if board[row][column] == ' ': # an empty cell
            board[row][column] = player
            done = True
        else:
            print("This cell is already occupied. Try a different cell")

# This function shows the game board 
def displayBoard(board):
    print("\n-------------")

    for i in range(3):
        print("| ", end = "")
        for j in range(3):
            print(board[i][j] + " | " if board[i][j] != '\u0000' else "  | ", end = "")
        print("\n-------------")

# This function checks to see if someone has won yet
def isWon(ch, board):
    # Check rows
    for i in range(3):
        if ch == board[i][0] and ch == board[i][1] and ch == board[i][2]: 
            return True

    # Check columns
    for j in range(3):
        if ch == board[0][j] and ch == board[1][j] and ch == board[2][j]: 
            return True

    # Check major diagonal
    if ch == board[0][0] and ch == board[1][1] and ch == board[2][2]: 
        return True

    # Check sub diagonal
    if ch == board[0][2] and ch == board[1][1] and ch == board[2][0]: 
        return True

    return False

# This function checks if any spots are left empty, if not then the board is full
def isDraw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ': 
                return False

    return True # All cells are now occupied

main()
