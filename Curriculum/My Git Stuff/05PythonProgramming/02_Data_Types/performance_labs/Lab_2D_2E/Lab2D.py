# Write a program that reverses a user inputted string then outputs the new string, 
# in all uppercase letters.

user_input=input("Input your text! ")
user_input=user_input.upper()
print(user_input[::-1])