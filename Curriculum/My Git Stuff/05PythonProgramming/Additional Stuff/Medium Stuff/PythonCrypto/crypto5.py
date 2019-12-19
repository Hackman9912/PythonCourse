alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string_input = input("Enter a string: ")

input_length = len(string_input)

string_output = ""

for i in range(input_length):
    character = string_input[i]
    location_of_character = alphabets.find(character)
    print(location_of_character)








# print(string_input)

# print(input_length)
