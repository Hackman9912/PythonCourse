# 6. Body Mass Index
# Write a program that calculates and displays a person’s body mass index (BMI). 
# TheBMI is often used to determine whether a person is overweight or underweight for hisor her height. 
# A person’s BMI is calculated with the following formula: 
# BMI  = weight * 703 / height^2
# where weight is measured in pounds and height is measured in inches.

def main():
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    bmi = calc(weight, height)
    print(f"Your BMI is: {bmi:.2f}")

def calc(num1, num2):
    return num1*703/(num2**2)

main()