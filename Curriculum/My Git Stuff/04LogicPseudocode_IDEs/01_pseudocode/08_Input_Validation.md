# Designing an Input Validation Loop

In previous sections you saw a program that your friend Samantha can use to calculate the retail price of an item in her import business. Samantha has encountered a problem when using the program, however. Some of the items that she sells have a wholesale cost of 50 cents, which she enters into the program as 0.50. Because the 0 key is next to the key for the negative sign, she sometimes accidentally enters a negative number. She has asked you to revise the program so it will not allow a negative number to be entered for the wholesale cost.

You decide to add an input validation loop to the showRetail module that rejects any negative numbers that are entered into the wholesale variable. Program Below shows the new pseudocode, with the new input validation code shown in lines 28 through 33.

Figure Below shows a new flowchart for the showRetail module.

## Program
```
 1  Module main()
 2     // Local variable
 3     Declare String doAnother
 4     
 5     Do
 6        // Calculate and display a retail price.
 7        Call showRetail()
 8        
 9        // Do this again?
10        Display "Do you have another item? (Enter y for yes.)"
11        Input doAnother
12     While doAnother == "y" OR doAnother == "Y"
13  End Module
14
15  // The showRetail module gets an item's wholesale cost
16  // from the user and displays its retail price.
17  Module showRetail()
18     // Local variables
19     Declare Real wholesale, retail
20
21     // Constant for the markup percentage
22     Constant Real MARKUP = 2.50
23
24     // Get the wholesale cost.
25     Display "Enter an item's wholesale cost."
26     Input wholesale
27    
28     // Validate the wholesale cost.
29     While wholesale < 0
30        Display "The cost cannot be negative. Please"
31        Display "enter the correct wholesale cost."
32        Input wholesale
33     End While
34   
35     // Calculate the retail price.
36     Set retail = wholesale * MARKUP
37   
38     // Display the retail price.
39     Display "The retail price is $", retail
40  End Module
```
```
Program Output (with Input Shown in Bold)
Enter an item's wholesale cost.
−0.50 [Enter]
The cost cannot be negative. Please
enter the correct wholesale cost.
0.50 [Enter]
The retail price is $1.25
Do you have another item? (Enter y for yes.)
n [Enter]
```
![image](https://user-images.githubusercontent.com/47218880/67502018-d995d980-f64a-11e9-87f0-9dc7dc5d7005.png)

## Using a Posttest Loop to Validate Input
```
Do
   Display "Enter a test score."
   Input score
While score < 0 OR score > 100
```
```
// Get the model number.
Display "Enter the model number."
Input model

While model != 100 AND model != 200 AND model != 300
   Display "The valid model numbers are 100, 200, and 300."
   Display "Enter a valid model number."
   Input model
End While

```
```
// Get the model number.
Display "Enter the model number."
Input model

While isInvalid(model)
   Display "The valid model numbers are 100, 200, and 300."
   Display "Enter a valid model number."
   Input model
End While

Function Boolean isInvalid(Integer model)
   // A local variable to hold True or False.
   Declare Boolean status

   // If the model number is invalid, set status to True.
   // Otherwise, set status to False.
   If model != 100 AND model != 200 AND model != 300 Then
      Set status = True
   Else
      Set status = False
   End If

   // Return the test status.
   Return status
End Function
```
```
// Get the answer to the question.
Display "Is your supervisor an effective leader?"
Input answer
// Validate the input.
While answer != "yes" AND answer != "no"
   Display "Please answer yes or no. Is your supervisor an"
   Display "effective leader?"
   Input answer
End While
```
```
// Get the answer to the question.
Display "Is your supervisor an effective leader?"
Input answer
// Validate the input.
While toLower(answer) != "yes" AND toLower(answer) != "no"
   Display "Please answer yes or no. Is your supervisor an"
   Display "effective leader?"
   Input answer
   
```
```
// Get the new password.
Display "Enter your new password."
Input password
// Validate the length of the password.
While length(password) < 6
   Display "The password must be at least six"
   Display "characters long. Enter your new password."
   Input password
End While
 ```
 




