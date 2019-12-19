# 10. Body Mass Index Program Enhancement
# In programming Exercise #6 in Chapter 3 you were asked to write a program that calculates a person’s body mass index
# (BMI). Recall from that exercise that the BMI is often used
# to determine whether a person is overweight or underweight for their height. A person’s
# BMI is calculated with the formula
# BMI = weight * 703 / height2
# where weight is measured in pounds and height is measured in inches. Enhance the program so it displays a message
# indicating whether the person has optimal weight, is
# underweight, or is overweight. A person’s weight is considered to be optimal if his or
# her BMI is between 18.5 and 25. If the BMI is less than 18.5, the person is considered
# to be underweight. If the BMI value is greater than 25, the person is considered to be
# overweight.

def main():
    bmi_calc = lambda x, y : x*703/(y**2)
    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))
    bmi = bmi_calc(weight, height)
    if bmi < 18.5:
        print(f"Your BMI is {bmi:.2f} which is under weight.")
    elif bmi > 18.5 and bmi < 25:
        print(f"Your BMI is {bmi:.2f} which is optimal.")
    else:
        print(f"Your BMI is {bmi:.2f} which is over weight. So, your are fat. Hit the gym. Fatty")

# replaced with lambda
# def bmi_calc(num1, num2):
#     return num1*703 / (num2**2)

main()