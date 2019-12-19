
# Designing a While Loop

A project currently underway at Chemical Labs, Inc. requires that a substance be continually heated in a vat. A technician must check the substance’s temperature every 15 minutes. If the substance’s temperature does not exceed 102.5, then the technician does nothing. However, if the temperature is greater than 102.5, the technician must turn down the vat’s thermostat, wait five minutes, and check the temperature again. The technician repeats these steps until the temperature does not exceed 102.5. The director of engineering has asked you to design a program that guides the technician through this process.

##  Here is the algorithm:
```
Get the substance’s temperature.

Repeat the following steps as long as the temperature is greater than 102.5:

Tell the technician to turn down the thermostat, wait five minutes, and check the temperature again.

Get the substance’s temperature.
```
After the loop finishes, tell the technician that the temperature is acceptable and to check it again in 15 minutes.

After reviewing this algorithm, you realize that steps 2(a) and 2(b) should not be performed if the test condition (temperature is greater than 102.5) is false to begin with. The While loop will work well in this situation, because it will not execute even once if its condition is false. Program 5-2 shows the pseudocode for the program, and Figure 5-4 shows a flowchart.

## Program 5-2
```
 1  // Variable to hold the temperature
 2  Declare Real temperature
 3
 4  // Constant for the maximum temperature
 5  Constant Real MAX_TEMP = 102.5
 6
 7  // Get the substance's temperature.
 8  Display "Enter the substance's temperature."
 9  Input temperature
10
11  // If necessary, adjust the thermostat.
12  While temperature > MAX_TEMP
13     Display "The temperature is too high."
14     Display "Turn the thermostat down and wait"
15     Display "five minutes. Take the temperature"
16     Display "again and enter it here."
17     Input temperature
18  End While
19
20  // Remind the user to check the temperature
21  // again in 15 minutes.
22  Display "The temperature is acceptable."
23  Display "Check it again in 15 minutes."
```
# Program Output (with Input Shown in Bold)
Enter the substance's temperature.
## 104.7 [Enter] 
The temperature is too high.
Turn the thermostat down and wait
five minutes. Take the temperature
again and enter it here.
## 103.2 [Enter] 
The temperature is too high.
Turn the thermostat down and wait
five minutes. Take the temperature
again and enter it here.
## 102.1 [Enter] 
The temperature is acceptable.
Check it again in 15 minutes.
# Program Output (with Input Shown in Bold)
Enter the substance's temperature.
## 102.1 [Enter] 
The temperature is acceptable.
Check it again in 15 minutes.

![image](https://user-images.githubusercontent.com/47218880/67348399-6c7b2a80-f50a-11e9-9567-94f49ae460da.png)


