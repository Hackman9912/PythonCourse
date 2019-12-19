# Demo Example Labs

## Program 6-1 
shows the pseudocode for a complete program that uses the random ­function. The statement in line 2 generates a random number in the range of 1 through 10 and assigns it to the number variable. (The program output shows that the number 7 was generated, but this value is arbitrary. If this were an actual program, it could display any number between 1 and 10.)

### Program 6-1
```
1  Declare Integer number
2  Set number = random(1, 10)
3  Display number
```
```
Program Output
7
```
## NOTE:
The way that you set up a program to work with library functions differs among programming languages. In some languages you don’t have to do anything special to call library functions. That’s the approach we take in our pseudocode. In other languages, however, you may have to write a statement near the top of a program indicating that it will access a particular library function.

The pseudocode in Program 6-2 shows another example. This program uses a For loop that iterates five times. Inside the loop, the statement in line 9 calls the random function to generate a random number in the range of 1 through 100.

## Program 6-2
```
 1  // Declare variables
 2  Declare Integer number, counter
 3
 4  // The following loop displays
 5  // five random numbers.
 6  For counter = 1 To 5
 7     // Get a random number in the range of
 8     // 1 through 100 and assign it to number.
 9     Set number = random(1, 100)
10
11     // Display the number.
12     Display number
13  End For
```
```
Program Output
89
7
16
41
12
```
The pseudocode in both Programs 6-1 and 6-2 calls the random function and assigns its return value to the number variable. If you just want to display a random number, it is not necessary to assign the random number to a variable. You can send the random function’s return value directly to the Display statement, as shown here:
```
Display random(1, 10)
```
When this statement executes, the random function is called. The function generates a random number in the range of 1 through 10. That value is returned and then sent to the Display statement. As a result, a random number in the range of 1 through 10 will be displayed. Figure below illustrates this.
![image](https://user-images.githubusercontent.com/47218880/67445308-11146f80-f5d2-11e9-8535-c783fee5ef09.png)

An illustration that displays a random number.
Figure Displaying a random number

The pseudocode in Program 6-3 shows how you could simplify Program 6-2. This program also displays five random numbers, but this program does not use a variable to hold those numbers. The random function’s return value is sent directly to the Display statement in line 4.

## Program 6-3
```
 1  // Counter variable
 2  Declare Integer counter
 3
 4  // This loop displays five random numbers.
 5  For counter = 1 To 5
 6     Display random(1, 100)
 7  End For
 ```
 ```
Program Output
32
79
6
12
98
```
## Program 6-4
```
 1  Module main()
 2     // Local variables
 3     Declare Integer firstAge, secondAge, total
 4
 5     // Get the user's age and the user's
 6     // best friend's age.
 7     Display "Enter your age."
 8     Input firstAge
 9     Display "Enter your best friend's age."
10     Input secondAge
11
12     // Get the sum of both ages.
13     Set total = sum(firstAge, secondAge)
14
15     // Display the sum.
16     Display "Together you are ", total, " years old."
17  End Module
18
19  // The sum function accepts two Integer arguments and
20  // returns the sum of those arguments as an Integer.
21  Function Integer sum(Integer num1, Integer num2)
22     Declare Integer result
23     Set result = num1 + num2
24     Return result
25  End Function
```
```
Program Output (with Input Shown in Bold)
Enter your age.
22 [Enter]
Enter your best friend's age.
24 [Enter]Together you are 46 years old.
```
## Program 6-5
```
 1  // Global constant for the discount percentage.
 2  Constant Real DISCOUNT_PERCENTAGE = 0.20
 3
 4  // The main module is the program's starting point.
 5  Module main()
 6     // Local variables to hold regular and sale prices.
 7     Declare Real regularPrice, salePrice
 8
 9     // Get the item's regular price.
10     Set regularPrice = getRegularPrice()
11
12     // Calculate the sale price.
13     Set salePrice = regularPrice − discount(regularPrice)
14
15     // Display the sale price.
16     Display "The sale price is $", salePrice
17  End Module
18
19  // The getRegularPrice function prompts the
20  // user to enter an item's regular price and
21  // returns that value as a Real.
22  Function Real getRegularPrice()
23     // Local variable to hold the price.
24     Declare Real price
25
26     // Get the regular price.
27     Display "Enter the item's regular price."
28     Input price
29
30     // Return the regular price.
31     Return price
32  End Function
33
34  // The discount function accepts an item's price
35  // as an argument and returns the amount of the
36  // discount specified by DISCOUNT_PERCENTAGE.
37  Function Real discount(Real price)
38     Return price * DISCOUNT_PERCENTAGE
39  End Function
```
```
Program Output (with Input Shown in Bold)
Enter the item's regular price.
100.00 [Enter]The sale price is $80
```
## Program 6-6
```
 1  // Variable declarations
 2  Declare Integer number
 3  Declare Real squareRoot
 4
 5  // Get a number.
 6  Display "Enter a number."
 7  Input number
 8
 9  // Calculate and display its square root.
10  Set squareRoot = sqrt(number)
11  Display "The square root of that number is ", squareRoot
```
```
Program Output (with Input Shown in Bold)
Enter a number.
25 [Enter]
The square root of that number is 5
```
The pseudocode in Program below finds the hypotenuse of a right triangle. The program uses the following formula, which you might recall from geometry class:

![image](https://user-images.githubusercontent.com/47218880/67445868-18d51380-f5d4-11e9-971e-785e4932284a.png)

In the formula, c is the length of the hypotenuse, and a and b are the lengths of the other sides of the triangle.

## Program 
```
 1  // Variable declarations
 2  Declare Real a, b, c
 3
 4  // Get the length of side A.
 5  Display "Enter the length of side A."
 6  Input a
 7
 8  // Get the length of side B.
 9  Display "Enter the length of side B."
10  Input b
11
12  // Calculate the length of the hypotenuse.
13  Set c = sqrt(a^2 + b^2)
14
15  // Display the length of the hypotenuse.
16  Display "The length of the hypotenuse is ", c
```
```
Program Output (with Input Shown in Bold)
Enter the length of side A.
5.0 [Enter]
Enter the length of side B.
12.0 [Enter]
The length of the hypotenuse is 13
```
