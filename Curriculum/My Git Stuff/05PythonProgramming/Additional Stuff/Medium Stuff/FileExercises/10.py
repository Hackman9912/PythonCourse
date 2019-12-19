#  10. Golf Scores
# The Springfork Amateur Golf Club has a tournament every weekend. The club presidenthas asked you to write two programs:
# 1. A program that will read each player’s name and golf score as keyboard input, and then save these as records in a file 
# named golf.txt. (Each record will have a field for theplayer’s name and a field for the player’s score.)
# 2. A program that reads the records from the golf.txt file and displays them.
player_input = str(input("Enter 1 to enter scores or enter 2 to view the score sheet: "))

if player_input == "1":

    player = ["Name"]
    score = ["score"]

    number = int(input("Enter the number of players you need to enter a golf score for: "))

    num_file = open('golf.txt', 'a')
    for i in range(1, number + 1):
        first_last = str(input("Enter the first and last name of the golfer: "))

        total_score = int(input("Enter the score for the player entered: "))

        player.append(first_last)
        score.append(total_score)
        players = str(player[i])
        scores = str(score[i])


        # Get the amount of sales for each day and write it to the file

        write = str(print("The player", player, "scored", score, "\n"))
        # write the sales amount to the file
        num_file.write("The player", player, "scored", score, "\n")

    # Close the file
    num_file.close()

elif player_input == "2":

    # Define counter
    count = 0

    # Open the file
    infile = open('golf.txt', 'r')

    # Set readline
    line = infile.readline()

    # Display first 5 lines
    while line != '':
        # Convert line to a float
        amount = line
        # Increment count
        count += 1
        # Format and display data
        print(amount)
        # Read the next line
        line = infile.readline()
    infile.close()
else:
    print("Enter a valid selection next time.")

