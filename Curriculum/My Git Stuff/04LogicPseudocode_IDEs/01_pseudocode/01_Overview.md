|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---

![](/01_pseudocode/assets/bookCover.png)

**Information used in this lesson topic and Figures shown are from the following source:** Farrell, Joyce, Programming Logic & Design (2017), comprehensive, 9th edition. Centage Learning, 20 Channel Center Street, Boston, MA 02210. USA
ISBN-10: 1-337-10207-5, ISBN-13: 978-1-337-10207-0

---

## Pseudocode Overview

**Objectives**

**In this chapter, you will learn about:**
* Computer systems
* Program logic
* Program development cycle process
* Pseudocode statements and flowchart symbols
* Sentinel value to end programs
* Programming and user environments
* Programming models

---

### Understanding Computer Systems

**Computer system**
* Combination of hardware and software components, that communicate with each other and externally,  required to process and store data using a computer

**Hardware**
* Physical ,tangibles parts or components (equipment) used to  with a computer
  
**Software**
* A set of data or computer instructions that tells the computer how to work
* Programs
  *A collection of Instructions written by programmers that performs a specific task when executed by a computer
* Programming
  * The process of taking an algorithm or a programming languages code and using it to write software instructions
* Application software such as word processing, spreadsheets, payroll and inventory, even games, app
* System software such as operating systems like Windows, Linux, or UNIX, Google Android and Apple IOS

---
**Computer hardware and software accomplish three major operations**
* Input
  * Data items such as text, numbers, images, and sound
* Processing
  * Calculations and comparisons performed by the central processing unit (CPU)
* Output 
  * Resulting information that is sent to a printer, a monitor, or storage devices after processing
  * A cloud based device is accessed through the Internet

**Programming language**
* Used to write computer instructions called program code
* Writing instructions is called coding the program
* Examples
  * Visual Basic, C#, C++, or Java
  
**Syntax**
* a set of rules specific to a language, governing programming language usage, arithmatic, and punctuation
* Mistakes in a language’s usage are syntax errors

**Computer memory**
* Computer’s temporary, internal storage – random access memory (RAM)
* Volatile memory – lost when the power is off

---

**Permanent storage devices**
* Nonvolatile memory

**Compiler or interpreter**
* Translates source code into machine language (binary language) statements called object code
* Checks for syntax errors

**Program executes or runs**
* Input will be accepted, some processing will occur, and results will be output

**Programs with syntax errors cannot execute**

---

**Logical errors**
* Errors in program logic produce incorrect output

**Logic of the computer program**
* Sequence of specific instructions in specific order

**Variable** 
* Named memory location whose value can vary

---

### Understanding the Program Development Cycle

**Program development cycle**
* Understand the problem
* Plan the logic
* Code the program
* Use software (a compiler or interpreter) to translate the program into machine language
* Test the program
* Put the program into production
* Maintain the program

---

   ## Program Development Cycle

![](/01_pseudocode/assets/Dev_Cycle.jpg)

Programming Logic & Design (2017), 9th edition

---
## Using Software to Translate the Prgram into Machine Language

![](/01_pseudocode/assets/machLang.png)

Programming Logic & Design (2017), 9th edition

---

### Statements and Flowchart Symbols

**Pseudocode**
* English-like representation of the logical steps it takes to solve a problem

**Flowchart**
* Pictorial representation of the logical steps it takes to solve a problem

## Writing Pseudocode

**Pseudocode representation of a number-doubling problem**

```
start
   input myNumber
   set myAnswer = myNumber * 2
   output myAnswer
stop

```

## Pseudocode Standards

* Programs begin with the word start and end with the word stop; these two words are always aligned
* Whenever a module name is used, it is followed by a set of parentheses
* Modules begin with the module name and end with return.  The module name and return are always aligned
* Each program statement performs one action

**Example** input, processing, or output
* Program statements are indented a few spaces more than the word start or the module name
* Each program statement appears on a single line if possible. When this is not possible, continuation lines are indented
* Program statements begin with lowercase letters
* No punctuation is used to end statements
---

## Drawing Flowcharts

**Create a Flowchart**
* Draw geometric shapes that contain the individual statements
* Connect shapes with arrows

**Input Symbol**
* Indicates input operation
* Parallelogram

![](/01_pseudocode/assets/input1.jpg)

**Processing symbol**
* Contains processing statements such as arithmetic
* Rectangle

![](/01_pseudocode/assets/mynumb2.jpg)

**Output symbol**
* Represents output statements
* Parallogram

![](/01_pseudocode/assets/MyAnsw3.jpg)

**Flowlines**
* Arrows that connect steps

**Terminal symbols**
* Start/stop symbols
* Shaped like a racetrack
* Called lozenges

![](/01_pseudocode/assets/StartStop4a.png)

![](/01_pseudocode/assets/flowChartDoub.png)

Programming Logic & Design (2017), 9th edition

---

## End a Program

**Making a Decision**
* Testing a value
* Decision symbol
  * Diamond shape
  
**Dummy value**
* Data-entry value that the user will never need
* Sentinel value

**End of File (eof)**
* Marker at the end of a file that automatically acts as a sentinel

![](/01_pseudocode/assets/flowChartSent.png)

Programming Logic & Design (2017), 9th edition

---

## Demonstration Labs

**Flowcharts**

* Draw a flowchart or write pseudocode to represent the logic of a program that allows the user to enter a value.  The program multiplies the value by 10 and outputs the result.

* Draw a flowchart or write pseudocode to represent the logic of a program that allows the user to enter a value for hours worked in a day.  The program calculates the hours worked in a five-day week and the hours worked in a 252- day work year.  The program outputs all the results.

* Draw a flowchart or write pseudocode to represent the logic of a program that allows the user to enter values for the current year and the user's birth year.  The program outputs the age of the user this year.

**Find the Bugs**

Since the early days of computer programming, program errors have been called bugs.  The term is often said to have origiated from an actual moth that was discovered trapped in the circuitry of a computer at Harvard University in 1945.  Actually, the term *bug* was in use prior to 1945 to mean trouble with any electrical apparatus; even during Thomas Edison's life, it meant an indusrial defect.  The term *debugging*, however, is more closely associated with correcting program syntax and logic errors than with any other type of trouble.

* Your provided files include DEBUG01-01.txt, DEBUG01-02.txt, DEBUG01-03.txt. Each file starts with some comments (lines that begin with two slashes) that describe the program. Examine the pseudocode that follows the introductory comments, and then find and correct all the bugs. 

* Your provided file includes a file named DEBUG01.04.jpg that contains a flowchart with syntax and/or logical errors.  Examine the flowchart, and then find and correct all the bugs.

* If the follwoing pseudocode were a actual program, why would it not display the output that the programmer expects?

```
  Declare String favoriteFood
  
  Display "What is the name of your favorite food?"
  Input favoriteFood
  
  Display "Your favorite food is "
  Display "favoriteFood"
  
 ```
 
 ---
 
 ## Summary

* Hardware and software accomplish input, processing, and output

* Logic must be developed correctly

* Logical errors are much more difficult to locate than syntax errors

* Use flowcharts and pseudocode to plan the logic

* Avoid infinite loops by testing for a sentinel value

* Use a text editor or an IDE to enter your program statements
---

## Performance Lab

* Please complete the instructor provided **Performance Labs 1**

|[Performance Lab 1](Labs/PseudoLab1.md)|
|---|
