alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string_input = input("Enter a string: ")
shift_input = int(input("Enter a value to shift by: "))

input_length = len(string_input)

string_output = ""

for i in range(input_length):
    character = string_input[i]
    location_of_character = alphabets.find(character)
    new_location = location_of_character + shift_input;
    if new_location >= 26:
        new_location -= 26
    string_output = string_output + alphabets[new_location]

print("Encrypted text: ", string_output)







# print(string_input)

# print(input_length)
