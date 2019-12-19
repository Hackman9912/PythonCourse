
# Using Random Numbers

Dr. Kimura teaches an introductory statistics class, and has asked you to write a program that he can use in class to simulate the rolling of dice. The program should randomly generate two numbers in the range of 1 through 6 and display them. In your interview with Dr. Kimura, you learn that he would like to use the program to simulate several rolls of the dice, one after the other. You decide to write a loop that simulates one roll of the dice, and then asks the user whether another roll should be performed. As long as the user answers “y” for yes, the loop will repeat. Program below shows the pseudocode for the program, and Figure below shows the flowchart.

## Program 
```
 1  // Declare a variable to control the
 2  // loop iterations.
 3  Declare String again
 4
 5  Do
 6     // Roll the dice.
 7     Display "Rolling the dice..."
 8     Display "Their values are:"
 9     Display random(1, 6)
10     Display random(1, 6)
11
12     // Do this again?
13     Display "Want to roll them again? (y = yes)"
14     Input again
15  While again == "y" OR again == "Y"
```
```
Program Output (with Input Shown in Bold)
Rolling the dice...
Their values are:
2
6
Want to roll them again? (y = yes)
y [Enter]
Rolling the dice...
Their values are:
4
1
Want to roll them again? (y = yes)
y [Enter]
Rolling the dice...
Their values are:
3
3
Want to roll them again? (y = yes)
n [Enter]
```

![image](https://user-images.githubusercontent.com/47218880/67446701-132cfd00-f5d7-11e9-8da7-825339ef6b78.png)

