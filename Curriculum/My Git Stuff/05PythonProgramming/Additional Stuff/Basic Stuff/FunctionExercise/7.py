# 7. Calories from Fat and Carbohydrates
# A nutritionist who works for a fitness club helps members by evaluating their diets. As partof her evaluation, she asks members for the number of fat grams and carbohydrate grams
# that they consumed in a day. Then, she calculates the number of calories that result from the fat, using the following formula:
# calories from fat = fat grams * 9
# Next, she calculates the number of calories that result from the carbohydrates, using thefollowing formula:
# calories from carbs = carb grams * 4
# The nutritionist asks you to write a program that will make these calculations.

def main():
    fat_grams = int(input("Enter the number of fat grams you have consumed today: "))
    carb_grams = int(input("Enter the number of carbohydrate grams you have consumed today: "))
    fat_calories = caloriefat(fat_grams)
    carb_calories = caloriecarb(carb_grams)
    notify(fat_calories, carb_calories)

def caloriefat(num1):
    return num1*9

def caloriecarb(num1):
    return num1*4

def notify(num1, num2):
    print("The number of calories you have gotten from fats is, ", num1, "and the number of calories from carbs is ", num2)

main()