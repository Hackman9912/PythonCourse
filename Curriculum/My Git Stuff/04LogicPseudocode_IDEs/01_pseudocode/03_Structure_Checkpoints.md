# Checkpoint
4.1 What is a control structure?
> An organized easy to follow logical structure of programming 

4.2 What is a decision structure?
>A structure that contains options for the program to go through

4.3What is a single alternative decision structure?
>One continual path based off of a yes or a no. Only one path has an end

4.4 What is a Boolean expression?
>True or False

4.5 What types of relationships between values can you test with relational operators?
>Greater than, less than, equal to, not equal too, greater than or equal to, less than or equal to

4.6 Write a pseudocode If-Then statement that assigns 0 to x if y is equal to 20.

```
If y == 20 then
    Set x = 0
End If
```

4.7 Write a pseudocode If-Then statement that assigns 0.2 to commission if sales is greater than or equal to 10,000.

```
If sales >= 10000 then
    set commission = 0.2
End If
```


4.8 How does a dual alternative decision structure work?

> code has structure to account for either possible option

4.9 What statement do you use in pseudocode to write a dual alternative decision structure?

> If  then else

4.10 When you write an If-Then-Else statement, under what circumstances do the statements that appear between Else and End If execute?
> If == false

4.11 If the following pseudocode were an actual program, what would it display?
```
If "z" < "a" Then
   Display "z is less than a."
Else
   Display "z is not less than a."
End If
```

> it would display the else

4.12 If the following pseudocode were an actual program, what would it display?
```
Declare String s1 = "New York"
Declare String s2 = "Boston"
If s1 > s2 Then
   Display s2
   Display s1
Else
   Display s1
   Display s2
End If
```
> It would display s2 over s1

4.13 How does a dual alternative decision structure work?
```
A dual alternative decision structure has two possible paths of execution—one path is taken if a condition is true, andthe other path is taken if the condition is false.
```
4.14 What statement do you use in pseudocode to write a dual alternative decision structure?
```
If-Then-Else
```
4.15 When you write an If-Then-Else statement, under what circumstances do the statements that appear between the Else clause and the End If clause execute?
```
If the condition is false
```
4.16 Convert the following pseudocode to an If-Then-Else If statement:
```
If number == 1 Then
   Display "One"
Else
   If number == 2 Then
      Display "Two"
   Else
      If number == 3 Then
         Display "Three"
      Else
        Display "Unknown"
      End If
   End If
End If
```
```
If number == 1 Then
   Display "One"
Else if number == 2 then
   Display "Two"
Else If number == 3 Then
   Display "Three"
Else
   Display "Unknown"
End If
```
4.17 What is a multiple alternative decision structure?
```
A structure that tests the value of a variable or an expression and then uses that value to determine which statement or set of statements to execute.
```

4.18 How do you write a multiple alternative decision structure in pseudocode?
```
With a Select Case statement
```
4.19 What does the case structure test, in order to determine which set of statements to execute?
```
A variable or expression
```
4.20 You need to write a multiple alternative decision structure, but the language you are using will not allow you to perform the test you need in a Select Case statement. What can you do to achieve the same results?
```
If-Then-Else-If statement or a nested decision structure
```
4.21 What is a compound Boolean expression?
```
It is an expression that is created by using a logical operator to combine two boolean subexpressions
```
4.22 The following truth table shows various combinations of the values true and false connected by a logical operator. Complete the table by circling T or F to indicate whether the result of such a combination is true or false.

![image](https://user-images.githubusercontent.com/47218880/67030627-697cd600-f0d5-11e9-8d5c-1f6f5ac73583.png)

```
F
T
F
F
T
T
T
F
F
T
```

4.23 Assume the variables a = 2, b = 4, and c = 6. Circle the T or F for each of the following conditions to indicate whether its value is true or false.

![image](https://user-images.githubusercontent.com/47218880/67030655-78638880-f0d5-11e9-8e87-3f2d8c245570.png)


```
T
F
T
T
T

```
4.24 Explain how short-circuit evaluation works with the AND and OR operators.
```
The AND operator: if the expression on the left side of the AND operator is false, the expression on the right side will not be checked
The OR operator: If the expression on the left side of the operator is true the expression on the right will not be checked.
```
4.25Write an If-Then statement that displays the message “The number is valid” if the variable speed is within the range 0 through 200.

```
If speed >= 0 AND speed <= 200 Then
   Display "The number is valid"
End If
```
4.26 Write an If-Then statement that displays the message “The number is not valid” if the variable speed is outside the range 0 through 200.
```
If speed < 0 OR speed > 200 Then
   Display "The number is not valid"
End If
```
4.27 What values can you store in a Boolean variable?
```
True or false variables"
```
4.28 What is a flag variable?
```
A varible that signals when some condition exists in the program
```

