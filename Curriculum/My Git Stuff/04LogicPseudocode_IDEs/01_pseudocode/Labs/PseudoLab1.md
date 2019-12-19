|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---

## PseudoLab1

**Draw Flowchart for pseudocode**

* Draw a flowchart or write pseudocode to represent the logic of a program that allows the user to enter a value for one edge of a cube. The program calculates the surface area of one side of the cube, the surface area of the cube, and its volume.  The progrma outputs all the results.

* Draw a flowchart or write pseudocode to represent the logic of a program that allows the user to enter two values.  The program outputs the sum and the differences between two values

* Draw a flowchart or write pseudocode to represent the logic of a program that allows the user to enter an hourly pay rate and hours worked.  The program outputs the user's gross pay.

* MOdify the program that computes gross pay to allow the user to enter the withholding tax rate.  The program outputs the net pay after taxes have been withheld.

* Research current rates of monetary exchange.  Draw a flowchart or write pseudocode to represent the logic of a program that allows the user to enter a number of dollasrs and convert it to euros and Japanese yen.

A mobile phone app allows a user to press a button that starts a timer that counts seconds.  When the user presses the button again, the timer stops.  Draw a flowchart or write pseudocode that accepts the elapsed time in seconds and displays the value in munutes and seconds.  For example, if the elapsed time was 130 seconds, the output would be 2 minutes and 10 seconds.

---

## Debugging Labs

**Find the errors**

* If the programmer translates the following pseudocode to an actual programming language, a syntax errror is likely to occur.  Can you find the error?

```
Declare String firstPrize
// 1stPrize should be firstPrize
Display "Enter the award for first prize."
Input firstPrize
Display "The first prize winner will receive $", firstPrize
```

---

* The following code will not display the results expected by the programmer.  Can you find the error?

```
Declare Real lowest, highest, average

Display "Enter the lowest score."
Input lowest

Display "Enter the highest score."
Input highest

Set average = (lowest + highest) / 2
// should be (lowest + highest) / 2
Display "The average is ", average, "."

```

---

* Find the error in the following pseudocode

```
Declare Integer length
Display "Enter the length of the room."
Input length 
// Declare Integer length needs to be at the top
```

---

* Find the error in the following pseudocode

```
Declare Integer value1, value2, value3, sum

// Set sum = value1 + value2 + value3 should follow the inputs
Display "Enter the first value."
Input value1

Display "Enter the second value."
Input value2

Display "Enter the third value."
Input value3

Set sum = value1 + value2 + value3

Display "The sum of numbers is ", sum

```

---

* Find the error in the following pseudocode

```
Declare Real pi
Set pi = 3.14159265
// pi should come before the number
Display "The value of pi is ", pi
// . should be a ,
```

---

* Find the error in the following pseudocode.

```
Declare Real gravity = 9.81
// Should be Declare and not Constant and not all caps gravity. All CAPS usually are constants
Display "Rates of acceleration of an objet in free fall:"
Display "Earth: ", gravity, " meters per second every second."
Set gravity = 1.63
Display "Moon: ", gravity, " meters per second every second."
```

---

|[Next Topic](/01_pseudocode/02_pseudocode.md)|
|---|
