"""
 6. Driver’s License Exam
The local driver’s license office has asked you to create an application that grades the written portion of the
 driver’s license exam. The exam has 20 multiple-choice questions. Here
are the correct answers:
1. B 	6. A 	11. B 	16. C
2. D 	7. B 	12. C 	17. C
3. A 	8. A 	13. D 	18. B
4. A 	9. C 	14. A 	19. D
5. C 	10. D 	15. D 	20. A
Your program should store these correct answers in a list. The program should read the
student’s answers for each of the 20 questions from a text file and store the answers in
another list. (Create your own text file to test the application.) After the student’s answers
have been read from the file, the program should display a message indicating whether the
student passed or failed the exam. (A student must correctly answer 15 of the 20 questions
to pass the exam.) It should then display the total number of correctly answered questions,
the total number of incorrectly answered questions, and a list showing the question numbers of the incorrectly 
answered questions.

"""
correct = 0
incorrect = 0
count = 0
correctAnswers = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
studentAnswers = []
incorrectAnswers = []
print("Use this tool to grade your test. Answers should be one per a line, only list the answer and capitolize the answer: IE 'A'")
fileName = input("Enter the name of your file to be graded: ")
f = open(fileName, 'r')
f_contents = f.readline().rstrip('\n')
while f_contents != '':
    studentAnswers.append(f_contents)
    f_contents = f.readline().rstrip('\n')
f.close()


while count < 20:
    if correctAnswers[count] == studentAnswers[count]:
        count += 1
        correct += 1
    else:
        number = count + 1
        incorrectAnswers.append(number)
        count += 1
        incorrect += 1

print("You got", correct, "correct.")
print("You got", incorrect, "incorrect.")

if incorrect >= 5:
    print("You got the following questions wrong: ")
    print(incorrectAnswers)
    print("You got ", incorrect, "wrong, you failed")
elif incorrect > 0:
    print("You got the following questions wrong: ")
    print(incorrectAnswers)
else:
    print("You got a perfect score.")