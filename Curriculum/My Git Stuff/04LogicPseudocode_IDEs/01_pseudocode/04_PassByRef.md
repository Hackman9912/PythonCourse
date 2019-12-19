# Passing Arguments by Reference
Passing an argument by reference means that the argument is passed into a special type of parameter known as a reference variable. When a reference variable is used as a parameter in a module, it allows the module to modify the argument in the calling part of the program.

A reference variable acts as an alias for the variable that was passed into it as an argument. It is called a reference variable because it references the other variable. Anything that you do to the reference variable is actually done to the variable it references.

Reference variables are useful for establishing two-way communication between modules. When a module calls another module and passes a variable by reference, communication between the modules can take place in the following ways:

The calling module can communicate with the called module by passing an argument.

The called module can communicate with the calling module by modifying the value of the argument via the reference variable.

In pseudocode, we will declare that a parameter is a reference variable by writing the word Ref before the parameter variable’s name in the module header. For example, look at the following pseudocode module:
```
Module setToZero(Integer Ref value)
  Set value = 0
End Module
```
The word Ref indicates that value is a reference variable. The module stores 0 in the value parameter. Because value is a reference variable, this action is actually performed on the variable that was passed to the module as an argument. Program "Pass by Ref" demonstrates this module.

# Program Pass by Ref
```
 1  Module main()
 2     // Declare and initialize some variables.
 3     Declare Integer x = 99
 4     Declare Integer y = 100
 5     Declare Integer z = 101
 6
 7     // Display the values in those variables.
 8     Display "x is set to ", x
 9     Display "y is set to ", y
10     Display "z is set to ", z
11
12     // Pass each variable to setToZero.
13     Call setToZero(x)
14     Call setToZero(y)
15     Call setToZero(z)
16
17     // Display the values now.
18     Display "---------------"
19     Display "x is set to ", x
20     Display "y is set to ", y
21     Display "z is set to ", z
22  End Module
23
24  Module setToZero(Integer Ref value)
25     Set value = 0
26  End Module
```
```
Program Output
x is set to 99
y is set to 100
z is set to 101
---------------
x is set to 0
y is set to 0
z is set to 0
```
In the main module the variable x is initialized with 99, the variable y is initialized with 100, and the variable z is initialized with 101. Then, in lines 13 through 15 those variables are passed as arguments to the setToZero module. Each time setToZero is called, the variable that is passed as an argument is set to 0. This is shown when the values of the variables are displayed in lines 19 through 21.
