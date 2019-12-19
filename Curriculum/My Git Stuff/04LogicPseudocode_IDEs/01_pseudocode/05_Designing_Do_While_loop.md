# Designing a Do-While Loop

Samantha owns an import business and she calculates the retail prices of her products with the following formula:

![image](https://user-images.githubusercontent.com/47218880/67348497-be23b500-f50a-11e9-91a5-443a84884641.png)

She has asked you to design a program to do this calculation for each item that she receives in a shipment. You learn that each shipment contains various numbers of items, so you decide to use a loop that calculates the price for one item, and then asks her whether she has another item. The loop will iterate as long as she indicates that she has another item. Program 5-6 shows the pseudocode for the program, and Figure 5-9 shows the flowchart.

3 Program 5-6
```
 1  Module main()
 2     // Local variable
 3     Declare String doAnother
 4
 5     Do
 6        // Calculate and display a retail price.
 7        Call showRetail()
 8
 9        // Do this again?
10        Display "Do you have another item? (Enter y for yes.)"
11        Input doAnother
12     While doAnother == "y" OR doAnother == "Y"
13  End Module
14
15  // The showRetail module gets an item's wholesale cost
16  // from the user and displays its retail price.
17  Module showRetail()
18     // Local variables
19     Declare Real wholesale, retail
20
21     // Constant for the markup percentage
22     Constant Real MARKUP = 2.50
23
24     // Get the wholesale cost.
25     Display "Enter an item's wholesale cost."
26     Input wholesale
27
28     // Calculate the retail price.
29     Set retail = wholesale * MARKUP
30
31     // Display the retail price.
32     Display "The retail price is $", retail
33  End Module
```
# Program Output (with Input Shown in Bold)
Enter an item's wholesale cost.
## 10.00 [Enter] 
The retail price is $25
Do you have another item? (Enter y for yes.)
## y [Enter] 
Enter an item's wholesale cost.
## 15.00 [Enter] 
The retail price is $37.50
Do you have another item? (Enter y for yes.)
## y [Enter] 
Enter an item's wholesale cost.
## 12.50 [Enter] 
The retail price is $31.25
Do you have another item? (Enter y for yes.)
## n [Enter]

![image](https://user-images.githubusercontent.com/47218880/67348845-d0eab980-f50b-11e9-880d-f03cb66a24e7.png)

Figure 5-9 Flowchart for Program 5-6

This program has two modules: main, which executes when the program runs, and showRetail, which calculates and displays an item’s retail price. In the main module, a Do-While loop appears in lines 5 through 12. In line 7, the loop calls the showRetail module. Then, in line 10 the user is prompted “Do you have another item? (Enter y for yes.)” In line 11, the user’s input is stored in the doAnother variable. In line 12, the following statement is the end of the Do-While loop:

While doAnother == "y" OR doAnother == "Y"
Notice that we are using the logical OR operator to test a compound Boolean expression. The expression on the left side of the OR operator will be true if doAnother is equal to lowercase "y". The expression on the right side of the OR operator will be true if doAnother is equal to uppercase "Y". If either of these subexpressions is true, the loop will iterate. This is a simple way to make a case insensitive comparison, which means that it does not matter whether the user enters uppercase or lowercase letters.
