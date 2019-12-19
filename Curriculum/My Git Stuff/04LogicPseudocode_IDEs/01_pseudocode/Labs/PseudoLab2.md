|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---

## PseudoLab2

**Draw hierarchy Charts**

* Draw the hierarchy chart and then plan the logic for a program needed by Hometown Bank.  The program determines a monthly checking account fee. Input includes an account balance and the number of times the account was overdrawn. The output is the fee, which is 1 percent of the balance minus 5 dollars for each time the account was overdrawn. Use three modules. The main program declares global variables and calls housekeeping, detail, and end-of-job modules. The housekeeping module prompts for and accepts a balances. The detail module prompts for and accepts the number of overdrafts, computes the fee, and displays the result. The end-of-job module displays the message Thanks for using this program. 

* Revise the banking program so that it runs continuously for any number of accounts. The detail loop executes continuously while the balance entered is not negative; in addition to calculating the fee, it prompts the user for and gets the balance for the next account. The end-of-job module executes after a number less than 0 is entered for the account balance.

* Draw the hierarchy chart and design the logic for a program that calculates service charges for Hazel's Housecleaning service. The program contains housekeeping, detail loop, and end-of-job modules. The main program declares any needed global variables and constants and calls the other modules. The housekeeping module displays a prompt for and accepts a customer's last name. While the user does not enter ZZZZ for the name, the detail loop accepts the number of bathrooms and the number of other rooms to be cleaned. The service charge is computed as $40 plus $15 for each bathroom and $10 for each of the other rooms. The detail loop also displays the service charge and then prompts the user for the next customer's name. The end-of-job module, which executes after the user enters the sentinel value for the name, displays a message that indicates the program is complete. 

* Draw the hierarchy chart and design the logic for a program needed by the manager of the Stengel County softball team, who wants to compute slugging percentages for his players. A slugging percentage is the total bases earned with base hits divided by the player's number of at-bats. Design a program that prompts the user for a player jersey number, the number of bases earned, and the number of at-bats, and then displays all the data, including the calculated slugging average. The program accepts players continuously until 0 is entered for the jersey number. Use appropriate modules, including one that displays End of job after the sentinel is entered for the jersey number. 

* Modify the slugging percentage program to also calculate a player's on-base percentage. An on-base percentage is calculated by adding a player's hits and walks, and then dividing by the sum of at-bats, walks, and sacrifice flies. Prompt the user for all the additional data needed, and display all the data for each player.

---

**Find the Errors**

* Find the error in the following pseudocode

```
Module main() 
    Call getCalories() 
End Module 


Module getCalories() 
    Declare Real calories 
    Display "How many calories are in the first food?" 
    Input calories 
    Declare Real calories 
    Display "How many calories are in the second food?" 
    Input calories 
End Module 

```

* Find the error in the following pseudocode
```
Module main()  
    Call raiseToPower(2, 1.5) 
End Module 


Module raiseToPower(Real value, Integer power)  
    Declare Real result 
    Set result = valueApower 
    Display result 
End Module
```

---

**End of Lab2**

---

|[Next Topic](/01_pseudocode/03_Structure.md)|
|---|
