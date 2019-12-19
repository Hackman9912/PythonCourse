|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---
 
![](/01_pseudocode/assets/bookCover.png)

**Information used in this lesson topic and Figures shown are from the following source:** Farrell, Joyce, Programming Logic & Design (2017), comprehensive, 9th edition. Centage Learning, 20 Channel Center Street, Boston, MA 02210. USA
ISBN-10: 1-337-10207-5, ISBN-13: 978-1-337-10207-0

---

## Looping

**Objective**

**In this section, you will learn about:**
* Looping advantages
* Loop control variable
* Nested loops
* Common loop mistakes
* for loops
* Using a posttest loop
* Characteristics shared by structured loops
* Common loop applications
* Similarities and differences between selections and loops

### Advantages of Looping

**Looping makes computer programming efficient and worthwhile**

**Write one set of instructions to operate on multiple, separate sets of data**
* Less time required for design and coding
* Fewer errors
* Shorter compile time
  
**Loop: a structure that repeats actions while some condition continues**

### Loop Control Variable

**As long as a condition remains true, the statements in a while loop’s body execute**

**Control number of repetitions**
* Loop control variable initialized before entering loop
* Loop control variable tested
* Body of loop must alter value of loop control variable
  
**Repetitions controlled by:**
* Counter – used to create a definite counter-controlled loop
* Sentinel value – used to create an indefinite loop

### Indefinite Loop with a Sentinel Value

**Indefinite loop**
* Performed a different number of times each time the program executes
* The user decides how many times the loop executes

![](/01_pseudocode/assets/indefLoop.png)

Programming Logic & Design (2017), 9th edition

---

### Understanding the Loop in a Program’s Mainline Logic

**Three steps should occur in every properly functioning loop:**
* Provide a starting value for the variable that will control the loop
* Test the loop control variable to determine whether the loop body executes
* Alter the loop control variable within the loop

### Nested Loops

**Nested loops: loops within loops**

**Outer loop: the loop that contains the other loop**

**Inner loop: the loop that is contained**

**Needed when values of two (or more) variables repeat to produce every combination of values**

**Nested Loop facts:**

* Nested loops never overlap. An inner loop is always completely contained within an outer loop
* An inner loop goes through all of its iterations each time its outer loop goes through just one iteration
* The total number of iterations executed by a nested loop is the number of inner loop iterations times the number of outer loop iterations

### Loop Mistakes

**Mistake: using the wrong comparison when testing loop control variable**
* Programmers must use correct comparison
* Seriousness depends on actions performed within a loop
  * Overcharge insurance customer by one month
  * Overbook a flight on airline application 
  * Dispense extra medication to patients in pharmacy

### for Loop

**for statement or for loop is a definite loop**

**Provides three actions in one structure:**
* Initializes
* Tests
* Alters

**Comparable while and for statements that output Hello 4 times**

```
count = 0		|	for count = 0 to 3 step 1
while count <= 3	|	    output "Hello"
    output "Hello"	|	endfor
    count = count +1	|
endwhile		|

```

**Example:**

```
for count = 0 to 3 step 1
    output "Hello"
endfor

```
**Initializes count variable to 0**

**Checks count variable against the limit value 3**

**If evaluation is true, for statement body prints the word “Hello”**

**Increases count by 1 using a step value**

**Step value: the amount by which a loop control variable changes**
* Can be positive or negative (incrementing or decrementing the loop control variable)
* Default step value is 1
* Programmer specifies a step value when each pass through the loop changes the loop control variable by a value other than 1

**while statement could be used in place of for statement**

**Pretest loop: the loop control variable is tested before each iteration**
* for loops and while loops are pretest loops

### Recognizing Structured Loop characteristics

**All structured loops have these characteristics:**
* The loop-controlling evaluation must provide either the entry to or exit from the structure
* The loop-controlling evaluation provides the only entry to or exit from the structure

**Some languages support a do-until loop, which is a posttest loop that iterates until the loop controlling evaluation is false**

### Common Loop Applications

**Using a loop to accumulate totals**
* Examples
  * Business reports often include totals
  * List of real estate sold and total value
  
**Accumulator: variable that gathers values**
* Similar to a counter
  * Counter increments by 1
  * Accumulator increments by some value

**Accumulators require three actions**
* Initialize the accumulator to 0
* Accumulators are altered: once for every data set processed
* At the end of processing, accumulators are output

**Summary reports**
* Contain only totals with no detail data
* Loops are processed but detail information is not printed

**Using a loop to validate data**
* Defensive programming: preparing for all possible errors before they occur
  * When prompting a user for data, no guarantee that data is valid
* Validate data: make sure data falls in acceptable ranges (month values between 1 and 12)
* GIGO: Garbage in, garbage out
  * Unvalidated input will result in erroneous output

**Limiting a reprompting loop**
* Reprompting can be frustrating to a user if it continues indefinitely
* Maintain a count of the number of reprompts
* Forcing a data item means: 
  * Override incorrect data by setting the variable to a specific value

**Validating a data type**
* Validating data requires a variety of methods
* isNumeric() or similar method
  * Provided with the language translator you use to write your programs
  * Black box
* isChar() or isWhitespace() or isUpper()
* Accept user data as strings
* Use built-in methods to convert to correct data types

**Validating reasonableness and consistency of data**
* Many data items can be checked for reasonableness
* Good defensive programs try to foresee all possible inconsistencies and errors

### Demonstration Labs

**Design the logic for a program**

* Design the logic for a program for each of the following that:
  * Outputs every number from 1 through 15.
  * Outputs every even number from 2 through 200. 
  * Allows a user to enter a number. Display the sum of every number from 1 through the entered number. 
  * 
  
* Design a program that allows a user to enter any quantity of numbers until a negative number is entered. Then display the highest number and the lowest number. 
  
* Design a program for Hunterville College. The current tuition is $20,000 per year, and tuition is expected to increase by 3 percent each year. Display the tuition each year for the next 10 years.
  * Modify the Hunterville College program so that the user enters the rate of tuition increase instead of having it fixed at 3 percent.

--- 

### Exercise

**Find the bugs**

* Your downloadable files for Chapter 5 include DEBUG05-01.txt, DEBUG05-02. txt, and DEBL/G05-03.txt. Each file starts with some comments that describe the problem. Comments are lines that begin with two slashes (//). Following the comments, each file contains pseudocode that has one or more bugs you must find and correct. 

* Your downloadable files for Chapter 5 include a file named DEBUG05-04.jpg that contains a flowchart with syntax and/or logical errors. Examine the flowchart, and then find and correct all the bugs. 

* The programmer intends for this pseudocode to display three random numbers in the range of 1 through 7. According to the way we've been generating random numbers in this book, however. there appears to be an error. Can you find it? 

```
// This program displays three random numbers 
// in the range of 1 through 7. 
Declare Integer count 
// Display three random numbers. 
For count = 1 To 3 
Display random(7, 1) 
End For 

```

---

### Summary

* Loops write one set of instructions that operate on multiple, separate sets of data
* Three steps must occur in every loop
  * Initialize the loop control variable
  * Compare the variable to some value
  * Alter the variable that controls the loop
* Nested loops: loops within loops
* Nested loops maintain two individual loop control variables
  * Alter each at the appropriate time
* Common mistakes made by programmers
  * Neglecting to initialize the loop control variable
  * Neglecting to alter the loop control variable
  * Using the wrong comparison with the loop control variable
  * Including statements inside the loop that belong outside the loop
* Most computer languages support a for loop 
  * for loop used when the number of iterations is known
* In a posttest loop, the loop body executes at least one time because the loop control variable is not tested until after the first iteration
* Loops are used to accumulate totals in business reports and to prompt users for valid data
* In the selection structure the two logical paths that emerge from a test join together following their actions
* In the loop structure, the paths that emerge from the test do not join together, instead, one of the paths eventually returns to the same test

---

**Performance Lab 5**

* Complete performance lab 5 before continuing to the next Topic

---

|[Performance Lab 5](Labs/PseudoLab5.md)|
|---|
