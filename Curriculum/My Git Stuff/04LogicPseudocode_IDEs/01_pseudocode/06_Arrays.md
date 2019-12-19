|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---
 
![](/01_pseudocode/assets/bookCover.png)

**Information used in this lesson topic and Figures shown are from the following source:** Farrell, Joyce, Programming Logic & Design (2017), comprehensive, 9th edition. Centage Learning, 20 Channel Center Street, Boston, MA 02210. USA
ISBN-10: 1-337-10207-5, ISBN-13: 978-1-337-10207-0

---

## Arrays

**Objective**

**In this section, you will learn about:**
* Arrays
* How an array can replace nested decisions
* Using constants with arrays
* Searching an array for an exact match
* Using parallel arrays
* Searching an array for a range match
* Remaining within array bounds
* Using a for loop to process arrays

## Arrays

**Array**
* A series or list of variables in computer memory
* All variables share the same name, and must be the same data type
* Each variable has a different subscript

## Computer Memory and Arrays

**Element: an item in the array**

**Array elements are contiguous in memory**

**Size of the array: the number of elements it will hold**

**Subscripts or indexes**
* Position number of an item in an array starting from 0 to one less than the number of elements in array
* Subscripts are always a sequence of integers
**Adding data values is called populating the array**

## Array Characteristics
**An array is a list of data items in contiguous memory locations**

**Each data item in an array is an element**

**Each array element is the same data type and the same size**

**Each element is differentiated from the others by a subscript, which is a whole number**

**Usable subscripts for an array range from 0 to one less than the number of elements in an array**

**Each array element can be used in the same way as a single item of the same data type**

## How an Array Can Replace Nested Decisions 

**The array reduces the number of statements needed**

**Six dependent count accumulators are redefined as a single array**

**Variable as a subscript to the array**

**Array subscript variable must be:**
* Numeric with no decimal places
* Initialized to 0
* Incremented by 1 each time the logic passes through the loop

**The array reduces the number of statements needed**

**Six dependent count accumulators are redefined as a single array**

**Variable as a subscript to the array**

**Array subscript variable must be:**
* Numeric with no decimal places
* Initialized to 0
* Incremented by 1 each time the logic passes through the loop

**Use constants in several ways:**
* To hold the size of an array
* As the array values
* As subscripts

**Avoid “magic numbers” (unnamed constants)**

**Declare a named numeric constant to be used every time the array is accessed**

**Make sure any subscript remains less than the constant value**

**Constants are created automatically in many languages**

**Sometimes the values stored in arrays should be constants**

**Example**
```
string MONTH[12] = "January", "February", 
"March", "April", "May", "June", "July", 
"August", "September", "October", "November", "December"
```

**Use a numeric constant as a subscript to an array**

**Example**
* Declare a named constant as: num INDIANA = 5
* Display value with:
  output salesArray[INDIANA]

**Sometimes you must search through an entire array to find a value – called a linear search**

**Example: mail-order business**
* Item numbers are three-digit, non-consecutive numbers
* Customer orders an item; check if item number is valid
* Create an array that holds valid item numbers
* Search the array for an exact match

**Flag: a variable that indicates whether an event occurred**

**Technique for searching an array**
* Set a subscript variable to 0 to start at the first element
* Initialize a flag variable to false to indicate the desired value has not been found
* Examine each element in the array
* If the value matches, set the flag to True
* If the value does not match, increment the subscript and examine the next array element

### Using Parallel Arrays

**Example: mail-order business**
* Two arrays, each with six elements
* Valid item numbers
* Valid item prices
* Each price in the valid item price array is in the same position as the corresponding item in the valid item number array

**Parallel arrays**
* Each element in one array is associated with an element in the same relative position in the other array

**Look through the valid item array for the customer’s item**
* When a match is found, get the price from the item price array

---
**ParallelArrays in Memory**
![](/01_pseudocode/assets/parallelArrays.jpg)

---

### Parallel Arrays
**Use parallel arrays when:**
* Two or more arrays contain related data
* A subscript relates the arrays
  * Elements at the same position in each array are logically related

**Indirect relationship**
* Relationship between an item’s number and its price
* Parallel arrays are very useful

### Search Efficiency
**The program should stop searching the array when a match is found**

**Set a variable to a specific value instead of letting normal processing set it**

**Leaving a loop as soon as a match is found improves efficiency**

**The larger the array, the more beneficial it becomes to do an early exit**

### Searching an Array for a Range Match
**Programmers may want to work with ranges of values in arrays, 1 through 5 or 20 through 30**

**Example: mail-order business**
* Read the customer order data; determine the discount based on the quantity ordered

**First approach**
* An array with as many elements as each possible order quantity
* Store the appropriate discount for each possible order quantity

**Drawbacks of previous approach**
* Requires a very large array; uses a lot of memory
* Stores the same value repeatedly
* How do you know when you have enough elements?
  * Customer can always order more
  
**Better approach**
* Create two parallel arrays, each with four elements
  * One array has the four discount rates
  * One array has the low end of each quantity range
* Use a loop to make comparisons

### Saying within Array Bounds
**In bounds: using a subscript that is within the acceptable range for the array**

**Out of bounds: using a subscript that is not within the acceptable range for the array**

**An invalid array subscript is a logical error**

**When an invalid subscript is used:**
* Some languages stop execution and issue an error
* Other languages access a memory location outside of the array

**The program should prevent bounds errors**

**To improve a program, add a test to ensure the entered subscript is valid**

**If entered subscript is not valid:**
* Display an error message and end the program
* Use a default value
* Continuously prompt the user for a new value until it is valid

**To improve a program, add a test to ensure the entered subscript is valid**

**If entered subscript is not valid:**
* Display an error message and end the program
* Use a default value
* Continuously reprompt the user for a new value until it is valid

### Using a *for* loop to Process an Array

**for loop: a single statement**
* Initializes the loop control variable
* Compares it to a limit
* Alters it

**The for loop is especially convenient when there is a need to process every element in the array**

**Must stay within array bounds**

**Highest usable subscript is one less than the array size**

---
### Demonstration Lab

* Design the logic for a program that allows a user to enter 20 numbers, then displays them in the reverse order of entry. b. Modify the reverse-display program so that the user can enter any amount of numbers up to 20 until a sentinel value is entered. 

* Design the logic for a program that allows a user to enter 20 numbers, then displays all of the numbers, the largest number, and the smallest. b. Modify the program in Exercise 3a so that the user can enter any amount of numbers up to 20 until a sentinel value is entered. 

---

* The Downdog Yoga Studio offers five types of classes, as shown Below:

|Class Number | Class Name |
|   :---:     |   :---:    |
| 1           | Yoga 1     |
| 2           | Yoga 2     |
| 3           | Children's Yoga|
| 4           | Prenatal Yoga|
| 5           | Senior Yoga |

* Design a program that accepts a number representing a class and then displays the name of the class. 
  * Modify the Downdog Yoga Studio program so that numeric class requests can be entered con-tinuously until a sentinel value is entered. 
  * Display each class number, name, and a count of the number of requests for each class
  
  ---

* The Jumpin Jive coffee shop charges $2 for a cup of coffee and offers the add-ins shown in the table below:

|   Product   |   Price    |
|   :---:     |   :---:    |
|Whipped Cream|0.89|
|Cinnamon|0.25|
|Chocolate Sauce|0.59|
|Amaretto|1.50|
|Irish whiskey|1.75|

* Design the logic for an application that allows a user to enter ordered add-ins continuously until a sentinel value is entered. After each 

---

* Design a program that computes pay for employees 
  * Allow a user to continuously input employee names until an appropriate sentinel value is entered 
  * Input each employee's hourly wage and hours worked
  * Compute each employee's withholding percentage using the below Table 
    * based on gross pay (hours times rate) 
    * withholding tax percentage (based on Table 64) 
    * withholding tax amount
    * net pay (gross pay minus withholding tax) 
  
| Weekly Gross Pay ($) | Withholding Percentage (%) |
|   :---:     |   :---:    |
|0.00-300.00|10|
|300.01-550.00|13|
|550.01-800.00|16|
|800.01 and up|20|
  
* Display all the results for each employee. After the last employee has been entered, display the sum of all the hours worked, the total gross payroll, the total withholding for all employees, and the total net payroll. 

---

### Exercises

**Find the Bugs:**

* Your downloadable files for Chapter 6 include DEBUG06-01.txt, DEBUG06-02. txt, and DEBUG06-03.txt. Each file starts with some comments that describe the problem. Comments are lines that begin with two slashes (//). Following the comments, each file contains pseudocode that has one or more bugs you must find and correct. 

* Your downloadable files for Chapter 6 include a file named DEBUG06-04.jpg that contains a flowchart with syntax and/or logical errors. Examine the flowchart, and then find and correct all the bugs. 

* Why does the following pseudocode not perform as indicated in the comments? 

---

```
// This program asks the user to enter a value 
// between 1 and 10 and validates the input. 
Declare Integer value 

// Get a value from the user. 
Display "Enter a value between 1 and 10." 
Input value 

// Make sure the value is between 1 and 10. 
While value < 1 AND value > 10 
    Display "ERROR: The value must be between 1 and 10." 
    Display "Enter a value between 1 and 10." 
    Input value 
End While 

```

---

### Summary

* Array: a named series or list of values in memory
  * Same data type
  * Different subscript
* Use a variable as a subscript to the array to replace multiple nested decisions
* Constants can be used to hold an array’s size
* Searching through an array requires
  * Initializing a subscript
  * Using a loop to test each element
  * Setting a flag when a match is found
* Parallel arrays: each element in one array is associated with the element in a second array
  * Elements in each array have the same relative position
* For range comparisons, store either the low- or high-end value of each range
* Access data in an array
  * Use a subscript containing a value that accesses memory within the array bounds
* A subscript is out of bounds if it is not within the defined range of acceptable subscripts
* The for loop is a convenient tool for working with arrays when processing each element of an array from beginning to end

---

**Performance Lab 6**

* Complete Performance Lab 6 before continuing to the next topic

---

|[Performance Lab 6](Labs/PseudoLab6.md)|
|---|
