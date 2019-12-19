# Write a program that takes a string as user input then counts the number of words in 
# that sentence.

user_input=input("Input your text with spaces to separate words! ")

user_input.split(" ")

a = user_input.split(" ")
print(" Your sentence is", len(a), "words long and", len(user_input), "characters long! ")

letter_input=input(" Put a letter in to see how many show up in your sentence ")

print(user_input.count(letter_input))