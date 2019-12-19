# Input Validation Exercise Workbench

Design an algorithm that prompts the user to enter a positive nonzero number and validates the input.


```
Display "Enter a positive non-zero number"
Input value

If value > 0 Then

   Return

Else

   Display "You suck, try again"
   Input value

End If

```
Design an algorithm that prompts the user to enter a number in the range of 1 through 100 and validates the input.

```
Display "Input a number between 1 and 0"
Input value

While value < 1 OR value > 100
   Display "Please put a number in between 1 and 100"
   Input value

End While


```

Design an algorithm that prompts the user to enter “yes” or “no” and validates the input. (Use a case-insensitive comparison.)


```
Display "Enter 'yes' or enter 'no'
Input answer

While toLower(answer) != "yes" AND toLower(answer) != "no"
   Display "Please answer yes or no."
   Input answer

End While
```
Design an algorithm that prompts the user to enter a number that is greater than 99 and validates the input.
```
Display "Please enter a number greater than 99"
Input answer

While answer <= 99
   Display "Please enter a number greater than 99"
   Input answer

End While
```
Design an algorithm that prompts the user to enter a secret word. The secret word should be at least 8 characters long. Validate the input.

```
Display "Please enter a secret word that is at least 8 characters long"
Input word

While length(word) < 8
   Display "Enter a secret word that is at least 8 characters long!"
   Input word
```

# Debugging Exercises

Why does the following pseudocode not perform as indicated in the comments?
```
// This program asks the user to enter a value
// between 1 and 10 and validates the input.
Declare Integer value

// Get a value from the user.
Display "Enter a value between 1 and 10."
Input value

// Make sure the value is between 1 and 10.
> While value < 1 OR value > 10
   Display "ERROR: The value must be between 1 and 10."
   Display "Enter a value between 1 and 10."
   Input value
End While
```
Why does the following pseudocode not perform as indicated in the comments?
```
// This program gets a dollar amount from the user
// and validates the input.
Declare Real amount

// Get the amount from the user.
Display "Enter a dollar amount"
Input amount

// Make sure the amount is not less than zero. If it is,
// get a new amount from the user.
While amount < 0
   Display "ERROR: The dollar amount cannot be less than 0."
   Display "Enter a dollar amount."
  > Input amount
End While
```
The following pseudocode works, but it performs a case-sensitive validation of the user’s input. How could the algorithm be improved so the user does not have to pay attention to capitalization when entering a name?
```
// This program asks the user to enter a string
// and validates the input.
Declare String choice

// Get the user's response.
Display "Cast your vote for Chess Team Captain."
Display "Would you like to nominate Lisa or Tim?"
Input choice

// Validate the input.
While choice != "Lisa" AND choice != "Tim"
   Display "Please enter Lisa or Tim."
   Display "Cast your vote for Chess Team Captain."
   Display "Would you like to nominate Lisa or Tim?"
   Input response
End While

>Should use toLower
```
