'''
5. Word Frequency
Write a program that reads the contents of a text file. The program should create a 
dictionary in which the keys are the individual words found in the file and the values 
are the number of times each word appears. For example, if the word “the” appears 
128 times, the dictionary would contain an element with 'the' as the key and 128 as 
the value. The program should either display the frequency of each word or create a 
second file containing a list of each word and its frequency
'''

word_frequency = {"word" : "frequency"}

# open the file
with open('frequency.txt', 'r') as f:
    # iterate through the file
    for line in f:
        # split up each word
        for word in line.split():
            # if the word is not in the dictionary then add it and set its value to 1
            if word not in word_frequency:
                word_frequency[word] = 1
            # If the word is in the dictionary then add to its value by 1
            else:
                word_frequency[word] += 1
# print the dictionary
print(word_frequency)