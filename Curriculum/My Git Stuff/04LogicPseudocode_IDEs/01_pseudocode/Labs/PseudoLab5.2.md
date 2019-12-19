# CHOOSE FOUR PROMPTS FROM THE LIST 

# Bug Collector

A bug collector collects bugs every day for seven days. Design a program that keeps a running total of the number of bugs collected during the seven days. The loop should ask for the number of bugs collected for each day, and when the loop is finished, the program should display the total number of bugs collected.

```

Start module()

    Declare integer numBug
    Declare integer totBug
    Declare integer day
    Constant Integer MAX_VALUE = 7
    Set day = 1
    Set totBug = 0

    While day <= MAX_VALUE

        Display "Input the number of bugs you caught today"
        Input = numBug
        Call bugTotal()
        Set day = day + 1
    
    End While

    Display "Here is your weekly total", totBug

End module()

    bugTotal()

        Set totBug = numBug + totBug

    End Module


```

# Calories Burned

Running on a particular treadmill you burn 3.9 calories per minute. Design a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
```
Module main()

    Declare integer min
    Declare real theBurn
    Declare real cal

    // Calories per minute burned
    Set theBurn = 3.9
    Set min = 5

    Do

        Call calcBurn()

    While min <= 30

End Module

Module calcBurn()

    Set min = min + 5
    Set cal = theBurn * min
    Display cal "burned in", min "minutes"

End Module

```

# Budget Analysis

Design a program that asks the user to enter the amount that he or she has budgeted for a month. A loop should then prompt the user to enter each of his or her expenses for the month, and keep a running total. When the loop finishes, the program should display the amount that the user is over or under budget.


```
Module main()

    Declare real monthMoney
    Declare real expense
    Declare real singleCost
    Declare string doAnother

    Set expense = 0

    Display "Enter your total monthly budget"
    Input monthMoney

    Do

        Display "Enter your expense"
        Input singleCost
        Set expense = expense + singleCost

        Display "Do you have other expenses (Y for yes and N for no)"
        Input doAnother

    While doAnother == N OR doAnother == n

    Call howsMoney()


End Module

Module howsMoney()

    If expense <= monthMoney Then

        Display "This is how much money is left:", monthMoney - expense

    Else

        Display "This is how much money you are in the hole for:"
        Display expense - monthMoney

    End If

End Module

```
# Sum of Numbers

Design a program with a loop that asks the user to enter a series of positive numbers. The user should enter a negative number to signal the end of the series. After all the positive numbers have been entered, the program should display their sum.

```
Module Main

    Declare integer num
    Declare string keepGoing
    Declare integer sum

    Set keepGoing = 1
    Set sum = 0

    Display "Enter positive numbers. Once all numbers are entered then"
    Display "enter -1 to add them all together"

    While keepGoing != -1

        Call inputNum()
        Call weDone()

    End While

    Display "Here is your total", sum

End Module

// input number and add to sum
Module inputNum()

    Display "Input number"
    Input num
    Set sum = sum + num

End Module


// Will the user put in -1?
Module weDone()

    Display "Are you done (-1 to be done)?"
    Input keepGoing

End Module

```

# Tuition Increase

At one college, the tuition for a full-time student is $6,000 per semester. It has been announced that the tuition will increase by 2 percent each year for the next five years. Design a program with a loop that displays the projected semester tuition amount for the next five years.

# Average Rainfall

Design a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The program should first ask for the number of years. The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.

# Celsius to Fahrenheit Table

Design a program that displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents. The formula for converting a temperature from Celsius to Fahrenheit is

![image](https://user-images.githubusercontent.com/47218880/67429019-e7911f00-f5a4-11e9-849e-c07e34b8044c.png)

where F is the Fahrenheit temperature and C is the Celsius temperature. Your program must use a loop to display the table.

# Pennies for Pay

Design a program that calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, two pennies the second day, and continues to double each day. The program should ask the user for the number of days. Display a table showing what the salary was for each day, and then show the total pay at the end of the period. The output should be displayed in a dollar amount, not the number of pennies.

# Largest and Smallest

Design a program with a loop that lets the user enter a series of numbers. The user should enter 
−
99
 to signal the end of the series. After all the numbers have been entered, the program should display the largest and smallest numbers entered.

# First and Last

Design a program that asks the user for a series of names (in no particular order). After the final person’s name has been entered, the program should display the name that is first alphabetically and the name that is last alphabetically. For example, if the user enters the names Kristin, Joel, Adam, Beth, Zeb, and Chris, the program would display Adam and Zeb.

# Calculating the Factorial of a Number

In mathematics, the notation n! represents the factorial of the nonnegative integer n. The factorial of n is the product of all the nonnegative integers from 1 up through n. For example:
![image](https://user-images.githubusercontent.com/47218880/67429154-2cb55100-f5a5-11e9-959b-79c4f1a34757.png)

and

![image](https://user-images.githubusercontent.com/47218880/67429177-3c349a00-f5a5-11e9-94c6-82826c1b03cf.png)

Design a program that asks the user to enter a nonnegative integer and then displays the factorial of that number.

# Multiplication Table

Design a program that uses nested loops to display a multiplication table for the numbers 1 through 12. The program’s output should look like this:
```
1 * 0 = 0

1 * 1 = 1

1 * 2 = 2

1 * 3 = 3
```
and so forth..
```
12 * 9 = 108

12 * 10 = 120

12 * 11 = 132

12 * 12 = 144
```
