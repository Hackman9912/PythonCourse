|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---

## Lab 2B & Lab2C


**Lab 2B: Numbers**

* **Instructions:** Modify lab2b.py and follow the comment instructions.
* **BONUS:** shorten the code!

**Lab 2C: Tax Calculator**

* **Instructions:** Write a program that calculates the total of an item, with taxes.
* **Bonus:**  Add additional functionality
* Keep in mind that you have not learned Python formatting for print or user input. 
  * Simple/ugly printing is allowed here. 
  * Hard code the user input


```
Module main()
    #Get tax rate
    tax=input("What is the tax rate?")
        # Output What is the tax rate percentage?
        6.5

    #Set tax to a real number
    tax=float(tax)

    # Convert user input to a better number

    taxRate=tax/100

    total=input("What is the amount to be taxed?")
        # Output What is the amount to be taxed
        155

    #Set total to real
    total=float(total)

    #Calculate the tax amount
    taxed=total*taxRate

    # Do total amount
    totalAmount=taxRate+total

    # Round out the decimals
    total=round(total, 2)
    taxed=round(taxed, 2)
    totalAmount=round(totalAmount, 2)

    #Display the amounts
    print("Your pretax amount is", total, "Your tax is", taxed,
            "Your full total is", totalAmount)

End Module
```
---

|[Next Topic](/02_Data_Types/03_strings.md)|
|---|
