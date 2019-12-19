# Passing Arguments by Value
All of the example programs that we have looked at so far pass arguments by value. Arguments and parameter variables are separate items in memory. Passing an argument by value means that only a copy of the argument’s value is passed into the parameter variable. If the contents of the parameter variable are changed inside the module, it has no effect on the argument in the calling part of the program. For example, look at Program "Pass By Value."

# Program Pass By Value   
```
 1  Module main()
 2     Declare Integer number = 99
 3
 4     // Display the value stored in number.
 5     Display "The number is ", number
 6
 7     // Call the changeMe module, passing
 8     // the number variable as an argument.
 9     Call changeMe(number)
10
11     // Display the value of number again.
12     Display "The number is ", number
13  End Module
14
15  Module changeMe(Integer myValue)
16     Display "I am changing the value."
17
18     // Set the myValue parameter variable
19     // to 0.
20     Set myValue = 0
21
22     // Display the value in myValue.
23     Display "Now the number is ", myValue
24  End Module
```
```
Program Output
The number is 99
I am changing the value.
Now the number is 0
The number is 99
```
The main module declares a local variable named number in line 2, and initializes it to the value 99. As a result, the Display statement in line 5 displays “The number is 99.” The number variable’s value is then passed as an argument to the changeMe module in line 9. This means that in the changeMe module the value 99 will be copied into the myValue parameter variable.

Inside the changeMe module, in line 20, the myValue parameter variable is set to 0. As a result, the Display statement in line 23 displays “Now the number is 0.” The module ends, and control of the program returns to the main module.

The next statement to execute is the Display statement in line 12. This statement displays “The number is 99.” Even though the myValue parameter variable was changed in the changeMe method, the argument (the number variable in main) was not modified.

Passing an argument is a way that one module can communicate with another module. When the argument is passed by value, the communication channel works in only one direction: the calling module can communicate with the called module. The called module, however, cannot use the argument to communicate with the calling module.

