'''
4. Unique Words
Write a program that opens a specified text file and then displays a list of 
all the unique words found in the file.
Hint: Store each word as an element of a set
'''
# initiate the set
word_list = set()

# open the file
with open('unique.txt', 'r') as f:
    # iterate through the file
    word_list = {word for word in line.split() for line in f}
        # split up each word
#        for word in line.split():
            # add the word to the set
#            word_list.add(word)
# display the set
print(word_list)
