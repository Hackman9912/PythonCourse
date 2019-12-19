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
class Trivia:
    def __init__(self):
        self.__question_list = {}

    def add_question(self, question, answer1, answer2, answer3, correct):
        self.__question_list[question] = [answer1, answer2, answer3, correct]

    def bulk_add(self, dict1):
        print("Make a dictionary in the format of dict = {Question : [Answer1, Answer2, Answer3, CorrectAnswer], Question : .... etc}")
        self.__question_list = dict1

    def get_questions(self):
        return self.__question_list
    def __str__(self):
        return self.__question_list