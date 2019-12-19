# Designing a Count-Controlled Loop with the For Statement

Your friend Amanda just inherited a European sports car from her uncle. Amanda lives in the United States, and she is afraid she will get a speeding ticket because the car’s speedometer works in kilometers per hour. She has asked you to write a program that displays a table of speeds in kilometers per hour with their values converted to miles per hour. The formula for converting kilometers per hour to miles per hour is:

![image](https://user-images.githubusercontent.com/47218880/67349075-7a31af80-f50c-11e9-82d2-105a64a2f58f.png)

In the formula, MPH is the speed in miles per hour and KPH is the speed in kilometers per hour.

The table that your program displays should show speeds from 60 kilometers per hour through 130 kilometers per hour, in increments of 10, along with their values converted to miles per hour. The table should look something like this:

![image](https://user-images.githubusercontent.com/47218880/67349102-959cba80-f50c-11e9-850f-5c7e23fc4066.png)

After thinking about this table of values, you decide that you will write a For loop that uses a counter variable to hold the kilometer-per-hour speeds. The counter’s starting value will be 60, its ending value will be 130, and a step value of 10 will be used. Inside the loop you will use the counter variable to calculate a speed in miles-per-hour. Program 5-11 shows the pseudocode for the program, and Figure 5-16 shows a flowchart.

# Program 5-11
```
 1  // Declare variables to hold speeds in MPH and KPH.
 2  Declare Real mph
 3  Declare Integer kph
 4  5  // Display the table headings.
 6  Display "KPH", Tab, "MPH"
 7  Display "-----------------------"
 8
 9  // Display the speeds.
10  For kph = 60 To 130 Step 10
11     // Calculate the miles-per-hour.
12     Set mph = kph * 0.6214
13
14     // Display KPH and MPH.
15     Display kph, Tab, mph
16  End For
```
# Program Output

![image](https://user-images.githubusercontent.com/47218880/67349195-e1e7fa80-f50c-11e9-8cb5-de8d2c426c1e.png)

![image](https://user-images.githubusercontent.com/47218880/67349366-430fce00-f50d-11e9-8717-8637439c1181.png)

Figure 5-16 Flowchart for Program 5-11

Notice that a variable named kph is used as the counter. Until now we have used the name counter for our counter variables. In this program, however, kph is a better name for the counter because it will hold speeds in kilometers-per-hour.
