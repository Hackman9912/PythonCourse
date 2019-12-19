|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---
 
![](/01_pseudocode/assets/bookCover.png)

**Information used in this lesson topic and Figures shown are from the following source:** Farrell, Joyce, Programming Logic & Design (2017), comprehensive, 9th edition. Centage Learning, 20 Channel Center Street, Boston, MA 02210. USA
ISBN-10: 1-337-10207-5, ISBN-13: 978-1-337-10207-0

---

## Making Decisions

**Objective**

**In this section, you will learn about:**

* Selection structure
* Relational comparison operators
* **AND** logic
* **OR** logic
* **NOT** logic
* Making selections within ranges
* Precedence when combining **AND** and **OR** operators
* case structure

---
## The Selection Structure

**Boolean expressions can be only true or false**

**Every computer decision yields a true-or-false, yes-or-no, 1-or-0 result**

**Used in every selection structure**

**Dual-alternative (or binary) selection structure**
* Provides an action for each of two possible outcomes

### The Dual-alternative Selection Structure

![](/01_pseudocode/assets/dualAlt1.jpg)

Programming Logic & Design (2017), 9th edition

**Single-alternative (or unary) selection structure**
  * Action is provided for only one outcome
  
### The Single-alternative Selection Structure

![](/01_pseudocode/assets/singleAlt2.jpg)

Programming Logic & Design (2017), 9th edition

**if-then-else decision**
* if-then clause
* Holds the action or actions that execute when the tested condition in the decision is true

**else clause**
* Executes only when the tested condition in the decision is false

---
## Using Relational Comparison Operators

**Relational comparison operators**
* Six types supported by all modern programming languages
* Two values compared can be either variables or constants but must be same data type

**Trivial expressions**
* Always evaluates to the same result

**Example:**
```
35 = 35?	TRUE
17 = 71?	FALSE
```
**Relational comparison operators**
* Equivalency operator: =
  * True when its operands are equal
* Greater-than operator: >
  * True when the left operand is greater than the right operand
* Less-than operator: <
  * True when the left operand is less than the right operand

**Relational comparison operators**
* Greater-than–or-equal-to operator: >=
  * True when the left operand is **greater** than or **equal** to the right operand
* Less-than–or-equal-to operator: <=
  * Evaluates as true when the left operand is less than or equal to the right operand
* Not-equal-to operator: <>
  * Evaluates as true when its operands are not equivalent 

---
## Understanding AND logic

**Compound condition**
* Asks multiple questions before an outcome is determined

**AND decision** 
* Requires that both of two tests evaluate to true
* Requires a nested decision (nested if) or a cascading if statement

---
## Nesting AND Decisions for Efficiency

**When nesting decisions**
* Either selection can come first

**Performance time can be improved by asking questions in the proper order**

**In an AND decision, first ask the question that is less likely to be true**
* Eliminates as many instances of the second decision as possible
* Speeds up processing time

---
## Avoiding Common Errors in an AND Selection

**Second decision must be made entirely within the first decision**

**In most programming languages, logical AND is a binary operator**
* Requires a complete Boolean expression on both sides

**Expressions should not be trivial**

---
## Understanding OR Logic

**OR decision**
* Take action when one or the other of two conditions is true

**Example:**
```
“Are you free for dinner Friday or Saturday?”
```

---
## Writing OR Selections for Efficiency

**May ask either question first**
* Both produce the same output but vary widely in number of questions asked

**If first question is true, no need to ask second**

**In an OR decision, first ask the question that is more likely to be true**
* Eliminate as many extra decisions as possible

---
## Using the OR Operator

**Conditional OR operator (simply an OR operator)**
* Ask two or more questions in a single comparison

**Only one Boolean expression in an OR selection must be true to produce a result of true**

**Question placed first will be asked first**
* Consider efficiency

**Computer can ask only one question at a time**

---
## Avoiding Common Errors in an OR Selection

**Second question must be a self-contained structure with one entry and exit point**

**Request for A and B in English logically means a request for A or B**

**Examples:**
```
“Add $20 to the bill of anyone who makes more than 100 calls and to anyone who has used more than 500 minutes”
“Add $20 to the bill of anyone who has made more than 100 calls or has used more than 500 minutes”
```

**Make sure Boolean expression are complete**

**Make sure that selections are structured**

**Make sure to use OR selections when they are required**

**Make sure that expression are not trivial**

---
## Understanding NOT Logic

**The NOT operator**
* Reverses the meaning of a Boolean expression
```
if NOT (age < 18) then
   output "Can register to vote"
Endif
```
* If NOT true, it is false
* If NOT false, it is true
* Is a unary operator
  * Takes only one operator

---
## Avoiding a Common Error in a NOT Expression

**Be careful not to create trivial expressions**

**Incorrect code:**
```
if NOT (employeeDept = 1) OR NOT (employeeDept = 2) then
    output "Employee is not in Department 1 or 2“
Endif
```

**Correct code:**
```
if NOT (employeeDept = 1 OR employeeDept = 2) then
   output "Employee is not in Department 1 or 2"
endif
```
---

## Avoiding Common Errors When Using Range Checks

**Avoid a dead or unreachable path**
* Don’t check for values that can never occur
* Requires some prior knowledge of the data

**Never ask a question if there is only one possible outcome**

**Avoid testing the same range limit multiple times**

---
## Understanding Precedence When Combining AND and OR Operators

**Combine multiple AND and OR operators in an expression**

**When multiple conditions must all be true, use multiple ANDs**

```
if score1 >= MIN_SCORE AND score2 >= MIN_SCORE AND score 3 >= MIN_SCORE then
		classGrade = "Pass"
	else 
		classGrade = "Fail"
	endif
```

**When only one of multiple conditions must be true, use multiple ORs**
```
if score1 >= MIN_SCORE OR score2 >= MIN_SCORE OR score3 >= MIN_SCORE then
		classGrade = "Pass"
	else
		classGrade = "Fail"
	endif
```

**When AND and OR operators are combined in the same statement, AND operators are evaluated first**
```
if age <= 16 OR age >= 61 AND 
 rating = "G"
```

**Use parentheses to correct logic and force evaluations to occur in the order desired**
```
if (age <= 16 OR age >= 61) 
AND rating = "G"
```
**Mixing AND and OR operators makes logic more complicated**

**Can avoid mixing AND and OR decisions by nesting if statements**

---
## Understanding the *case* Structure

**Case structure – specialized selection structure**
* Use when there are several distinct possible values for a single variable and each value requires a different subsequent action

## Demonstration Labs

**Assume that the following variables contain the values shown:**

```
numberBig = 100			wordBig = "Constitution" 
numberMedium = 10 		wordMedium = "Dance" 
numberSmall = 1  		wordSmall = "Toy" 

```

---

**Exercise**

For each of the following Boolean expressions, decide whether the statement is true, false, or illegal. 
* numberBig > numberSmall 
* numberBig < numberMedium 
* numberMedium = numberSmall 
* numberBig = wordBig 
* numberBig = "Big" 
* wordMedium > wordSmall 
* wordSmal 1 = "TOY" 
* numberBig <= 5 * numberMedium + 50 
* numberBig >= 2000
* numberBig > numberMedium + numberSmall 
* numberBig > numberMedium AND numberBig < numberSmall 
* numberBig = 100 OR numberBig > numberSmall 
* numberBig < 10 OR numberSmall > 10
* numberBig = 300 AND numberMedium = 10 OR numberSmall = 1 
* wordSmall > wordBig 
* wordSmall > wordMedium

* Design a flowchart or pseudocode for a program that accepts three numbers from a user and displays a message if the sum of any two numbers equals the third. 

* ShoppingBay is an online auction service that requires several reports. Data for each auctioned item includes an **ID number, item description, length of auction in days, and minimum required bid**. Design a flowchart or pseudocode for the following: 

  * A program that accepts data for one auctioned item. Display data for an auction only if the minimum required bid is more than $250.00. 

  ```
  start
    
  Declare Integer idNumber
  Declare Integer numDays
  Declare Real minReqBid
  Declare String itemDesc
  CONSTANT Integer MIN_BID = 250
        GetMerch()
        ReqMin()
        
  stop

    GetMerch()
        Display “ Online Auction Program”
        Display “ Enter Id: “
        Input idNumber
        Display “ Enter Description: “
        Input itemDesc
        Display “Enter Length in Days: “
        Input numdays
        Display “ Enter Minimum Bid: “
        Input minReqBid

        //output “Online Auction program”
        //input idNumber, itemDesc, numDays, minReqBid
    return

    ReqMin()
        if minReqBid > MIN_BID then
            output idNumber, itemDesc, numDays, minReqBid
        endif   
    return
  ```

  * A program that continuously accepts auction item data until a sentinel value is entered and displays all data for auctions in which the minimum required bid is more than $300.00. 

 ```
  Start
    
    Declare Integer idNumber
    Declare Integer numDays
    Declare String item Desc
    Declare Real minReqBid
    CONSTANT Integer MIN_BID = 300
      GetMerch()
      ReqMin()

  Stop

      GetMerch()
        Display "Online Auction Program"
        Display "Enter ID:"
        Input idNumber
        Display "Enter Description:"
        Input itemDesc
        Display "Enter Length in Days:
        Input numDays
        Display "Enter Minimum Bid:"
        Input minReqBid

        //output "Online Auction program"
        //input idNumber, itemDesc, numDays, minReqBid
    Return

    ReqMin()
        If minReqBid > MIN_BID then
          ouput idNumber, itemDesc, numDays, minReqBid
        Else
          CALL GetMerch() then ReqMin()
        EndIf
    Return
 ```

  

  

  * A program that continuously accepts auction item data and displays data for every auction in which there are no bids yet (in other words, the minimum bid is $0.00) and the length of the auction is seven days or less. 

  ```
  Start
    
    Declare Integer idNumber
    Declare Integer numDays
    Declare String item Desc
    Declare Real minReqBid
    CONSTANT Integer MIN_BID = 0
    CONSTANT Integer MAX_DAY = 7
      GetMerch()
      ReqMin()

  Stop

      GetMerch()
        Display "Online Auction Program"
        Display "Enter ID:"
        Input idNumber
        Display "Enter Description:"
        Input itemDesc
        Display "Enter Length in Days:
        Input numDays
        Display "Enter Minimum Bid:"
        Input minReqBid

        //output "Online Auction program"
        //input idNumber, itemDesc, numDays, minReqBid
    Return

    ReqMin()
        If minReqBid == MIN_BID AND numDays <= MAX_DAY then
          ouput idNumber, itemDesc, numDays, minReqBid
          CALL GetMerch() then ReqMin()
        EndIf
    Return
 ```

  * A program that continuously accepts auction data and displays data for every auction in which the length is between 14 and 28 days inclusive. 

  * A program that prompts the user for a maximum required bid, and then continuously accepts auction data and displays data for every auction in which the minimum bid is less than or equal to the amount entered by the user.
  

---
---

```
Start
  Declarations
      num firstNum
      num secondNum
      num thirdNum
     string MSG = "Got it!"
    GetNum()
    Calc()
    finish()
  stop

  GetNum()
    output "Enter three numbers: "
    input firsNum, secondNum, thirdNum
  return

  Calc()
    if ((firstNum + secondNum) = thirdNum) OR
       ((secondNum + thirdNum) = firstNum) OR
       ((firstNum + thirdNum) = secondNum) then
       output MSG
    endif
return
```
---
---
* The Drive-Rite Insurance Company provides automobile insurance policies for drivers. Design a flowchart or pseudocode for the following: 
  * A program that accepts insurance policy data, including a policy number, customer last name, customer first name, age, premium due date (month, day, and year), and number of driver accidents in the last three years. If an entered policy number is not between 1000 and 9999 inclusive, set the policy number to O. If the month is not between 1 and 12 inclusive, or the day is not correct for the month (for example, not between 1 and 31 for January or 1 and 29 for February), set the month, day, and year to 0. Display the policy data after any revisions have been made. 
  * A program that continuously accepts policy holders' data until a sentinel value has been entered, and displays the data for any policy holder over 40 years old. 
  * A program that continuously accepts policy holders' data until a sentinel value has been entered, and displays the data for any policy holder who is at least 18 years old. 
  * A program that continuously accepts policy holders' data and displays the data for any policy holder no more than 60 years old. 
  * A program that continuously accepts policy holders' data and displays the data for any policy holder whose premium is due no later than April 30 any year. 
  * A program that continuously accepts policy holders' data and displays the data for any policy holder whose premium is due up to and including January 1, 2018. 
  * A program that continuously accepts policy holders' data and displays the data for any policy holder whose premium is due by June 1, 2018. 
  * A program that continuously accepts policy holders' data and displays the data for anyone who has a policy number between 1000 and 4000 inclusive, whose policy comes due in September or October of any year, and who has had three or fewer accidents.

* Mark Daniels is a carpenter who creates personalized house signs. He wants an application to compute the price of any sign a customer orders, based on the following factors: 
  * The minimum charge for all signs is $30. 
  * If the sign is made of oak, add $15. No charge is added for pine. 
  * The first six letters or numbers are included in the minimum charge; there is a $3 charge for each additional character. 
  * Black or white characters are included in the minimum charge; there is an additional $12 charge for gold-leaf lettering. 

* Design a flowchart or pseudocode for the following: 
 * A program that accepts data for an order number, customer name, wood type, number of characters, and color of characters. Display all the entered data and the final price for the sign. 
 * A program that continuously accepts sign order data and displays all the relevant information for oak signs with five white letters. 
 * A program that continuously accepts sign order data and displays all the relevant information for pine signs with gold-leaf lettering and more than 10 characters. 

**Find the Bugs Activities/Labs** 

* Your downloadable files for Chapter 4 include DEBUG04-01.txt, DEBUG04-02. txt, and DEBUG04-03.txt. Each file starts with some comments that describe the problem. Comments are lines that begin with two slashes (//). Following the comments, each file contains pseudocode that has one or more bugs you must find and correct. 

* Your downloadable files for Chapter 4 include a file named DEBUG04-04.jpg that contains a flowchart with syntax and/or logical errors. Examine the flowchart, and then find and correct all the bugs.

* The programmer intends for this pseudocode to display three random numbers in the range of 1 through 7. According to the way we've been generating random numbers in this book, however, there appears to be an error. Can you find it? 

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

## Summary

* Decisions involve evaluating Boolean expressions
* Use relational operators to compare values
* An AND decision requires that both conditions be true to produce a true result
* In an AND decision, first ask the question that is less likely to be true
* An OR decision requires that either of the conditions be true to produce a true result
* In an OR decision, first ask the question that is more likely to be true

## Range check:
* Make comparisons with the highest or lowest values in each range
* Eliminate unnecessary or previously answered questions
* The AND operator takes precedence over the OR operator
* Case structure is a specialized selection structure that can be used when there are several distinct possible values for a single variable, and each value requires a different subsequent action

---
**Performance Lab 4**

* Complete Performance Lab 4 prior to continuing to the next Topic

---

|[Performance Lab 4](/01_pseudocode/Labs/PseudoLab4.md)|
|---|
