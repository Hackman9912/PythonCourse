# Using the If-Then-Else Statement

Chris owns an auto repair business and has several employees. If an employee works over 40 hours in a week, Chris pays that employee 1.5 times his or her regular hourly pay rate for all hours over 40. Chris has asked you to design a simple payroll program that calculates an employee’s gross pay, including any overtime wages. You design the following algorithm:
```
Get the number of hours worked.

Get the hourly pay rate.

If the employee worked more than 40 hours, calculate the gross pay with overtime. Otherwise, calculate the gross pay as usual.

Display the gross pay.
```
You go through the top-down design process and create the hierarchy chart shown in Figure 4-10. As shown in the hierarchy chart, the main module will call four other modules. The following are summaries of those modules:
![image](https://user-images.githubusercontent.com/47218880/67346573-d0025980-f504-11e9-9bfa-311f7c3c4a9a.png)
Figure 4-10 Hierarchy chart

```
getHoursWorked—This module will ask the user to enter the number of hours worked.

getPayRate—This module will ask the user to enter the hourly pay rate.

calcPayWithOT—This module will calculate an employee’s pay with overtime.

calcRegularPay—This module will calculate the gross pay for an employee with no overtime.
```
The main module, which executes when the program is run, will call these modules and then display the gross pay. The pseudocode for the program is shown in Program 4-2. Figures 4-11 and 4-12 show flowcharts for each of the modules.

![image](https://user-images.githubusercontent.com/47218880/67346613-ef998200-f504-11e9-9796-d92fb0f25d46.png)

Figure 4-11 Flowchart for the main module

![image](https://user-images.githubusercontent.com/47218880/67346685-2a031f00-f505-11e9-8755-9743ff8ac8b3.png)

Figure 4-12 Flowcharts for the other modules

## Program 4-2
```
 1  // Global constants
 2  Constant Integer BASE_HOURS = 40
 3  Constant Real OT_MULTIPLIER = 1.5
 4
 5  Module main()
 6     // Local variables
 7     Declare Real hoursWorked, payRate, grossPay
 8
 9     // Get the number of hours worked.
10     Call getHoursWorked(hoursWorked)
11
12     // Get the hourly pay rate.
13     Call getPayRate(payRate)
14
15     // Calculate the gross pay.
16     If hoursWorked > BASE_HOURS Then
17        Call calcPayWithOT(hoursWorked, payRate,
18                          grossPay)
19     Else
20        Call calcRegularPay(hoursWorked, payRate,
21                           grossPay)
22     End If
23
24     // Display the gross pay.
25     Display "The gross pay is $", grossPay
26  End Module
27
28  // The getHoursWorked module gets the number
29  // of hours worked and stores it in the
30  // hours parameter.
31  Module getHoursWorked(Real Ref hours)
32     Display "Enter the number of hours worked."
33     Input hours
34  End Module
35
36  // The getPayRate module gets the hourly
37  // pay rate and stores it in the rate
38  // parameter.
39  Module getPayRate(Real Ref rate)
40     Display "Enter the hourly pay rate."
41     Input rate
42  End Module
43
44  // The calcPayWithOT module calculates pay
45  // with overtime. The gross pay is stored
46  // in the gross parameter.
47  Module calcPayWithOT(Real hours, Real rate,
48                       Real Ref gross)
49     // Local variables
50     Declare Real overtimeHours, overtimePay
51
52     // Calculate the number of overtime hours.
53     Set overtimeHours = hours - BASE_HOURS
54
55     // Calculate the overtime pay
56     Set overtimePay = overtimeHours * rate * 
57 OT_MULTIPLIER
58
59     // Calculate the gross pay.
60     Set gross = BASE_HOURS * rate + overtimePay
61  End Module
62
63  // The calcRegularPay module calculates
64  // pay with no overtime and stores it in
65  // the gross parameter.
66  Module calcRegularPay(Real hours, Real rate,
67                        Real Ref gross)
68     Set gross = hours * rate
69  End Module
```
#  Program Output (with Input Shown in Bold)
Enter the number of hours worked.
## 40 [Enter] 
Enter the hourly pay rate.
## 20 [Enter] 
The gross pay is $800

# Program Output (with Input Shown in Bold)
Enter the number of hours worked.
## 50 [Enter] 
Enter the hourly pay rate.
## 20 [Enter] 
The gross pay is $1100
Notice that two global constants are declared in lines 2 and 3. The BASE_HOURS constant is set to 40, which is the number of hours an employee can work in a week without getting paid overtime. The OT_MULTIPLIER constant is set to 1.5, which is the pay rate multiplier for overtime hours. This means that the employee’s hourly pay rate is multiplied by 1.5 for all overtime hours.
