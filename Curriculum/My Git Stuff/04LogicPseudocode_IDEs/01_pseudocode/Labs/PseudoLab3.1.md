1. Design an If-Then statement (or a flowchart with a single alternative decision structure) that assigns 20 to the variable y and assigns 40 to the variable z if the variable x is greater than 100.

```
If x > 100 Then
   Set y = 20 
   Set z = 40
End If

```
2. Design an If-Then statement (or a flowchart with a single alternative decision structure) that assigns 0 to the variable b and assigns 1 to the variable c if the variable a is less than 10.

```
If a < 10 Then
   Set b = 0
   Set c = 1
End If
```
3. Design an If-Then-Else statement (or a flowchart with a dual alternative decision structure) that assigns 0 to the variable b if the variable a is less than 10. Otherwise, it should assign 99 to the variable b.

```
If a < 10 Then
   Set b = 0
Else
   Set b = 99
End If
```
4. The following pseudocode contains several nested If-Then-Else statements. Unfortunately, it was written without proper alignment and indentation. Rewrite the code and use the proper conventions of alignment and indentation.
```
If score < 60 Then
   Display "Your grade is F."
ElseIf score < 70 Then
   Display "Your grade is D."
ElseIf score < 80 Then
   Display "Your grade is C."
ElseIf score < 90 Then
   Display "Your grade is B."
Else
   Display "Your grade is A."
End If

```
5. Design nested decision structures that perform the following: If amount1 is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2.

```
If amount1 > 10 AND amount2 < 100 Then
   If amount1 > amount2 Then
      Display amount1
   ElseIf amount2 > amount 1 Then
      Display amount 2
End If
End If
```

6. Rewrite the following If-Then-Else If statement as a Select Case statement.
```
If selection == 1 Then
   Display "You selected A."
Else If selection == 2 Then
   Display "You selected 2."
Else If selection == 3 Then
   Display "You selected 3."
Else If selection == 4 Then
   Display "You selected 4."
Else
   Display "Not good with numbers, eh?"
End If


Case based on selection
Case == 1 Then
   Display "You selected A."
Case == 2 Then
   Display "You selected 2."
Case == 3 Then
   Display "You selected 3."
Case == 4 Then
   Display "You selected 4."
Default
   Display "Not good with numbers, eh?"
End If

```
7. Design an If-Then-Else statement (or a flowchart with a dual alternative decision structure) that displays “Speed is normal” if the speed variable is within the range of 24 to 56. If speed holds a value outside this range, display “Speed is abnormal.”

```
If speed > 23 AND speed < 57 Then
   Display "Speed is normal"
Else 
   Display "Speed is abnormal"
End If
```
8. Design an If-Then-Else statement (or a flowchart with a dual alternative decision structure) that determines whether the points variable is outside the range of 9 to 51. If the variable holds a value outside this range it should display “Invalid points.” Otherwise, it should display “Valid points.”

```
If points > 8 AND points < 52 Then
   Display "Valid points."
Else
   Display "Invalid points."
End If
```

9. Design a case structure that tests the month variable and does the following:

* If the month variable is set to 1, it displays “January has 31 days.”

* If the month variable is set to 2, it displays “February has 28 days.”

* If the month variable is set to 3, it displays “March has 31 days.”

* If the month variable is set to anything else, it displays “Invalid selection.”

```
Case based on month
   Case == 1
      Display "January has 31 days."
   Case == 2
      Display "February has 21 days."
   Case == 3
      Display "March has 31 days."
   Default
      Display "Invalid selection."
End Case

```
10. Write an If-Then statement that sets the variable hours to 10 when the flag variable minimum is set.

```
If minimum then
   set hours = 10
```
