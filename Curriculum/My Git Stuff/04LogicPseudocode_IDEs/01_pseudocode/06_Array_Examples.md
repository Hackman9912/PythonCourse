
# Inputting and Outputting Array Contents
You can read values from the keyboard and store them in an array element just as you can a regular variable. You can also output the contents of an array element. The pseudocode in Program below shows an array being used to store and display values entered by the user.

## Program 
```
 1  // Create a constant for the number of employees.
 2  Constant Integer SIZE = 3
 3 
 4  // Declare an array to hold the number of hours
 5  // worked by each employee.
 6  Declare Integer hours[SIZE]
 7 
 8  // Get the hours worked by employee 1.
 9  Display "Enter the hours worked by employee 1."
10  Input hours[0]
11 
12  // Get the hours worked by employee 2.
13  Display "Enter the hours worked by employee 2."
14  Input hours[1]
15 
16  // Get the hours worked by employee 3.
17  Display "Enter the hours worked by employee 3."
18  Input hours[2]
19 
20  // Display the values entered.
21  Display "The hours you entered are:"
22  Display hours[0]
23  Display hours[1]
24  Display hours[2]
```
```
Program Output (with Input Shown in Bold)
Enter the hours worked by employee 1.
40 [Enter]
Enter the hours worked by employee 2.
20 [Enter]
Enter the hours worked by employee 3.
15 [Enter]
The hours you entered are:
40
20
15
```
Let’s look at another example. Previous Program could be simplified by using two For loops: one for inputting the values into the array and the other for displaying the contents of the array. This is shown in Program below.

Program 
```
 1  // Create a constant for the size of the array.
 2  Constant Integer SIZE = 3
 3 
 4  // Declare an array to hold the number of hours
 5  // worked by each employee.
 6  Declare Integer hours[SIZE]
 7 
 8  // Declare a variable to use in the loops.
 9  Declare Integer index
10 
11  // Get the hours for each employee.
12  For index = 0 To SIZE − 1
13     Display "Enter the hours worked by"
14     Display "employee number ", index + 1
15     Input hours[index]
16  End For
17 
18  // Display the values entered.
19  Display "The hours you entered are:"
20  For index = 0 To SIZE − 1
21     Display hours[index]
22  End For
```
```
Program Output (with Input Shown in Bold)
Enter the hours worked by
employee number 1
40 [Enter]
Enter the hours worked by
employee number 2
20 [Enter]
Enter the hours worked by
employee number 3
15 [Enter]
The hours you entered are:
40
20
15
```
## Array Bounds Checking
Most programming languages perform array bounds checking, which means they do not allow a program to use an invalid array subscript. For example, look at the following pseudocode:
```
// Create an array.
Constant Integer SIZE = 5
Declare Integer numbers[SIZE]

// ERROR! This statement uses an invalid subscript!
Set numbers[5] = 99
```
This pseudocode declares an array with 5 elements. The subscripts for the array’s elements are 0 through 4. The last statement will cause an error in most languages because it attempts to assign a value in numbers[5], a nonexistent element.

## Watch for Off-by-One Errors
Because array subscripts start at 0 rather than 1, you have to be careful not to perform an off-by-one error. An off-by-one error occurs when a loop iterates one time too many or one time too few. For example, look at the following pseudocode:
```
// This code has an off-by-one error.
Constant Integer SIZE = 100;
Declare Integer numbers[SIZE]
Declare Integer index
For index = 1 To SIZE − 1
   Set numbers[index] = 0
End For
```
The intent of this pseudocode is to create an array of integers with 100 elements, and store the value 0 in each element. However, this code has an off-by-one error. The loop uses its counter variable, index, as a subscript with the numbers array. During the loop’s execution, the index variable takes on the values 1 through 99, when it should take on the values 0 through 99. As a result, the first element, which is at subscript 0, is skipped.

Assuming numbers is the same array as previously declared, the following loop also performs an off-by-one error. This loop correctly starts with the subscript 0, but it iterates one too many times, ending with the subscript 100:
```
// ERROR!
For index = 0 To SIZE
   Set numbers[index] = 0
End For
```
## Partially Filled Arrays
A partially filled array is normally used with an accompanying integer variable that holds the number of items that are actually stored in the array. If the array is empty, then 0 is stored in this variable because there are no items in the array. Each time an item is added to the array, the variable is incremented. When code steps through the array’s elements, the value of this variable is used instead of the array’s size to determine the maximum subscript. Program below shows a demonstration.

## Program
```
 1  // Declare a constant for the array size.
 2  Constant Integer SIZE = 100
 3
 4  // Declare an array to hold integer values.
 5  Declare Integer values[SIZE]
 6
 7  // Declare an Integer variable to hold the number of items
 8  // that are actually stored in the array.
 9  Declare Integer count = 0
10
11  // Declare an Integer variable to hold the user's input.
12  Declare Integer number
13
14  // Declare a variable to step through the array.
15  Declare Integer index
16
17  // Prompt the user to enter a number. If the user enters the
18  // sentinel value − 1 we will stop accepting input.
19  Display "Enter a number or − 1 to quit."
20  Input number
21
22  // If the input is not − 1 and the array is not
23  // full, process the input.
24  While (number != − 1 AND count < SIZE)
25     // Store the input in the array.
26     Set values[count] = number
27
28     // Increment count.
29     count = count + 1
30
31     // Prompt the user for the next number.
32     Display "Enter a number or − 1 to quit."
33     Input number
34  End While
35
36  // Display the values stored in the array.
37  Display "Here are the numbers you entered:"
38  For index = 0 To count − 1
39     Display values[index]
40  End For
```
```
Program Output (with Input Shown in Bold)
Enter a number or − 1 to quit.
2 [Enter]
Enter a number or − 1 to quit.
4 [Enter]
Enter a number or − 1 to quit.
6 [Enter]
Enter a number or − 1 to quit.
− 1 [Enter]
Here are the numbers you entered:
2
4
6
```
## The For Each Loop
```
Constant Integer SIZE = 5
Declare Integer numbers[SIZE] = 5, 10, 15, 20, 25
Declare Integer num
```
The following For Each loop can be used to display all of the values stored in the ­numbers array:
```
For Each num In numbers
   Display num
End For
```
The pseudocode in Program below demonstrates how to implement the sequential search in a program. 
This program has an array that holds test scores. It sequentially searches the array for a score of 100.
If a score of 100 is found, the program displays the test number.

## Program
```
 1  // Constant for the array size.
 2  Constant Integer SIZE = 10
 3 
 4  // Declare an array to hold test scores.
 5  Declare Integer scores[SIZE] = 87, 75, 98, 100, 82,
 6                                 72, 88, 92, 60, 78
 7 
 8  // Declare a Boolean variable to act as a flag.
 9  Declare Boolean found
10 
11  // Declare a variable to use as a loop counter.
12  Declare Integer index
13 
14  // The flag must initially be set to False.
15  Set found = False
16 
17  // Set the counter variable to 0.
18  Set index = 0
19 
20  // Step through the array searching for a
21  // score equal to 100.
22  While found == False AND index <= SIZE − 1
23     If scores[index] == 100 Then
24        Set found = True
25     Else
26        Set index = index + 1
27     End If
28  End While
29 
30  // Display the search results.
31  If found Then
32     Display "You earned 100 on test number ", index + 1
33  Else
34     Display "You did not earn 100 on any test."
35  End If
```
Program Output
```
You earned 100 on test number 4
```
##  Searching a String Array
Previus Program demonstrates how to use the sequential search algorithm to find a specific number in an Integer array. 
As shown in Program below, you can also use the algorithm to find a string in a String array.

Program 
```
 1  // Declare a constant for the array size.
 2  Constant Integer SIZE = 6
 3 
 4  // Declare a String array initialized with values.
 5  Declare String names[SIZE] = "Ava Fischer", "Chris Rich",
 6                               "Gordon Pike", "Matt Hoyle",
 7                               "Rose Harrison", "Giovanni Ricci"
 8 
 9  // Declare a variable to hold the search value.
10  Declare String searchValue
11 
12  // Declare a Boolean variable to act as a flag.
13  Declare Boolean found
14 
15  // Declare a counter variable for the array.
16  Declare Integer index
17 
18  // The flag must initially be set to False.
19  Set found = False
20 
21  // Set the counter variable to 0.
22  Set index = 0
23 
24  // Get the string to search for.
25  Display "Enter a name to search for in the array."
26  Input searchValue
27 
28  // Step through the array searching for
29  // the specified name.
30  While found == False AND index <= SIZE − 1
31     If names[index] == searchValue Then
32        Set found = True
33     Else
34        Set index = index + 1
35     End If
36  End While
37 
38  // Display the search results.
39  If found Then
40     Display "That name was found at subscript ", index
41  Else
42     Display "That name was not found in the array."
43  End If
```
```
Program Output (with Input Shown in Bold)
Enter a name to search for in the array.
Matt Hoyle [Enter]
That name was found at subscript 3.
Program Output (with Input Shown in Bold)
Enter a name to search for in the array.
Matt [Enter]
That name was not found in the array.
```
The pseudocode in Program below shows how you can modify the previous Program to use the "contains" function. This version of the program will find strings in the array that partially match the string entered by the user.

Program 
```
 1  // Declare a constant for the array size.
 2  Constant Integer SIZE = 6
 3 
 4  // Declare a String array initialized with values.
 5  Declare String names[SIZE] = "Ava Fischer", "Chris Rich",
 6                               "Gordon Pike", "Matt Hoyle",
 7                               "Rose Harrison", "Giovanni Ricci"
 8 
 9  // Declare a variable to hold the search value.
10  Declare String searchValue
11 
12  // Declare a Boolean variable to act as a flag.
13  Declare Boolean found
14 
15  // Declare a counter variable for the array.
16  Declare Integer index
17 
18  // The flag must initially be set to False.
19  Set found = False
20 
21  // Set the counter variable to 0.
22  Set index = 0
23 
24  // Get the string to search for.
25  Display "Enter a name to search for in the array."
26  Input searchValue
27 
28  // Step through the array searching for
29  // the specified name.
30  While found == False AND index <= SIZE − 1
31     If contains(names[index], searchValue) Then
32        Set found = True
33     Else
34        Set index = index + 1
35     End If
36  End While
37 
38  // Display the search results.
39  If found Then
40     Display "That name matches the following element:"
41     Display names[index]
42  Else
43     Display "That name was not found in the array."
44  End If
```
```
Program Output (with Input Shown in Bold)
Enter a name to search for in the array.
Matt [Enter]
That name matches the following element:
Matt Hoyle
```
## Totaling the Values in an Array

Program 
```
 1  // Declare a constant for the array size.
 2  Constant Integer SIZE = 5
 3
 4  // Declare an array initialized with values.
 5  Declare Integer numbers[SIZE] = 2, 4, 6, 8, 10
 6
 7  // Declare and initialize an accumulator variable.
 8  Declare Integer total = 0
 9
10  // Declare a counter variable for the loop.
11  Declare Integer index
12
13  // Calculate the total of the array elements.
14  For index = 0 To SIZE − 1
15      Set total = total + numbers[index]
16  End For
17
18  // Display the sum of the array elements.
19  Display "The sum of the array elements is ", total
```
```
Program Output
The sum of the array elements is 30
```

## Averaging the Values in an Array

The first step in calculating the average of the values in an array is to get the total of the values. You saw how to do that with a loop in the preceding section. The second step is to divide the total by the number of elements in the array. The pseudocode in ­Program below demonstrates the algorithm.

Program
```
 1  // Declare a constant for the array size.
 2  Constant Integer SIZE = 5
 3
 4  // Declare an array initialized with values.
 5  Declare Real scores[SIZE] = 2.5, 8.3, 6.5, 4.0, 5.2
 6
 7  // Declare and initialize an accumulator variable.
 8  Declare Real total = 0
 9
10  // Declare a variable to hold the average.
11  Declare Real average
12
13  // Declare a counter variable for the loop.
14  Declare Integer index
15
16  // Calculate the total of the array elements.
17  For index = 0 To SIZE − 1
18      Set total = total + numbers[index]
19  End For
20  
21  // Calculate the average of the array elements.
22   Set average = total / SIZE
23
24  // Display the average of the array elements.
25  Display "The average of the array elements is ", average
```
```
Program Output
The average of the array elements is 5.3
```

# Finding the Highest Value in an Array

Program 
```
 1  // Declare a constant for the array size.
 2  Constant Integer SIZE = 5
 3 
 4  // Declare an array initialized with values.
 5  Declare Integer numbers[SIZE] = 8, 1, 12, 6, 2
 6 
 7  // Declare a counter variable for the array.
 8  Declare Integer index
 9 
10  // Declare a variable to hold the lowest value.
11  Declare Integer lowest
12 
13  // Assign the first element to lowest.
14  Set lowest = numbers[0]
15 
16  // Step through the rest of the array,
17  // beginning at element 1. When a value
18  // less than lowest is found, assign
19  // that value to lowest.
20  For index = 1 To SIZE − 1
21     If numbers[index] < lowest Then
22        Set lowest = numbers[index]
23     End If
24  End For
25 
26  // Display the lowest value.
27  Display "The lowest value in the array is ", lowest
```
```
Program Output
The lowest value in the array is 1
```
## Copying an Array
```
Constant Integer SIZE = 5
Declare Integer firstArray[SIZE] = 100, 200, 300, 400, 500
Declare Integer secondArray[SIZE]
```
```
Declare Integer index
For index = 0 To SIZE − 1
   Set secondArray[index] = firstArray[index]
End For
```
## Passing an Array as an Argument to a Module or a Function

The pseudocode in Program below shows an example of a function that accepts an ­Integer array as an argument. The function returns the total of the array’s elements.

Program 
```
 1  Module main()
 2     // A constant for the array size.
 3     Constant Integer SIZE = 5
 4    
 5     // An array initialized with values.
 6     Declare Integer numbers[SIZE] = 2, 4, 6, 8, 10
 7    
 8     // A variable to hold the sum of the elements.
 9     Declare Integer sum
10     
11     // Get the sum of the elements.
12     Set sum = getTotal(numbers, SIZE)
13    
14     // Display the sum of the array elements.
15     Display "The sum of the array elements is ", sum
16  End Module
17 
18  // The getTotal function accepts an Integer array and the
19  // array's size as arguments. It returns the total of the
20  // array elements.
21  Function Integer getTotal(Integer array[], Integer arraySize)
22     // Loop counter
23     Declare Integer index
24    
25     // Accumulator, initialized to 0
26     Declare Integer total = 0
27    
28     // Calculate the total of the array elements.
29     For index = 0 To arraySize − 1
30        Set total = total + array[index]
31     End For
32    
33     // Return the total.
34     Return total
35  End Function
```
```
Program Output
The sum of the array elements is 30
```
## Parallel Arrays
CONCEPT: By using the same subscript, you can establish relationships between data stored in two or more arrays.

To access the data, you use the same subscript with both arrays. For example, the loop in the following pseudocode displays each person’s name and address:
```
Declare Integer index
For index = 0 To SIZE − 1
   Display names[index]
   Display addresses[index]
End For
```
## Using Parallel Arrays

In this section, Megan asked you to design a program that allows her to enter the number of hours worked by each of her employees and then displays each employee’s gross pay. As it is currently designed, the program refers to the employees as “employee 1,” employee 2,” and so on. Megan has asked you to modify the program so she can enter employees’ names along with their hours, and then it should display each employee’s name along with his or her gross pay.

Currently, the program has an array named hours that holds each employee’s hours worked. You decide to add a parallel array named names that will hold each employee’s name. The first employee’s data will appear in names[0] and in hours[0], the second employee’s data will appear in names[1] and in hours[1], and so on.

Here is the updated program:
```
For each employee:

Get the employee’s name and store it in the names array.

Get the employee’s number of hours worked and store it in the corresponding element of the hours array.

Step through each set of elements in the parallel arrays and display the employee’s name and gross pay.
```
Program below shows the pseudocode for the revised program

Program 
```
 1  // Constant for the array sizes.
 2  Constant Integer SIZE = 6
 3
 4  // Array to hold each employee's name.
 5  Declare String names[SIZE]
 6
 7  // Array to hold each employee's hours.
 8  Declare Real hours[SIZE]
 9
10  // Variable to hold the hourly pay rate.
11  Declare Real payRate
12
13  // Variable to hold a gross pay amount.
14  Declare Real grossPay
15
16  // Variable to use as a loop counter.
17  Declare Integer index
18
19  // Get each employee's data.
20  For index = 0 To SIZE − 1
21      // Get an employee's name.
22      Display "Enter the name of employee ", index + 1
23      Input names[index]
24
25      // Get the employee's hours.
26      Display "Enter the hours worked by that employee."
27      Input hours[index]
28  End For
29
30  // Get the hourly pay rate.
31  Display "Enter the hourly pay rate."
32  Input payRate
33
34  // Display each employee's gross pay.
35  Display "Here is each employee's gross pay."
36  For index = 0 To SIZE − 1
37      Set grossPay = hours[index] * payRate
38      Display names[index], ": ", currencyFormat(grossPay)
39  End For
```
```
Program Output (with Input Shown in Bold)
Enter the name of employee 1
Jamie Lynn [Enter]
Enter the hours worked by that employee.
10 [Enter]
Enter the name of employee 2
Courtney [Enter]
Enter the hours worked by that employee.
20 [Enter]
Enter the name of employee 3
Ashley [Enter]
Enter the hours worked by that employee.
15 [Enter]
Enter the name of employee 4
Brian [Enter]
Enter the hours worked by that employee.
40 [Enter]
Enter the name of employee 5
Jane [Enter]
Enter the hours worked by that employee.
20 [Enter]
Enter the name of employee 6
Ian [Enter]
Enter the hours worked by that employee.
18 [Enter]
Enter the hourly pay rate.
12.75 [Enter]
Here is each employee's gross pay.
Jamie Lynn: $127.50
Courtney: $255.00
Ashley: $191.25
Brian: $510.00
Jane: $255.00
Ian: $229.50
```
## Accessing the Elements in a Two-Dimensional Array
To access one of the elements in a two-dimensional array, you must use both subscripts. For example, the following pseudocode statement assigns the number 95 to values[2][1]:
```
Set values[2][1] = 95
```
Programs that process two-dimensional arrays commonly do so with nested loops. The pseudocode in the program below shows an example. It declares an array with three rows and four columns, prompts the user for values to store in each element, and then displays the values in each element.

Program
```
 1  // Create a 2D array.
 2  Constant Integer ROWS = 3
 3  Constant Integer COLS = 4
 4  Declare Integer values[ROWS][COLS]
 5 
 6  // Counter variables for rows and columns.
 7  Declare Integer row, col
 8 
 9  // Get values to store in the array.
10  For row = 0 To ROWS − 1
11     For col = 0 To COLS − 1
12        Display "Enter a number."
13        Input values[row][col]
14     End For
15  End For
16 
17  // Display the values in the array.
18  Display "Here are the values you entered."
19  For row = 0 To ROWS − 1
20     For col = 0 To COLS − 1
21        Display values[row][col]
22     End For
23  End For
```
```
Program Output (with Input Shown in Bold)
Enter a number.
1 [Enter]
Enter a number.
2 [Enter]
Enter a number.
3 [Enter]
Enter a number.
4 [Enter]
Enter a number.
5 [Enter]
Enter a number.
6 [Enter]
Here are the values you entered.
1
2
3
4
5
6
```
## Using a Two-Dimensional Array

Unique Candy Inc. has three divisions: division 1 (East Coast), division 2 (Midwest), and division 3 (West Coast). The sales manager has asked you to design a program that will read as input each division’s sales for each quarter of the year, and then display the total sales for all divisions.

This program requires you to process three sets of data:
```
The sales amounts for division 1

The sales amounts for division 2

The sales amounts for division 3
```
Each of these sets of data contains four items:
```

The sales for quarter 1

The sales for quarter 2

The sales for quarter 3

The sales for quarter 4
```

You decide to store the sales amounts in a two-dimensional array. The array will have three rows (one for each division) and four columns (one for each quarter). Figure below shows how the sales data will be organized in the array.

![image](https://user-images.githubusercontent.com/47218880/67575519-5cc63680-f702-11e9-8707-68d2e8ee7381.png)

Two-dimensional array to hold sales data

The program will use a pair of nested loops to read the sales amounts. It will then use a pair of nested loops to add all of the array elements to an accumulator variable. Here is an overview of the algorithm:
```
For each division:

For each quarter:

Read the amount of sales for the quarter and store it in the array.

For each row in the array:

For each column in the array:

Add the amount in the column to an accumulator.

Display the amount in the accumulator.

```
Program shows the pseudocode for the program.

Program
```
 1  // Constants for the array sizes.
 2  Constant Integer ROWS = 3
 3  Constant Integer COLS = 4
 4 
 5  // An array to hold company sales.
 6  Declare Real sales[ROWS][COLS]
 7 
 8  // Counter variables
 9  Declare Integer row, col
10 
11  // Accumulator
12  Declare Real total = 0
13 
14  // Display instructions.
15  Display "This program calculates the company's"
16  Display "total sales. Enter the quarterly sales"
17  Display "amounts for each division when prompted."
18 
19  // Nested loops to fill the array with quarterly
20  // sales amounts for each division.
21  For row = 0 To ROWS − 1
22     For col = 0 To COLS − 1
23        Display "Division ", row + 1, " quarter ", col + 1
24        Input sales[row][col]
25     End For
26     // Display a blank line.
27     Display
28  End For
29 
30  // Nested loops to add all of the array elements.
31  For row = 0 To ROWS − 1
32     For col = 0 To COLS − 1
33        Set total = total + sales[row][col]
34     End For
35  End For
36 
37  // Display the total sales.
38  Display "The total company sales are: $",
39           currencyFormat(total)
```
```
Program Output (with Input Shown in Bold)
This program calculates the company's total sales. Enter the quarterly sales 
amounts for each division when prompted.

Division 1 quarter 1
1000.00 [Enter]
Division 1 quarter 2
1100.00 [Enter]
Division 1 quarter 3
1200.00 [Enter]
Division 1 quarter 4
1300.00 [Enter]

Division 2 quarter 1
2000.00 [Enter]
Division 2 quarter 2
2100.00 [Enter]
Division 2 quarter 3
2200.00 [Enter]
Division 2 quarter 4
2300.00 [Enter]

Division 3 quarter 1
3000.00 [Enter]
Division 3 quarter 2
3100.00 [Enter]
Division 3 quarter 3
3200.00 [Enter]
Division 3 quarter 4
3300.00 [Enter]

The total company sales are: $25,800.00
```

