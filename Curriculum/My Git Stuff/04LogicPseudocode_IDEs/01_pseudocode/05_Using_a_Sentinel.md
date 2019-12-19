# Using a Sentinel

The county tax office calculates the annual taxes on property using the following formula:

![image](https://user-images.githubusercontent.com/47218880/67349598-fc6ea380-f50d-11e9-93ca-d6a25677b711.png)

Every day, a clerk in the tax office gets a list of properties and has to calculate the tax for each property on the list. You have been asked to design a program that the clerk can use to perform these calculations.

In your interview with the tax clerk, you learn that each property is assigned a lot number, and all lot numbers are 1 or greater. You decide to write a loop that uses the number 0 as a sentinel value. During each loop iteration, the program will ask the clerk to enter either a property’s lot number, or 0 to end. Program 5-19 shows the pseudocode for the program, and Figure 5-20 shows a flowchart.

# Program 5-19
```
 1  Module main()
 2     // Local variable for the lot number
 3     Declare Integer lotNumber
 4
 5     // Get the first lot number.
 6     Display "Enter the property's lot number"
 7     Display "(or enter 0 to end)."
 8     Input lotNumber
 9
10     // Continue processing as long as the user
11     // does not enter lot number 0.
12     While lotNumber ! = 0
13        // Show the tax for the property.
14        Call showTax()
15
16       // Get the next lot number.
17       Display "Enter the lot number for the"
18       Display "next property (or 0 to end)."
19       Input lotNumber
20     End While
21  End Module
22
23  // The showTax module gets a property's
24  // value and displays its tax.
25  Module showTax()
26     // Local variables
27     Declare Real propertyValue, tax
28
29     // Constant for the tax factor.
30     Constant Real TAX_FACTOR = 0.0065
31
32     // Get the property's value.
33     Display "Enter the property's value."
34     Input propertyValue
35
36     // Calculate the property's tax.
37     Set tax = propertyValue * TAX_FACTOR
38
39     // Display the tax.
40     Display "The property's tax is $", tax
41  End Module
```
# Program Output (with Input Shown in Bold)
Enter the property's lot number
(or enter 0 to end).
## 417 [Enter] 
Enter the property's value.
## 100000 [Enter] 
The property's tax is $650
Enter the lot number for the
next property (or 0 to end).
## 692 [Enter] 
Enter the property's value.
## 60000 [Enter] 
The property's tax is $390
Enter the lot number for the
next property (or 0 to end).
## 0 [Enter]

![image](https://user-images.githubusercontent.com/47218880/67349714-553e3c00-f50e-11e9-8d21-0ea62619381d.png)
Figure 5-20 Flowchart for Program 5-19
