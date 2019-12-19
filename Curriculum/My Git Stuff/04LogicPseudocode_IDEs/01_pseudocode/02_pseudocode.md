|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---
 
![](/01_pseudocode/assets/bookCover.png)

**Information used in this lesson topic and Figures shown are from the following source:** Farrell, Joyce, Programming Logic & Design (2017), comprehensive, 9th edition. Centage Learning, 20 Channel Center Street, Boston, MA 02210. USA
ISBN-10: 1-337-10207-5, ISBN-13: 978-1-337-10207-0

---

## Pseudocode

**Objective**

**In this section, you will learn about:**
* Declaring and using variables and constants
* Performing arithmetic operations
* The advantages of modularization
* Modularizing a program
* Hierarchy charts
* Features of good program design

---

## Declaring and Using, Variables and Constants

**Understanding Data Types**
* Data type describes:
  * What values can be held by the item
  * How the item is stored in memory
  * What operations can be performed on the item

* All programming languages support these data types:
  * Numeric consists of numbers that can be used in math
  * String is anything not used in math

---

## Understanding Unnamed, Literal Constants

**There are two types of constants**

**Numeric constant (or literal numeric constant)**
* Contains numbers only
* Number does not change

**String constant (or literal string constant)**
* Also known as Alphanumeric values
* Can contain both alphabetic characters and numbers
* Strings are enclosed in quotation marks

## Working with Variables

**Variable are named memory locations** 

**Contents can vary or differ over time**

**Declaration is a statement that provides a variable's:**
* Data type 
* Identifier (variable’s name)
* Optionally, an initial value

### Flowchart and pseudocode of number-doubling program with variable declarations

![](/01_pseudocode/assets/flowchart1.jpg)

Programming Logic & Design (2017), 9th edition

---

**Casing conventions**

* Variable names that start with a lowercase character.  If a second part is added to the name it should start with an Uppercase character.  Example: **h**ourly**W**age. Commonly referred to as (Camel case)
* Variable names where the first letter in each word in uppercase such as **H**ourly**W**age (Pascal casing)
* A form of camel casing in which the data type is part of the name such as **num**HourlyWage (Hungarian casing)

**Other examples of casing types**
* Parts of variable names are separated by underscores such as hourly **_** wage (snake casing)
* Similar to snake casing, but new words start with a uppercase letter such as **H**ourly_**W**age (mixed case)
* Parts of variable names are separated by dashes such as hourly **-** wage (Kebob case)

## Assigning Values to Variables

**Assignment statement**
* set myAnswer = myNumber * 2

**Assignment operator**
* Equal sign 
* A binary operator, meaning it requires two operands—one on each side     
* Always operates from right to left, which means that it has right-associativity or right-to-left associativity
* The result to the left of an assignment operator is called an lvalue  **Example: operand2 (lvalue) = operand1 * X **

## Initializing a Variable

**Initializing the variable - declare a starting value**

```
num yourSalary = 22.57 
string yourName = “Larry”
```

**Garbage – a variable’s unknown value**

**Variables must be declared before they are used in the program**

## Declaring Named Constants

**Named constant** 
* Similar to a variable
* Can be assigned a value only once
* Assign a useful name to a value that will never be changed during a program’s execution

**Magic number** 
Unnamed constant
* Use
```
taxAmount = price * SALES_TAX_AMOUNT 
```

**instead of:**
```
taxAmount = price * .06
```

## Performing Arithmetic Operations

Standard arithmetic operators:
+ (plus sign)—addition
− (minus sign)—subtraction
* (asterisk)—multiplication
/ (slash)—division
% (percent sign)-remainder

**Rules of precedence**
* Expressed as Order of operations
* States the order in which operations are carried out
* Expressions within parentheses are evaluated first
* All the arithmetic operators have left-to-right associativity
* Multiplication and division are evaluated next
  * From left to right
* Addition and subtraction are evaluated next
  * From left to right

### Precedence & Associativity of Five Common Operators
![](/01_pseudocode/assets/precedence3.jpg)

Programming Logic & Design (2017), 9th edition

---

## Creating Hierarchy Charts

**Hierarchy chart**
* Shows the overall picture of how modules are related to one another
* Defines which modules exist within a program and which modules call others
* A Specific module may be called from locations within a program

**Planning tool** 
* Develop the overall relationship of program modules before you write them 

**Documentation tool**

### Hierachy chart of payroll report program
![](/01_pseudocode/assets/higharchy4.jpg)

Programming Logic & Design (2017), 9th edition

---
### Billing program hiearchy chart
![](/01_pseudocode/assets/higharchy5.jpg)

Programming Logic & Design (2017), 9th edition

---
## Features of Good Program Design

**Use program comments where appropriate**

**Identifiers should be chosen carefully**

**Strive to design clear statements within your programs and modules**

**Write clear prompts and echo input**

**Continue to maintain good programming habits as you develop your programming skills**

## Maintaining Good Programming Habits

**Every program you write will be better if you:** 
* Plan prior to coding
* Continue to draw flowcharts or write pseudocode
* Draft your program logic on paper
* Think carefully about the variable and module names you use
* Design your program statements for ease of reading and use

## Demonstration Labs

* Explain why each of the following names does or does not seem like a good variable name to represent a state sales tax rate. 
  * stateTaxRate: **Good but Maybe a bit vague. What kind of tax?**
  * txRt: **bad because too cryptic**
  * t: **bad, too short, no definition**
  * stateSalesTaxRateValue: **Decent, maybe too long.**
  * taxRate: **same a the stateTaxRate**
  * 1TaxRate: **Bad, starts with a number**
  * moneyCharged: **decent, depends on the usage of the program could be confusing**
  
* If productCost and productPrice are numeric variables, and productName is a string variable, which of the following statements are valid assignments? If a statement is not valid, explain why not.
  * productCost = 100 >**good**
  * productPrice = productCost >**good**
  * productPrice = productName >**bad, cannot go string to number**
  * productPrice = “24.95” >**bad, quotes make a string**
  * 15.67 = productCost >**bad syntax should be right to left**
  * productCost = productPrice – 10 >**valid**
  * productName = “mouse pad” >**valid**
  * productCost + 20 = productPrice >**operations must occur after equals sign**
  * productName = 3-inch nails >**no quotes so bad**
  * productName = 43 >**no, it needs quotes**
  * productName = productCost >**productName is a string productCost is a number**
  
* Draw a typical hierarchy chart for a program that produces a monthly bill for a cellphone customer.  Try to think of at least 10 separate modules that might be included. For example, one module might calculate the charge for daytime phone minutes used.


* Draw the hierarchy chart and then plan the logic for a program that calculates a person’s body mass index (BMI). BMI is a statistical measure that compares a person’s body mass index (BMI). BMI is a statistical measure that compares a person’s weight and height.  The program uses three modules.  The first prompts a user for and accepts the user’s hight in inches. The second module accepts the user’s weight in pounds and converts the user’s height to meters and weight to kilograms. Then, it calculates BMI as weight in kilograms divided by height in meters squared, and displays the results.  There are 2.54 centimeters in an inch, 100 centimeters in a meter, 453.59 grams in a pound, and 1,000 grams in a kilogram.  Use named constants whenever you think they are appropriate. The last module displays the message *End of job.*

* Revise the BMI-determining program to execute continuously until the user enters ) for the height in inches.

* Draw the hierachy chart and design the logic for a program that calculates teh projected cost of a remodeling project.  Assume that the labor cost is $30 per hour. Design a program that prompts the user for a number hours projected for the job, which is the number of hourstimes the hourly rate plus the 120% of the wholesale cost of materials.  The program accepts data continuously until 0 is entered for the number of hours. Use appropriate modules, including one that displays *End of program* when the program is finished. 

* Draw the hierarchy chart and design the logic for a program for Arnie's Appliances.  Design a program that prompts the user for a refrigerator model nmae and the interior height, width, and depth in inches.  Calculate the refrigerator capacity in cubic feet by first multiplying the height, width, and depth to get cubic inches, and then dividing by 1728 (the number of cubic inches in cubic foot). The program accepts model names continuoulsly until "XXX" is entered. Use named constants  where appropriate. Also use modules, including one that displays *End of job* after the sentinel is entered for the model name.

---
## Practice Exercises

**Find The Bugs**

Your files for this will be provided by the instructor.  They include; DEBUG02-01.txt, DEBUG02-02.txt, and DEBUG02-03.txt.  Each file starts with some comments that describe the problem.  Comments are lines that begin with two slashes (//). Following the comments, each file contains pseudocode that has one or more bugs you must find and correct.

Your files for this will be provided by the instructor.  They include; DEBUG02-04.jpg that contains a flowchart with syntax and/or logical errors.  Examine the flowchart, and then find and correct all of the bugs.


* Find the error in the following pseudocode
```
Module main()
    Declare Real mileage
    call getMileage()
    Display "You've driven a total of ", mileage, " miles."
End Module

Module getMileage()
    Display "Enter your vehicle's mileage."
    Input mileage
End Module
````

---

* Find the potential error in the following pseudocode.

```
Module manin()
    Call squareNumber(5)
End Module

Module squareNumber(Integer Ref number)
    Set number = number^2
    Display number
End Module
```

---

## Summary
* Programs contain literals, variables, and named constants
* Arithmetic follows rules of precedence
* Break down programming problems into modules
* Include a header, a body, and a return statement
* Hierarchy charts show relationship among modules
* As programs become more complicated: 
* Need for good planning and design increases

---

**Performance Lab 2**

* Continue to Performance Lab 2 prior to continuing to the next topic.

---

---

|[Performance Lab 2](Labs/PseudoLab2.md)|
|---|

