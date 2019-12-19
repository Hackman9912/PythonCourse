# 5. Property Tax
# A county collects property taxes on the assessment value of property, which is 60 percent of the property’s actual value. 
# For example, if an acre of land is valued at $10,000,its assessment value is $6,000. The property tax is then 64¢ for each $100 of the assessment value. 
# The tax for the acre assessed at $6,000 will be $38.40. 
# Write a program thatasks for the actual value of a piece of property and displays the assessment value andproperty tax.

def main():
    actual_value = float(input("Enter the actual vlaue of your property: "))
    assessment_value = assess(actual_value)
    property_tax = tax(assessment_value)
    print("Your assessed value is:", assessment_value, "and your property tax is:", property_tax)



def assess(property):
    return property*.6

def tax(assessment):
    return (assessment/100)*.64
main()