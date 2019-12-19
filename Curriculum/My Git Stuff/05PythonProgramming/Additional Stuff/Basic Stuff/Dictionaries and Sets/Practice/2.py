'''
2. Capital Quiz
Write a program that creates a dictionary containing the U.S. states as keys and their capitals as values. 
(Use the Internet to get a list of the states and their capitals.) The program
should then randomly quiz the user by displaying the name of a state and asking the user
to enter that state’s capital. The program should keep a count of the number of correct and
incorrect responses. (As an alternative to the U.S. states, the program can use the names of
countries and their capitals.)
'''

# import the neato library
import random
# make this ridiculous dictionary
state_capitals = {
    'Arizona' : 'Phoenix',
    'Alaska' : 'Juneau',
    'Arkansas' : 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
    }
# set the cont variable
cont = 'y'
# set my counters
correct = 0
incorrect = 0
# set the while loop to play as long as the user wants
while cont == 'y':
    # randomly select a state to ask about
    rando = random.choice(list(state_capitals.keys()))
    # Ask student to put the capital of the random choice
    student_answer = input(f"Enter the capital for {rando:}: ")
    # print(state_capitals[rando])
    # If the student is correct then add one to correct and tell them how many
    if student_answer.lower() == state_capitals[rando].lower():
        correct += 1
        print("You are right!", state_capitals[rando], "is the capital of", rando)
        print("You have gotten ", correct, "right answers.")
        print("You have gotten ", incorrect, "wrong answers. ")
    # If they got it wrong add to incorrect and tell them how many wrong
    else:
        incorrect += 1
        print("Sad day...", state_capitals[rando], "is the capital of", rando)
        print("You have gotten ", correct, "right answers.")
        print("You have gotten ", incorrect, "wrong answers. ")
    # Do thye want to keep playing?
    cont = input("If you would like to continue enter y. To quit enter any other key. ").lower()