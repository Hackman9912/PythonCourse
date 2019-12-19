# This program averages the test scores. It asks user for the number of students and the test scores for students


# Get num students
num_students = int(input("How many students do you have? "))


# get num test scores per student
num_test_scores = int(input("How many test scores per student? "))


# Determin each students average test score

for student in range(num_students):
    # initialize accumulator
    total = 0.0

    # Get student test scores
    print("Student number", student+1)
    print("---------------")
    for test_num in range(num_test_scores):
        print("Test number", test_num +1)
        score = float(input(': '))
        total += score

    # Calc average score for this student

    average = total / num_students

    # Display average

    print("The average for student ", student+1, "is", average)
