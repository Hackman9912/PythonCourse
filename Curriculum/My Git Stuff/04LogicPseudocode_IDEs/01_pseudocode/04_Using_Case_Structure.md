
# Using a Case Structure

Lenny, who owns Lenny’s Stereo and Television, has asked you to write a program that will let a customer pick one of three TV models and then displays the price and size of the selected model. Here is the algorithm:
```
Get the TV model number.

If the model is 100, then display the information for that model.

Otherwise, if the model is 200, then display the information for that model.

Otherwise, if the model is 300, then display the information for that model.
```
At first, you consider designing a nested decision structure to determine the model number and display the correct information. But you realize that a case structure will work just as well because a single value, the model number, will be used to determine the action that the program will perform. The model number can be stored in a variable, and that variable can be tested by the case structure. Assuming that the model number is stored in a variable named modelNumber, Figure 4-20 shows a flowchart for the case structure. Program 4-8 shows the pseudocode for the program.


![image](https://user-images.githubusercontent.com/47218880/67347007-62efc380-f506-11e9-9539-b1157fb6f9ad.png)

Figure 4-20 Flowchart for the case structure

## Program 4-8
```
1  // Constants for the TV prices
 2  Constant Real MODEL_100_PRICE = 199.99
 3  Constant Real MODEL_200_PRICE = 269.99
 4  Constant Real MODEL_300_PRICE = 349.99
 5
 6  // Constants for the TV sizes
 7  Constant Integer MODEL_100_SIZE = 24
 8  Constant Integer MODEL_200_SIZE = 27
 9  Constant Integer MODEL_300_SIZE = 32
10
11  // Variable for the model number
12  Declare Integer modelNumber
13
14  // Get the model number.
15  Display "Which TV are you interested in?"
16  Display "The 100, 200, or 300?"
17  Input modelNumber
18
19  // Display the price and size.
20  Select modelNumber
21     Case 100:
22        Display "Price: $", MODEL_100_PRICE
23        Display "Size: ", MODEL_100_SIZE
24     Case 200:
25        Display "Price: $", MODEL_200_PRICE
26        Display "Size: ", MODEL_200_SIZE
27     Case 300:
28        Display "Price $", MODEL_300_PRICE
29        Display "Size: ", MODEL_300_SIZE
30     Default:
31        Display "Invalid model number"
32  End Select
```
# Program Output (with Input Shown in Bold)
Which TV are you interested in?
The 100, 200, or 300?
## 100 [Enter] 
Price: $199.99
Size: 24
# Program Output (with Input Shown in Bold)
Which TV are you interested in?
The 100, 200, or 300?
## 200 [Enter] 
Price: $269.99
Size: 27
# Program Output (with Input Shown in Bold)
Which TV are you interested in?
The 100, 200, or 300?
## 300 [Enter] 
Price: $349.99
Size: 32
# Program Output (with Input Shown in Bold)
Which TV are you interested in?
The 100, 200, or 300?
## 500 [Enter] 
Invalid model number
 NOTE:
The details of writing a case structure differ from one language to another. Because of the specific rules that each language uses for writing case structures, you might not be able to use the case structure for every multiple alternative decision. In such an event, you can use the If-Then-Else If statement or a nested decision structure.
