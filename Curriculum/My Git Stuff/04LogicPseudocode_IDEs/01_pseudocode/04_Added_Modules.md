
# Defining and Calling Modules

Professional Appliance Service, Inc. offers maintenance and repair services for household appliances. The owner wants to give each of the company’s service technicians a small handheld computer that displays step-by-step instructions for many of the repairs that they perform. To see how this might work, the owner has asked you to develop a program that displays the following instructions for disassembling an ACME laundry dryer:
```
Step 1. Unplug the dryer and move it away from the wall.

Step 2. Remove the six screws from the back of the dryer.

Step 3. Remove the dryer’s back panel.

Step 4. Pull the top of the dryer straight up.
```
During your interview with the owner, you determine that the program should display the steps one at a time. You decide that after each step is displayed, the user will be asked to press a key to see the next step. Here is the algorithm for the program:
```
Display a starting message, explaining what the program does.

Ask the user to press a key to see Step 1.

Display the instructions for Step 1.

Ask the user to press a key to see the next step.

Display the instructions for Step 2.

Ask the user to press a key to see the next step.

Display the instructions for Step 3.

Ask the user to press a key to see the next step.

Display the instructions for Step 4.
```
This algorithm lists the top level of tasks that the program needs to perform, and becomes the basis of the program’s main module. Figure below shows the program’s structure in a hierarchy chart.
![image](https://user-images.githubusercontent.com/47218880/67345932-700ab380-f502-11e9-9d62-b5438124f3b8.png)


As you can see from the hierarchy chart, the main module will call several other modules. Here are summaries of those modules:
```
startingMessage—This module will display the starting message that tells the technician what the program does.

step1—This module will display the instructions for Step 1.

step2—This module will display the instructions for Step 2.

step3—This module will display the instructions for Step 3.

step4—This module will display the instructions for Step 4.
```
Between calls to these modules, the main module will instruct the user to press a key to see the next step in the instructions. Program 3-2 shows the pseudocode for the program. Figure 3-9 shows the flowchart for the main module, and Figure 3-10 shows the flowcharts for the startingMessage, step1, step2, step3, and step4 modules.

## Program 3-2
```
 1  Module main()
 2     // Display the starting message.
 3     Call startingMessage()
 4     Display "Press a key to see Step 1."
 5     Input
 6
 7     // Display Step 1.
 8     Call step1()
 9     Display "Press a key to see Step 2."
10     Input
11
12     // Display Step 2.
13     Call step2()
14     Display "Press a key to see Step 3."
15     Input
16
17     // Display Step 3.
18     Call step3()
19     Display "Press a key to see Step 4."
20     Input
21
22     // Display Step 4.
23     Call step4()
24  End Module
25
26  // The startingMessage module displays
27  // the program's starting message.
28  Module startingMessage()
29     Display "This program tells you how to"
30     Display "disassemble an ACME laundry dryer."
31     Display "There are 4 steps in the process."
32  End Module
33
34  // The step1 module displays the instructions
35  // for Step 1.
36  Module step1()
37     Display "Step 1: Unplug the dryer and"
38     Display "move it away from the wall."
39  End Module
40
41  // The step2 module displays the instructions
42  // for Step 2.
43  Module step2()
44     Display "Step 2: Remove the six screws"
45     Display "from the back of the dryer."
46  End Module
47
48  // The step3 module displays the instructions
49  // for Step 3.
50  Module step3()
51     Display "Step 3: Remove the dryer's"
52     Display "back panel."
53  End Module
54
55  // The step4 module displays the instructions
56  // for Step 4.
57  Module step4()
58     Display "Step 4: Pull the top of the"
59     Display "dryer straight up."
60  End Module
```
## Program Output (with Input Shown in Bold)

This program tells you how to
disassemble an ACME laundry dryer.
There are 4 steps in the process.
Press a key to see Step 1.
## [Enter] 
Step 1: Unplug the dryer and
move it away from the wall.
Press a key to see Step 2.
## [Enter] 
Step 2: Remove the six screws
from the back of the dryer.
Press a key to see Step 3.
## [Enter] 
Step 3: Remove the dryer's
back panel.
Press a key to see Step 4.
## [Enter] 
Step 4: Pull the top of the
dryer straight up.

![image](https://user-images.githubusercontent.com/47218880/67346174-7d746d80-f503-11e9-91ca-0bcfb4082d70.png)

Figure 3-9 Flowchart for the main module in Program 3-2
![image](https://user-images.githubusercontent.com/47218880/67346185-85341200-f503-11e9-85f8-ae595420ae18.png)

Figure 3-10 Flowcharts for the other modules in Program 3-2

 NOTE:
Lines 5, 10, 15, and 20 show an Input statement with no variable specified. In our pseudocode, this is the way we will read a keystroke from the keyboard without saving the character that was pressed. Most programming languages provide a way to do this.



