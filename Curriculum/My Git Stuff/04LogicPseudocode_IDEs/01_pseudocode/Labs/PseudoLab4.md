|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---
## Performance Lab 4

**Flowchart**

* Design a flowchart or pseudocode for a program that accepts two numbers from a user and displays one of the following messages: First is large; Second is larger, Numbers are equal. 

* Cecilia's Boutique wants several lists of salesperson data. Design a flowchart or pseudocode for the following:
  * A program that accepts one salesperson's ID number, number of items sold in the last month, and total value of the items and displays data message only if the salesperson is a high performer—defined as a person who sells more than 200 items in the month. 
  * A program that accepts the salesperson's data and displays a message only if the salesperson is a high performer—defined a person who sells more than 200 items worth at least $1,000 in the month.

* The Dash Cell Phone Company charges customers a basic rate of $5 per month to send text messages. Additional rates are as follows: 
  * The first 100 messages per month, regardless of message length, are included in the basic bill. 
  * An additional three cents are charged for each text message after the 100th message, up to and including 300 messages. 
  * An additional two cents are charged for each text message after the 300th message. 
  * Federal, state, and local taxes add a total of 14 percent to each bill. 

* Design a flowchart or pseudocode for the following: 
  * A program that accepts the following data about one customer's messages: area code (three digits), phone number (seven digits), and number of text messages sent. Display all the data, including the month-end bill both before and after taxes are added. 
  * A program that continuously accepts data about text messages until a sentinel value is entered, and displays all the details. 
  
* The Barking Lot is a dog day care center. Design a flowchart or pseudocode for the following: 
  * A program that accepts data for an ID number of a dog's owner, and the name, breed, age, and weight of the dog. Display a bill containing all the input data as well as the weekly day care fee, which is $55 for dogs weighing less than 15 pounds, $75 for dogs from 15 to 30 pounds inclusive, $105 for dogs from 31 to 80 pounds inclusive, and $125 for dogs weighing more than 80 pounds. 
  * A program that continuously accepts dogs' data until a sentinel value is entered, and displays billing data for each dog. 
  * A program that continuously accepts dogs' data until a sentinel value is entered, and displays billing data for dog owners who owe more than $100. 
  * A program that continuously accepts dogs' data until a sentinel value is entered, and displays billing data for dogs that weigh less than 20 pounds or more than 100 pounds.

* Black Dot Printing is attempting to organize carpools to save energy. Each input record contains an employee's name and town of residence. Ten percent of the company% employees live in Wonder Lake; 30 percent live in the adjacent town of Woodstock. Black Dot wants to encourage employees who live in either town to drive to work together. Design a flowchart or pseudocode for the following: 
  * A program that accepts an employee's data and displays it with a message that indicates whether the employee is a candidate for the carpool (because he lives in one of the two cities). 
  * A program that continuously accepts employee data until a sentinel value is entered, and displays a list of all employees who are carpool candidates. Make sure the decision-making process is as efficient as possible.
  * A program that continuously accepts employee data until a sentinel value is entered, and displays a list of all employees who are ineligible to carpool because they do not live in either Wonder Lake or Woodstock. Make sure the decision-making process is as efficient as possible. 

* A file named MAINTENIANCE04-01.jpg is included with your downloadable student files. Assume that this program is a working program in your organization and that it needs modifications as described in the comments (lines that begin with two slashes) at the beginning of the file. Your job is to alter the pro-gram to meet the new specifications.

* Can you find the reason that the following pseudocode function does not return the value indicated in the comments'? 

```

// The calcDiscountPrice function accepts an item's price and 
// the discount percentage as arguments. It uses those 
// values to calculate and return the discounted price. 
Function Real calcDiscountPrice(Real price, Real percentage) 
    // Calculate the discount.
    Declare Real discount = price * percentage 

    // Subtract the discount from the price. 
    Declare Real discountPrice = price - discount 
    // Return the discount price.
    Return discount 
End Function

```

* Can you find the reason that the following pseudocode does not perform as indicated in the comments?

```

// Find the error in the following pseudocode. 
Module main() 
    Declare Real value, result
    // Get a value from the user. 
    Display "Enter a value." 
    Input value 
    // Get 10 percent of the value. 
    Call tenPercent(value) 
    // Display 10 percent of the value. 
    Display "10 percent of ", value, " is ", result 
End Module 

// The tenpercent function returns 10 percent 
// of the argument passed to the function. 
Function Real tenPercent(Real num) 
    Return num * 0.1 
End Function

```

---
**End of Performance Lab 4**

---

|[Next Topic](/01_pseudocode/05_Looping.md)|
|---|
