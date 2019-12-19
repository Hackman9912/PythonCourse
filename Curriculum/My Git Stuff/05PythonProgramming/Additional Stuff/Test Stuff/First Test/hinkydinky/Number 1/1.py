"""
Python Basics Performance Exam

    This exam is open note, open book, and open internet. Feel free to use any resources
    you can (other than someone else) to solve the following problems. Direct collaboration with another
    individual will result in immediate failure and consequences to follow. If you are unsure about 
    whether or not you can use a resource please ask me. If you are unsure about any of the prompts I can clarify. 

    Comments are necessary. 

    Each problem will weigh the same towards the final grade. 4 Problems at 25% each. 

    Please send each problem as a .py file separately. Please direct message them to me (Daniel Curran) 
    through slack. If there are supporting files for a problem then please send them with the .py file 
    as a zipped folder. 

    You will have 3 hours to complete this exam. If you complete this portion early and I have verified
    I have everything needed to grade your exam then you will be released.

    Happy Thanksgiving. 

1. 
    (Remove text) Write a program that removes all the occurrences of a specified
    string from a text file named pointsOfAuthority.txt. Your program should prompt the user to enter 
    a filename and a string to be removed.

    Points Of Authority - Linkin Park

        Forfeit the game
        Before somebody else
        Takes you out of the frame
        And puts your name to shame
        Cover up your face
        You can't run the race
        The pace is too fast
        You just won't last

        You love the way I look at you
        While taking pleasure in the awful things you put me through
        You take away if I give in
        My life, my pride is broken

        You like to think you're never wrong
        (You live what you've learned)
        You have to act like you're someone
        (You live what you've learned)
        You want someone to hurt like you
        (You live what you've learned)
        You want to share what you've been through
        (You live what you've learned)

        You love the things I say I'll do
        The way I'll hurt myself again just to get back at you
        You take away when I give in
        My life, my pride is broken

        You like to think you're never wrong
        (You live what you've learned)
        You have to act like you're someone
        (You live what you've learned)
        You want someone to hurt like you
        (You live what you've learned)
        You want to share what you've been through
        (You live what you've learned)

        Forfeit the game
        Before somebody else
        Takes you out of the frame
        And puts your name to shame
        Cover up your face
        You can't run the race
        The pace is too fast
        You just won't last

        Forfeit the game
        Before somebody else
        Takes you out of the frame
        And puts your name to shame
        Cover up your face
        You can't run the race
        The pace is too fast
        You just won't last

        You like to think you're never wrong
        (You live what you've learned)
        You have to act like you're someone
        (You live what you've learned)
        You want someone to hurt like you
        (You live what you've learned)
        You want to share what you've been through
        (You live what you've learned)


"""
# Define the main program

def main():

    text = []
    # open the file as f
    with open("pointsOfAuthority.txt", 'r') as f:
        # read each file in the line
        for line in f:
            # add the line to the list splitting it by word
            text.extend(line.split())
            # add a new line return at each line
            text.append("\n")
    # Get the word the user would like to have removed
    print("Enter the word you would like to have removed from the song: ")
    remv = input()
    # Get the name of the file the user wants to make
    print("Enter the name of the file you would like to save your new song to:")
    userfile = input() + ".txt"
    # make a list with the indexes of the offending word
    index = [i for i, x in enumerate(text) if x.lower() == remv.lower()]
    count = 0
    # iterate through the list of the indexes
    for i in index:
        # remove those words from the list of the song stuff
        print(text[i - count])
        count += 1
        del text[i - count]
    # open the outfile
    outfile = open(userfile, 'w')
    # write the list to the file, joining it so that it displays correctly
    outfile.write(" ".join(text))




# Call the main function
main()
