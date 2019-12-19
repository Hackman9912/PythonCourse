# Write a program that prompts the user to enter a number within the range of 1 through 10.
# The program should display the Roman numeral version of that number. If the number is
# outside the range of 1 through 10, the program should display an error message.

numberdict = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X"
}

number = int(input("Enter a number from 1 to 10: "))

if number < 1 or number > 10:
    print("Put a number in from 1 to 10")
else:
    x = numberdict.get(number)
    print("The roman numeral you want is: ", x)


