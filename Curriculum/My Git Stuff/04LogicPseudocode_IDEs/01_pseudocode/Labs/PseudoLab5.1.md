# Exercise Workbench
* Design a While loop that lets the user enter a number. The number should be multiplied by 10, and the result stored in a variable named product. The loop should iterate as long as product contains a value less than 100.


```
Declare integer prodct
Declare integer inNumber
Declare real MAX_NUM = 100
modMain()

   Display "Enter a number"
   Input inNumber
   Set product = inNumber *10

   While product < MAX_NUM
      Display "Too small, try again"
      Input inNumber
   End While

   Display "Good Job"

End

```
* Design a Do-While loop that asks the user to enter two numbers. The numbers should be added and the sum displayed. The loop should ask the user whether he or she wishes to perform the operation again. If so, the loop should repeat; otherwise it should terminate.

```
Module main()

   Declare integer num1
   Declare integer num2
   Declare integer total

   Do

      Display "Input your first number"
      Input num1

      Display "Input your second number"
      Input num2

      Call addEm()

      Display "Do you want to do another (y or Y for yes)?"
      Input doAnother

   While doAnother == "Y" OR do Another == "y"

End Module

Module addEm()

   Set total = num1 + num2
   Display "Here is the total", total

End Module

```

* Design a For loop that displays the following set of numbers:

0, 10, 20, 30, 40, 50, . . . , 1000

```
Module main()

   Declare integer num
   Declare integer MAX_VALUE 
   Constant integer MAX_VALUE = 1000
   Set num = 0

   Display "Here is the first number", num

  For num = 0 To MAX_VALUE

      Set num = num + 10
      Display "Here is the latest number", num

   End For

End Module

```
* Design a loop that asks the user to enter a number. The loop should iterate 10 times and keep a running total of the numbers entered.


```
Module main()

   Declare integer num
   Declare string list
   Declare integer counter
   Constant integer MAX_VALUE = 10

   For counter = 1 To MAX_Value

   Display "Enter a number"
   Input num

   Call numList()

   End For

End Module

   numList()

      Output num | list
      Display "Here are your numbers", list

   End Module

```


* Design a For loop that calculates the total of the following series of numbers:
![image](https://user-images.githubusercontent.com/47218880/67423054-31740800-f599-11e9-9565-031c1f729e1c.png)


```
Declare Integer denominator, numerator
Declare Real value, total
Set denominator = 30
Set total = 0
   For numerator = 1 To 30
      Set value = numerator / denominator
      Set total = total + value
      Set denominator = denominator - 1
   End For
Display total

```

* Design a nested loop that displays 10 rows of # characters. There should be 15 # characters in each row.

* Convert the While loop in the following code to a Do-While loop:
```
Declare Integer x = 1
While x > 0
   Display "Enter a number."
   Input x
End While
```

```
Declare Integer x=1

Display "Enter a number"
Input X

While X >0
```



* Convert the Do-While loop in the following code to a While loop:
```
Declare String sure
Do
  Display "Are you sure you want to quit?"
  Input sure
While sure != "Y" AND sure != "y"
```
* Convert the following While loop to a For loop:
```
Declare Integer count = 0
While count < 50
   Display "The count is ", count
   Set count = count + 1
End While
```
* Convert the following For loop to a While loop:
```
Declare Integer count
For count = 1 To 50
   Display count
End For
```
