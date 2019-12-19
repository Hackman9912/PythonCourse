|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---

## Performance Lab 5

* Design the logic for a program for each of the requirements below that:
  * Outputs every number from 1 through 15 along with its value times 10 and times 100 
  * Outputs numbers in reverse order from 10 down to 0 
  * Allows a user to continuously enter numbers until the user enters 0. Display the sum of the numbers entered

* Design an application for Bob's E-Z Loans. The application accepts a client's loan amount and monthly payment amount. Output the customer's loan balance each month until the loan is paid off. 

* Modify the Bob's E-Z Loans application so that after the payment is made each month, a finance charge of 1 percent is added to the balance. 

* Design a retirement planning calculator for Skulling Financial Services. Allow a user to enter a number of working years remaining in the user's career and the annual amount of money the user can save. Assume that the user earns 3 percent simple interest on savings annually. Program output is a schedule that lists each year number in retirement starting with year 0 and the user's savings at the start of that year. Assume that the user spends $60,000 per year in retirement and then earns 3 percent interest on the remaining balance. End the list after 30 years, or when the user's balance is 0 or less, whichever comes first. 

* A file named MAINTENANCE05-01.txt is included with your downloadable stu-dent files. Assume that this program is a working program in your organization and that it needs modifications as described in the comments (lines that begin with two slashes) at the beginning of the file. Your job is to alter the program to meet the new specifications. 

* Can you find the reason that the following pseudocode function does not return the value indicated in the comments? 

```
// The calcDiscountPrice function accepts an item's price and 
// the discount percentage as arguments. It uses those 
// values to calculate and return the discounted price. 
Function Real calcDiscountPrice (Real price, Real percentage) 
    // Calculate the discount. 
    Declare Real discount = price * percentage 
    
    // Subtract the discount from the price.
    Declare Real discountPrice = price - discount 

    // Return the discount price. 
    Return discount 
End Function

```

---

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

// The tenPercent function returns 10 percent 
// of the argument passed to the function. 
Function Real tenPercent(Real num) 
    Return num * 0.1 
End Function

```

---

**End of Performance Lab 5**

---

|[Next Topic](/01_pseudocode/06_Arrays.md)|
|---|
