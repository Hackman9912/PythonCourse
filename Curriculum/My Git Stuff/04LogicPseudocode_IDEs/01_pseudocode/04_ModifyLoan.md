
For example, consider a program that determines whether a bank customer qualifies for a loan. To qualify, two conditions must exist: (1) the customer must earn at least $30,000 per year, and (2) the customer must have been employed at his or her current job for at least two years. Figure 4-15 shows a flowchart for an algorithm that could be used in such a program. Assume that the salary variable contains the customer’s annual salary, and the yearsOnJob variable contains the number of years that the customer has worked on his or her current job.

If we follow the flow of execution, we see that the condition salary >= 30000 is tested. If this condition is false, there is no need to perform further tests; we know that the customer does not qualify for the loan. If the condition is true, however, we need to test the second condition. This is done with a nested decision structure that tests the condition yearsOnJob >= 2. If this condition is true, then the customer qualifies for the loan. If this condition is false, then the customer does not qualify. Program 4-5 shows the pseudocode for the complete program.

Figure 4-15 A nested decision structure

![image](https://user-images.githubusercontent.com/47218880/67347297-430ccf80-f507-11e9-8089-093774b868d4.png)

##  Program 4-5
```
 1  // Declare variables
 2  Declare Real salary, yearsOnJob
 3
 4  // Get the annual salary.
 5  Display "Enter your annual salary."
 6  Input salary
 7
 8  // Get the number of years on the current job.
 9  Display "Enter the number of years on your"
10  Display "current job."
11  Input yearsOnJob
12
13  // Determine whether the user qualifies.
14  If salary >= 30000 Then
15     If yearsOnJob >= 2 Then
16        Display "You qualify for the loan."
17     Else
18        Display "You must have been on your current"
19        Display "job for at least two years to qualify."
20     End If
21  Else
22     Display "You must earn at least $30,000"
23     Display "per year to qualify."
24  End If
```
# Program Output (with Input Shown in Bold)
Enter your annual salary.
##  35000 [Enter] 
Enter the number of years on your
current job.
## 1 [Enter] 
You must have been on your current
job for at least two years to qualify.
# Program Output (with Input Shown in Bold)
Enter your annual salary.
## 25000 [Enter] 
Enter the number of years on your
current job.
## 5 [Enter] 
You must earn at least $30,000
per year to qualify.
# Program Output (with Input Shown in Bold)
Enter your annual salary.
## 35000 [Enter] 
Enter the number of years on your
current job.
## 5 [Enter] 
You qualify for the loan.


# The Loan Qualifier Program Revisited
In some situations the AND operator can be used to simplify nested decision structures. For example, recall that the loan qualifier program in Program 4-5 uses the following nested If-Then-Else statements:
```
If salary >= 30000 Then
    If yearsOnJob >= 2 Then
       Display "You qualify for the loan."
    Else
       Display "You must have been on your current"
       Display "job for at least two years to qualify."
    End If
Else
    Display "You must earn at least $30,000"
    Display "per year to qualify."
End If
```
The purpose of this decision structure is to determine that a person’s salary is at least $30,000 and that he or she has been at his or her current job for at least two years. Program 4-9 shows a way to perform a similar task with simpler code.

# Program 4-9
```
 1  // Declare variables
2  Declare Real salary, yearsOnJob
3
 4  // Get the annual salary.
5  Display "Enter your annual salary."
6  Input salary
7
 8  // Get the number of years on the current job.
9  Display "Enter the number of years on your ",
10          "current job."
11  Input yearsOnJob
12
13  // Determine whether the user qualifies.
14  If salary >= 30000 AND yearsOnJob >= 2 Then
15     Display "You qualify for the loan."
16  Else
17     Display "You do not qualify for this loan." 
18  End If
```
# Program Output (with Input Shown in Bold)
Enter your annual salary.
## 35000 [Enter] 
Enter the number of years on your current job.
## 1 [Enter] 
You do not qualify for this loan.
# Program Output (with Input Shown in Bold)
Enter your annual salary.
## 25000 [Enter] 
Enter the number of years on your current job.
## 5 [Enter] 
You do not qualify for this loan.
# Program Output (with Input Shown in Bold)
Enter your annual salary.
## 35000 [Enter] 
Enter the number of years on your current job.
## 5 [Enter] 
You qualify for the loan.

The If-Then-Else statement in lines 14 through 18 tests the compound expression salary >= 30000 AND yearsOnJob >= 2. If both subexpressions are true, the compound expression is true and the message “You qualify for the loan” is displayed. If either of the subexpressions is false, the compound expression is false and the message “You do not qualify for this loan” is displayed.

 ### NOTE:
 
A careful observer will realize that Program 4-9 is similar to Program 4-5, but it is not equivalent. If the user does not qualify for the loan, Program 4-9 displays only the message “You do not qualify for this loan,” whereas Program 4-5 displays one of two possible messages explaining why the user did not qualify.

# Yet Another Loan Qualifier Program
Suppose the bank is losing customers to a competing bank that isn’t as strict about whom it loans money to. In response, the bank decides to change its loan requirements. Now, customers have to meet only one of the previous conditions, not both. Program 4-10 shows the pseudocode for the new loan qualifier program. The compound expression that is tested by the If-Then-Else statement in line 14 now uses the OR operator.

# Program 4-10
```
1  // Declare variables
 2  Declare Real salary, yearsOnJob
 3
 4  // Get the annual salary.
 5  Display "Enter your annual salary."
 6  Input salary
 7
 8  // Get the number of years on the current job.
 9  Display "Enter the number of years on your"
10  Display "current job."
11  Input yearsOnJob
12
13  // Determine whether the user qualifies.
14  If salary >= 30000 OR yearsOnJob >= 2 Then
15     Display "You qualify for the loan."
16  Else
17     Display "You do not qualify for this loan." 
18  End If
```
# Program Output (with Input Shown in Bold)
Enter your annual salary.
## 35000 [Enter] 
Enter the number of years on your 
current job.
## 1 [Enter]
You qualify for the loan.
# Program Output (with Input Shown in Bold)
Enter your annual salary.
## 25000 [Enter] 
Enter the number of years on your
current job.
## 5 [Enter]
You qualify for the loan.
# Program Output (with Input Shown in Bold)
Enter your annual salary.
## 12000 [Enter] 
Enter the number of years on your
current job.
## 1 [Enter] 
You do not qualify for this loan.










