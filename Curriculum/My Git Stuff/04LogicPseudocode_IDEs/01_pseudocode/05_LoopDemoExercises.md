
# Program 5-1
```
 1  // Variable declarations
 2  Declare Real sales, commission
 3  Declare String keepGoing = "y"
 4
 5  // Constant for the commission rate
 6  Constant Real COMMISSION_RATE = 0.10
 7
 8  While keepGoing == "y"
 9      // Get the amount of sales.
10      Display "Enter the amount of sales."
11      Input sales
12
13      // Calculate the commission.
14      Set commission = sales * COMMISSION_RATE
15
16      // Display the commission
17      Display "The commission is $", commission
18
19      Display "Do you want to calculate another"
20      Display "commission? (Enter y for yes.)"
21      Input keepGoing
22  End While
```
```
Program Output (with Input Shown in Bold)
Enter the amount of sales.
10000.00 [Enter] 
The commission is $1000
Do you want to calculate another
commission? (Enter y for yes.)
y [Enter] 
Enter the amount of sales.
5000.00 [Enter] 
The commission is $500
Do you want to calculate another
commission? (Enter y for yes.)
y [Enter] 
Enter the amount of sales.
12000.00  [Enter] 
The commission is $1200
Do you want to calculate another
commission? (Enter y for yes.)
n [Enter]
```
# Program 5-2
```
 1  // Declare a variable to hold the password.
 2  Declare String password
 3
 4  // Repeatedly ask the user to enter a password
 5  // until the correct one is entered.
 6  Do
 7     // Prompt the user to enter the password.
 8     Display "Enter the password."
 9     Input password
10
11     // Display an error message if the wrong
12     // password was entered.
13     If password != "prospero" Then
14        Display "Sorry, try again."
15     End If
16  Until password == "prospero"
17
18  // Indicate that the password is confirmed.
19  Display "Password confirmed."
```
```
Program Output (with Input Shown in Bold)
Enter the password.
ariel [Enter] 
Sorry, try again.
Enter the password.
caliban [Enter] 
Sorry, try again.
Enter the password.
prospero [Enter] 
Password confirmed.
```
# Program 5-3
```
1  Declare Integer counter
2  Constant Integer MAX_VALUE = 5
3
4  For counter = 1 To MAX_VALUE
5     Display "Hello world"
6  End For
```
```
Program Output
Hello world
Hello world
Hello world
Hello world
Hello world
```
# Program 5-10
```
 1  // Declare a counter variable
 2  Declare Integer counter
 3
 4  // Constant for the maximum value
 5  Constant Integer MAX_VALUE = 11
 6
 7  // Display the odd numbers from 1 through 11.
 8  For counter = 1 To MAX_VALUE Step 2
 9     Display counter
10  End For
```
```
Program Output
1
3
5
7
9
11
```
# Program 5-5
```
 1  // Variables
 2  Declare Integer counter, square, upperLimit
 3
 4  // Get the upper limit.
 5  Display "This program displays numbers, starting at 1,"
 6  Display "and their squares. How high should I go?"
 7  Input upperLimit
 8
 9  // Display table headings.
10  Display "Number", Tab, "Square"
11  Display "--------------------"
12
13  // Display the numbers and their squares.
14  For counter = 1 To upperLimit
15     // Calculate number squared.
16     Set square = counter^2
17
18     // Display number and number squared.
19     Display counter, Tab, square
20  End For
```
```
Program Output
This program displays numbers, starting at 1,
and their squares. How high should I go?
5 [Enter]
```
![image](https://user-images.githubusercontent.com/47218880/67425915-92520f00-f59e-11e9-8a76-cc0cd143bb56.png)

# Program 5-6
```
 1  // Variables
 2  Declare Integer counter, square,
 3                  lowerLimit, upperLimit
 4
 5  // Get the lower limit.
 6  Display "This program displays numbers and"
 7  Display "their squares. What number should"
 8  Display "I start with?"
 9  Input lowerLimit
10
11  // Get the upper limit.
12  Display "What number should I end with?"
13  Input upperLimit
14
15  // Display table headings.
16  Display "Number", Tab, "Square"
17  Display "-----------------------"
18
19  // Display the numbers and their squares.
20  For counter = lowerLimit To upperLimit
21     // Calculate number squared.
22     Set square = counter^2
23
24     // Display number and number squared.
25     Display counter, Tab, square
26  End For
```
```
Program Output
This program displays numbers and
their squares. What number should
I start with?
3 [Enter] 
What number should I end with?
7 [Enter]
```
![image](https://user-images.githubusercontent.com/47218880/67426000-c1688080-f59e-11e9-8931-f1ea69fd8673.png)

# Program 5-7
```
 1  // Declare and initialize a counter variable.
 2  Declare Integer counter = 1
 3
 4  // Constant for the maximum value
 5  Constant Integer MAX_VALUE = 5
 6
 7  While counter <= MAX_VALUE
 8     Display "Hello world"
 9     Set counter = counter + 1
10  End While
```
```
Program Output
Hello world
Hello world
Hello world
Hello world
Hello world
```

#Program 5-8
```
 1  // Declare a variable to hold each number
 2  // entered by the user.
 3  Declare Integer number
 4
 5  // Declare an accumulator variable,
 6  // initialized with 0.
 7  Declare Integer total = 0
 8
 9  // Declare a counter variable for the loop.
10  Declare Integer counter
11
12  // Explain what we are doing.
13  Display "This program calculates the"
14  Display "total of five numbers."
15
16  // Get five numbers and accumulate them.
17  For counter = 1 To 5
18       Display "Enter a number."
19       Input number
20      Set total = total + number
21   End For
22
23   // Display the total of the numbers.
24   Display "The total is ", total
```
```
Program Output (with Input Shown in Bold)
This program calculates the
total of five numbers.
Enter a number.
2 [Enter] 
Enter a number.
4 [Enter] 
Enter a number.
6 [Enter] 
Enter a number.
8 [Enter] 
Enter a number.
10 [Enter] 
The total is 30
```
