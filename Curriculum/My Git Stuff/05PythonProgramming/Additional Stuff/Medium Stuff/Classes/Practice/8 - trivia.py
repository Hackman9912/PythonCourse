"""
8. Trivia Game
    In this programming exercise you will create a simple trivia game for two players. The program will 
    work like this:
        • Starting with player 1, each player gets a turn at answering 5 trivia questions. (There
        should be a total of 10 questions.) When a question is displayed, 4 possible answers are
        also displayed. Only one of the answers is correct, and if the player selects the correct
        answer, he or she earns a point.
        • After answers have been selected for all the questions, the program displays the number
        of points earned by each player and declares the player with the highest number of points
        the winner.
    To create this program, write a Question class to hold the data for a trivia question. The
    Question class should have attributes for the following data:
        • A trivia question
        • Possible answer 1
        • Possible answer 2
        • Possible answer 3
        • Possible answer 4
        • The number of the correct answer (1, 2, 3, or 4)
    The Question class also should have an appropriate __init__ method, accessors, and
    mutators.
    The program should have a list or a dictionary containing 10 Question objects, one for
    each trivia question. Make up your own trivia questions on the subject or subjects of your
    choice for the objects.
"""
question_dict = {"Blue, Black or Red?" : ['Blue', 'Red', 'Clear', 'Black'],
                "Yes or No?" : ['Yes', 'Maybe', 'True', 'No'],
                "Laptop or Desktop?" : ['Cell Phone', 'Tablet', 'Laptop', 'Desktop']}

import trivia
import random

def main():
    global question_dict
    questions = trivia.Trivia()

    questions.bulk_add(question_dict)

    for key in questions.get_questions():
        print(key)
        # print(questions.get_questions()[key])
        answerlist = []
        answerlist2 = []
        for i in questions.get_questions()[key]:
            answerlist.append(i)
            answerlist2.append(i)
        random.shuffle(answerlist2)
        print("1", answerlist)
        print("2", answerlist2)
        count = 0
        for i in answerlist2:
            print(f"Number {count}: {i}")
            count += 1
        choice = int(input("Enter the number choice for your answer: "))
        if answerlist[3] == answerlist2[choice]:
            print("You got it right!")
        else:
            print("You got it wrong!")


main()