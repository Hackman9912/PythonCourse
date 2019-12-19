>As shown in this chapter, write a pseudocode statement that generates a random number in the range of 1 through 100 and assigns it to a variable named rand.

```
Module main()
   Declare Integer count
   Declare Integer rand

   For count = 1 To 100

      Set rand = random(1, 100)
      Display rand

   End For

End Module
```

 >The following pseudocode statement calls a function named half, which returns a value that is half that of the argument. (Assume both the result and number variables are Real.) Write pseudocode for the function.

Set result = half(number)

```
Set tesult = half(number)
Function Real half(Real num)

   Return num / 2

End Function
```

 >A pseudocode program contains the following function definition:

```
	Function Integer cube(Integer num)
   Return num * num * num
End Function
```


Write a statement that passes the value 4 to this function and assigns its return value to the variable result.

```
Set result = cube (4)
```

>Design a pseudocode function named timesTen that accepts an Integer argument. When the function is called, it should return the value of its argument multiplied times 10.



>Design a pseudocode function named getFirstName that asks the user to enter his or her first name, and returns it.

```
Function String get(firstName)
   Declare String firstName
   Display "Enter your first name:"
   Input firstName

   return firstName

End Function
```

Assume that a program has two String variables named str1 and str2. Write a pseudocode statement that assigns an all uppercase version of str1 to the str2 variable.

```
set str2 = toUpper(str1)
```

Debugging Exercises
The programmer intends for this pseudocode to display three random numbers in the range of 1 through 7. According to the way we’ve been generating random numbers in this book, however, there appears to be an error. Can you find it?


// This program displays three random numbers
// in the range of 1 through 7.
Declare Integer count

// Display three random numbers.
For count = 1 To 3
   Display random(7, 1) 
   
   ///////// (1, 7)
End For


Can you find the reason that the following pseudocode function does not return the value indicated in the comments?


// The calcDiscountPrice function accepts an item's price and
// the discount percentage as arguments. It uses those
// values to calculate and return the discounted price.
Function Real calcDiscountPrice(Real price, Real percentage)
   // Calculate the discount.
   Declare Real discount = price * percentage

   // Subtract the discount from the price.
   Declare Real discountPrice = price – discount 

   // Return the discount price.
   Return discount

   /////////return discountPrice

End Function

Can you find the reason that the following pseudocode does not perform as indicated in the comments?

/////// Result is never set


// Find the error in the following pseudocode.
Module main()
    Declare Real value, result

    // Get a value from the user.
    Display "Enter a value."
    Input value

    // Get 10 percent of the value.
    Call tenPercent(value)

    // Display 10 percent of the value.
    Display "10 percent of ", value, " is ", result
End Module

// The tenPercent function returns 10 percent
// of the argument passed to the function.
Function Real tenPercent(Real num)
    Return num * 0.1
End Function
