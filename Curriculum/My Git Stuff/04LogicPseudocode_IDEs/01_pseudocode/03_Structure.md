|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---

![](/01_pseudocode/assets/bookCover.png)

**Information used in this lesson topic and Figures shown are from the following source:** Farrell, Joyce, Programming Logic & Design (2017), comprehensive, 9th edition. Centage Learning, 20 Channel Center Street, Boston, MA 02210. USA
ISBN-10: 1-337-10207-5, ISBN-13: 978-1-337-10207-0

---

## Understanding Structures

**Objective**

**In this section, you will learn about:**

* Unstructured spaghetti code disadvantages
* Three basic structures: sequence, selection, & loop
* Structuring a program using a priming input
* Why a structure
* Recognizing a structure
* Structuring and modularizing unstructured logic

---
## Unstructured Spaghetti Code Disadvantages

**Spaghetti code**
* Unstructured tangled web of program statements
* Often a complicated mess
* Programs often work but are difficult to read and maintain
* Confusing and prone to error (nearly impossible to debug)

**Unstructured programs**
* Do not follow the rules of structured logic

**Structured programs** 
* Follow the rules of structured logic

---
### Example: Spaghetti code - *washing a dog*

![](/01_pseudocode/assets/spaghetti1.jpg)

Programming Logic & Design (2017), 9th edition

---
## Understanding the Three Basic Structures

**Structure**
* Basic unit of programming logic 
* Three types of structure include:
  * Sequence structure
  * Selection structure (decision structure)
  * Loop structure

**any program can be constructed using one or more of these three structures**

**Sequence structure**
* Perform actions or tasks in order
* No branching or skipping any task

**Selection structure (decision structure)**
* Ask a question, take one of two actions based on testing a condition. Known as evaluating a Boolean expression, a statement that is either true or false 
* Often called if-then-else
* Dual-alternative ifs or single-alternative ifs

**Loop structure**
* Repeat actions while a condition remains true

---
## The Selection Structure

**Dual-alternative ifs**
* Contains two alternatives
* The if-then-else structure
```
if someCondition is true then
	do oneProcess
else
	do theOtherProcess 
endif
```

**Single-alternative ifs**
```
if employee belongs to dentalPlan then
	deduct $40 from employeeGrossPay 
```
* An else clause is not required

**null case**
* Circumstance where nothing is done

---
## The Loop Structure

**Loop structure**
* Repeats a set of actions while a condition remains true
  * Loop body
* Also called repetition or iteration
* Condition is tested first in the most common form of loop
* The while…do or while loop

**Loop structure**
```
while testCondition continues to be true
	do someProcess 
endwhile
while you continue to be hungry
	take another bite of food
   	determine if you still feel hungry
endwhile
```

---
## Combining Structures

**Any individual task or step in a structure can be replaced by a structure**

**Nesting structures**
* Placing one structure within another
* Indent the nested structure’s statements

**Block**
* A group of statements that execute as a single unit

**Structured programs have the following characteristics:**
* Include only combinations of the three basic structures
* Each structure has a single entry point and a single exit point
* Structures can be stacked or connected to one another only at their entry or exit points
* Any structure can be nested within another structure

---
## Using a Priming Input to Structure a Program

**Priming input (or priming read)**
* Reads the first input data record
* Is outside the loop that reads the rest of the records
* Helps keep the program structured

**Analyze a flowchart for structure one step at a time**

**Watch for unstructured loops that do not follow this order**
* First ask a question
* Take action based on the answer
* Return to ask the question again

---
## Understading "Why" Structure

**Use structured programming for:**
* Clarity—unstructured programs are confusing
* Professionalism—other programmers expect it
* Efficiency—most languages support it
* Maintenance —other programmers find it easier to read
* Modularity —easily broken down into modules

**Structured programming is sometimes called goto-less programming**

## Demonstration Labs

**Flowcharts**

In figure #1 below, the process of buying and planting flowers in the spring was shown using the same structures as the generic example in Figure #2. We will use the same logical structure as in Figure2 to create a flowchart or pseudocode that describes some other process

![](/01_pseudocode/assets/Figure1.jpg)

---

![](/01_pseudocode/assets/Figure2.jpg)

---
## Exercises

* Each of the flowchart segments in *Figure 3* are **unstructured** 

* Redraw each segment so that it does the same processes under the same conditions, but is **structured**

![](/01_pseudocode/assets/Figure3a.jpg)

![](/01_pseudocode/assets/Figure3b.jpg)

---

Assume that you have created a mechanical arm that can hold a pen. The arm can perform the following tasks:

```
* Lower the pen to a piece Of paper
* Raise the pen from the paper
* Move the pen 1 inch along a straight line. 
  * If the pen is lowered, this action draws a 1-inch line from left to right; 
  * if the pen is raised, this action just repositions the pen 1 inch to the right 
* Turn 90 degrees to the right
* Draw a circle that is 1 inch in diameter
``` 
 ---
 
* Draw a structured flowchart or write structured pseudocode describing the logic that would cause the arm to draw or write the following. Have a fellow student act as the mechanical arm and carry out your instructions. Don't reveal the desired outcome to your partner until the exercise is complete. 

  * 1-inch square
  * 2-inch by 1-inch rectangle 
  * string Of three beads 
  * short word (for example, *cat*) 
  * four-digit number

---

* Draw a structured flowchart or write pseudocode that describes the process Of guessing a number between 1 and 100. After each guess, the player is told that the guess is too high or too low. The process continues until the player guesses the correct number. Pick a number and have a fellow student try to guess it by following your instructions.
 
* Draw a structured flowchart or write structured pseudocode describing how to get from your home to your school. Include at least two decisions and two loops. 

* Draw a structured flowchart or write structured pseudocode describing how to buy a new shirt, Include at least two decisions and two loops.


**Find the bugs Activities/Labs** 

* The instructor will profide files that include DEBUG03-Ol.txt, DEBUG03-02. txt. Each file starts with some comments that describe the problem. Comments are lines that begin with two slashes (n). Following the comments, each file contains pseudocode that has one or more bugs you must find and correct.

* The instructor will profide files that include DEBUG03-04.jpg, which contains a flowchart with syntax and/or logical errors. Examine the flowchart, and then find and correct all the bugs.

* Part of the following pseudocode is incompatible with the Java, Python, C, and C++ languages. Identify the problem How would you fix the problem if you were to translate this pseudocode into one Of the aforementioned languages?

```
Module checkEquaIity (Integer numl, Integer num2)
    If num1 — num2 Then 
       Display "The values are equal. " 
    Else 
       Display "The values axe NOT equal." 
    End If 
End Module 

```
---

## Summary

**Spaghetti code**
* Statements not following the rules of structured logic

**Three basic structures**
* Sequence, selection, and loop
* Combined by stacking and nesting

**Priming input**
* Statement that reads the first input value prior to starting a structured loop

**Structured techniques promote:** 

* Clarity
* Professionalism
* Efficiency
* Modularity

**Flowcharts can be made structured by untangling logic**

**Logical steps can be rewritten to conform to the three structures: sequence, selection, and loop**

**Performance Lab3**

* Complete Performance Lab3 prior to continuing to the next topic

---

|[Performance Lab 3](Labs/PseudoLab3.md)|
|---|
