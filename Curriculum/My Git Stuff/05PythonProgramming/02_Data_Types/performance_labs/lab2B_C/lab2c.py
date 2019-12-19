#Python lab2c

#Get tax rate
tax=input("What is the tax rate?")
       
        

#Set tax to a real number
tax=float(tax)

# Convert user input to a better number
taxRate=tax/100

total=input("What is the amount to be taxed?")
       
        

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
print("Your pretax amount is", total, "Your tax is", taxed,"Your full total is", totalAmount)