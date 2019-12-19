# Select 5 Programming projects from the list

## Rectangle Area

The area of a rectangle is calculated according to the following formula:

![image](https://user-images.githubusercontent.com/47218880/67446156-3e165180-f5d5-11e9-8673-1dab25034bff.png)

Design a function that accepts a rectangle’s width and length as arguments and returns the rectangle’s area. Use the function in a program that prompts the user to enter the rectangle’s width and length, and then displays the rectangle’s area.

```
Module main()

  Declare real width, length, result

  // Get the length and width
  Display "To calculate the area of a rectangle, enter length"
  Display "and width when prompted."
  Display "Enter the length:"
  Input length
  Display "Enter the width:"
  Input width

  // Get the area
  Set result = area(length, width)

  // Display the result
  Display "Here is your result.", result

End Module

Function Real area(width length)

    Declare real area

    Set area = width * length
    Return area

End Function
```

## Feet to Inches

One foot equals 12 inches. Design a function named feetToInches that accepts a number of feet as an argument, and returns the number of inches in that many feet. Use the function in a program that prompts the user to enter a number of feet and then displays the number of inches in that many feet.


```
Module main()

  Declare real feet, inches

  //Get the feet
  Display "To get the feet converted to inches, enter the feet",
  Input feet

  //Convert feet to inches

  Set inches = feetInches(feet)

  Display "Here are your results in inches", inches, "in", feet, "feet"

End Module

Function Real feetInches(feet)

  Declare real result
  Set Constant IN_FT = 12

  Set result = feet / IN_FT
  Return result

End Function

```

## Math Quiz

Design a program that gives simple math quizzes. The program should display two random numbers that are to be added, such as:
```
  247
+ 129
```
The program should allow the student to enter the answer. If the answer is correct, a message of congratulations should be displayed. If the answer is incorrect, a message showing the correct answer should be displayed.

```

Module main()

  Declare integer num1, num2, answ, userAnsw

  Set num1 = randNum()
  Set num2 = randNum()
  Set answ = sum(num1, num2)

  Display "Answer the addition problem shown"
  Display num1, "+", num2, "equals"
  Input userAnsw

  If answ != userAnsw Then

    Display "Congratulations you rock!"

  Else

    Display "Sorry that is not correct", answ, "Is the answer."

  End If

End Module

Function Integer randNum()

  Declare integer number

  Set number = random(1, 9999)

  Return number

End Function

Function Integer sum(num1, num2)

  Declare integer result

  Set result = num1 + num2

  Return result

End Function

```

## Maximum of Two Values

Design a function named max that accepts two integer values as arguments and returns the value that is the greater of the two. For example, if 7 and 12 are passed as arguments to the function, the function should return 12. Use the function in a program that prompts the user to enter two integer values. The program should display the value that is the greater of the two.

```
Module main()

  Declare integer num1, num2, great


  Display "Please input two whole numbers and the larger will be displayed"

  Display "Input the first"
  Input num1

  Display "Input the second"
  Input num2

  If num1 == num2 Then
    Display "That is cheating, they are equal!"

  Else
    Set great = greater(num1, num2)
    Display "This is the greater number", great

  End If

End Module

Function Integer greater(num1, num2)

  Declare integer result

  If num1 > num2 Then
    Set result = num1

  Else
    Set result = num2

  End IF

  Return result

End Function
```

## Falling Distance

When an object is falling because of gravity, the following formula can be used to determine the distance the object falls in a specific time period:

![image](https://user-images.githubusercontent.com/47218880/67446204-67cf7880-f5d5-11e9-9375-bbde7f1473b5.png)

The variables in the formula are as follows: d is the distance in meters, g is 9.8, and t is the amount of time, in seconds, that the object has been falling.

Design a function named fallingDistance that accepts an object’s falling time (in seconds) as an argument. The function should return the distance, in meters, that the object has fallen during that time interval. Design a program that calls the function in a loop that passes the values 1 through 10 as arguments and displays the return value.

## Kinetic Energy

In physics, an object that is in motion is said to have kinetic energy. The following formula can be used to determine a moving object’s kinetic energy:

![image](https://user-images.githubusercontent.com/47218880/67446241-8fbedc00-f5d5-11e9-94c6-460160036f3f.png)

The variables in the formula are as follows: KE is the kinetic energy, m is the ­object’s mass in kilograms, and v is the object’s velocity, in meters per second.

Design a function named kineticEnergy that accepts an object’s mass (in ­kilograms) and velocity (in meters per second) as arguments. The function should return the amount of kinetic energy that the object has. Design a program that asks the user to enter values for mass and velocity, and then calls the kineticEnergy function to get the object’s kinetic energy.

## Odd/Even Counter

In this chapter you saw an example of how to design an algorithm that determines whether a number is even or odd. Design a program that generates 100 random numbers, and keeps a count of how many of those random numbers are even and how many are odd.

## Guess the Number

Design a number guessing game program. The program should generate a random number and then ask the user to guess the number. Each time the user enters his or her guess, the program should indicate whether it was too high or too low. The game is over when the user correctly guesses the number. When the game ends, the program should display the number of guesses that the user made.

## Prime Numbers

A prime number is a number that is only evenly divisible by itself and 1. For example, the number 5 is prime because it can only be evenly divided by 1 and 5. The number 6, however, is not prime because it can be divided evenly by 1, 2, 3, and 6.

Design a Boolean function named isPrime, which takes an integer as an argument and returns True if the argument is a prime number, or False otherwise. Use the function in a program that prompts the user to enter a number and then displays a message indicating whether the number is prime.

 ### TIP:
Recall that the MOD operator divides one number by another and returns the remainder of the division. In an expression such as num1 MOD num2, the MOD operator will return 0 if num1 is evenly divisible by num2.

## Prime Number List

This exercise assumes you have already designed the isPrime function in Programming Exercise 10. Design another program that displays all of the prime numbers from 1 through 100. The program should have a loop that calls the isPrime function.

## Rock, Paper, Scissors Game

Design a program that lets the user play the game of Rock, Paper, Scissors against the computer. The program should work as follows:
```
When the program begins, a random number in the range of 1 through 3 is generated. If the number is 1, then the computer has chosen rock. If the number is 2, then the computer has chosen paper. If the number is 3, then the computer has chosen scissors. (Don’t display the computer’s choice yet.)

The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.

The computer’s choice is displayed.

The program should display a message indicating whether the user or the computer was the winner. A winner is selected according to the following rules:

If one player chooses rock and the other player chooses scissors, then rock wins. (The rock smashes the scissors.)

If one player chooses scissors and the other player chooses paper, then scissors wins. (Scissors cut paper.)

If one player chooses paper and the other player chooses rock, then paper wins. (Paper wraps rock.)

If both players make the same choice, the game must be played again to determine the winner.
```

## Slot Machine Simulation

A slot machine is a gambling device that the user inserts money into and then pulls a lever (or presses a button). The slot machine then displays a set of random images. If two or more of the images match, the user wins an amount of money, which the slot machine dispenses back to the user.

Design a program that simulates a slot machine. When the program runs, it should do the following:
```
Ask the user to enter the amount of money he or she wants to insert into the slot machine.

Instead of displaying images, the program will randomly select a word from the following list:

Cherries, Oranges, Plums, Bells, Melons, Bars

The program will select and display a word from this list three times.

If none of the randomly selected words match, the program will inform the user that he or she has won $0. If two of the words match, the program will inform the user that he or she has won two times the amount entered. If three of the words match, the program will inform the user that he or she has won three times the amount entered.

The program will ask whether the user wants to play again. If so, these steps are repeated. If not, the program displays the total amount of money entered into the slot machine and the total amount won.
```
## ESP Game

Design a program that tests your ESP, or extrasensory perception. The program will randomly pick a color, and you will be asked to predict the program’s selection before it is revealed. Design the program to randomly select one of the following words:
```
Red, Green, Blue, Orange, Yellow
```
To select a word, the program can generate a random number. For example, if the number is 0, the selected word is Red, if the number is 1, the selected word is Green, and so forth.

Next, the program should ask the user to enter the color that the computer has selected. After the user has entered his or her guess, the program should display the name of the randomly selected color. The program should repeat this 10 times and then display the number of times the user correctly guessed the selected color.


```
Module main()

  Declare integer red, green, blue, orange, yellow, input, choice, count, correct

  Set correct = 0
  Set red = 1
  Set green = 2
  Set blue = 3
  Set orange = 4
  Set yellow = 5
  Constant integer MAX_VAL = 10 

  For count = 1 to MAX_VAL
    Set choice = random (1, 5)

    Display "Enter the number to select the color you think the computer chose"
    Display " Red (1), Green(2), Blue(3), Orange (4), Yellow (5)
    Input input

    If choice == input then
      Set correct = correct + 1

    End If

  End For

  If correct > 5 Then
    Display "You might have ESP, you got", correct, "out of 10 right!"

  Else

    Display "You probably do not have ESP, you only got", correct, "out of 10."

  End If

End Module
```