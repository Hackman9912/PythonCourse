
# Using Random Numbers to Represent Other Values

Dr. Kimura was so happy with the dice rolling simulator that you wrote for him, he has asked you to write one more program. He would like a program that he can use to simulate ten coin flips, one after the other. Each time the program simulates a coin flip, it should randomly display either “Heads” or “Tails.”

You decide that you can simulate the flipping of a coin by randomly generating a number in the range of 1 through 2. You will design a decision structure that displays “Heads” if the random number is 1, or “Tails” otherwise. Program below shows the pseudocode for the program, and Figure below shows the flowchart.

## Program 
```
 1  // Declare a counter variable.
 2  Declare Integer counter
 3
 4  // Constant for the number of flips.
 5  Constant Integer NUM_FLIPS = 10
 6
 7  For counter = 1 To NUM_FLIPS
 8     // Simulate the coin flip.
 9     If random(1, 2) == 1 Then
10        Display "Heads"
11     Else
12        Display "Tails"
13     End If
14  End For
```
```
Program Output
Tails
Tails
Heads
Tails
Heads
Heads
Heads
Tails
Heads
Tails
```
![image](https://user-images.githubusercontent.com/47218880/67446980-0eb51400-f5d8-11e9-9417-aa7ef4a250be.png)

