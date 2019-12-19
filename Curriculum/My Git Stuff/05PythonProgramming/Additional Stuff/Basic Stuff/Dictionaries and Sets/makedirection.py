import pickle
hangman_dict = open('hangmandict.dat', 'wb')

dictr = {1 : "word", 2 : "ceiling", 3 : "superb", 
        4 : "python", 5 : "computer", 6 : "light"
    }

pickle.dump(dictr, hangman_dict)

hangman_dict.close()