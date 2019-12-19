|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---

## Performance Lab 6

* A file named MAINTENANCE06-01.txt is included with your downloadable student files. Assume that this program is a working program in your organization and that it needs modifications as described in the comments (lines that begin with two slashes) at the beginning of the file. Your job is to alter the program to meet the new specifications.

* Why does the following pseudocode not perform as indicated in the comments? 

```

// This program gets a dollar amount from the user 
// and validates the input 
Declare Real amount 

// Get the amount from the user 
Display "Enter a dollar amount" 
Input amount 

// Make sure the amount is not less than zero. If it is... 
// get a new amount from the user 
While amount < 0 
    Display "ERROR: The dollar amount cannot be less than 0." 
    Display "Enter a dollar amount." 
End While 

```

---

* The following pseudocode works. but it performs a case-sensitive validation of the user's input How could the algorithm be improved so the user does not have to pay attention to capitalization when entering a name?

```

// This program asks the user to enter a string 
// and validates the input. 
Declare String choice

// Get the user's response. 
Display "Cast your vote for Chess Team Captain." 
Display "Would you like to nominate Lisa or Tim?" 
Input choice 

// Validate the input. 
While choice != "Lisa" AND choice != "Tim" 
Display "Please enter Lisa or Tim." 
Display "Cast your vote for Chess Team Captain." 
Display "Would you like to nominate Lisa or Tim?" 
Input response 
End While

```

---

* Design the logic for a program that allows a user to enter 20 numbers, then displays each number and its difference from the numeric average of the numbers entered. 

* Modify the program in Exercise 2a so that the user can enter any amount of numbers up to 20 until a sentinel value is entered. 

* Trainers at Tom's Athletic Club are encouraged to enroll new members. Write an application that allows Tom to enter the names of each of his 25 trainers and the number of new members each trainer has enrolled this year. Output is the number of trainers who have enrolled 0 to 5 members, 6 to 12 members, 13 to 20 members, and more than 20 members. 

* Search the web to discover the 10 most common user-selected passwords, and store them in an array. Design a program that prompts a user for a password, and continue to prompt the user until the user has not chosen one of the common passwords. 

* Design the application logic for a company that wants a report containing a breakdown of payroll by department. Input includes each employee's department number, hourly salary, and number of hours worked. The output is a list of the seven departments in the company and the total gross payroll (rate times hours) for each department. 

The department names are shown in the Table below

|Department Number |Department Name |
|   :---:     |   :---:    |
| 1 | Personnel |
| 2 | Marketing |
| 3 | Manufacturing |
| 4 | Computer Services |
| 5 | Sales |
| 6 | Accounting |
| 7 | Shipping |

---

* Daily Life Magazine wants an analysis of the demographic characteristics of its readers. The marketing department has collected reader survey records containing the age, gender, marital status, and annual income of readers. Design an application that allows a user to enter reader data and, when data entry is complete, produces a count of readers by age groups as follows: younger than 20, 20-29, 30-39, 40-49, and 50 and older.

* Modify the Daily Life Magazine program so that it produces a count of read-ers by gender within age group—that is, under-20 females, under-20 males, and so on.

* Modify the Daily Life Magazine program so that it produces a count of read-en by income groups as follows: under $30,000, $30,000–$49,999, 550,000–$69,999, and $70,000 and up. 

* Design an application in which the number of days for each month in the year is stored in an array. (For example, January has 31 days, February has 28, and so on. Assume that the year is not a leap year.) Display 12 sentences in the same format for each month; for example, the sentence displayed for January is Month 1 has 31 days. 

* Modify the months and days program to contain a parallel array that stores month names. Display 12 sentences in the same format; for example, the first sentence is January has 31 days. 

* Modify the months and days program to prompt the user for a month number and display the corresponding sentence, for example, January has 31 days.

* Prompt a user to enter a birth month and day, and continue to prompt until the day entered is in range for the month. Compute the day's numeric position in the year. (For example. February 2 is day 33.) Then, using parallel arrays, find and display the traditional Zodiac sign for the date. For example, the sign for February 2 is Aquarius.

---

**End of Performance Lab 6**

---
**This Completes the pseudocode topic**  

**Continue to Introduction to Debugging**

---

|[Introduction to Debugging](/03_Debugging/01_Intro_to_Debugging.md)|
|---|
