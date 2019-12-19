"""
4. Chick-fil-a vs Popeye's Chicken Sandwich Quest
    Using a superclass of Person with two subclasses Student and Instructor create 
    a program that determines who is going to go where and how we'll grade the 
    sandwiches and determine a winner. Get creative with this one. Add in some 
    methods and have fun with it.I'll leave 
    this open to see what you come up with. 
	
"""
import sandwich
import random
import pprint
import time
import os
import pickle
popeyes = 0
chikfil = 0


def main():
    global popeyes, chikfil
    empty_list = []
    instructors = read_or_new_pickle('instructorlist.dat', empty_list)
    students = read_or_new_pickle('studentlist.dat', empty_list)
    print("Welcome to the great chicken sandwich showdown!")
    enter_or_vote = 1
    while enter_or_vote != 0:
        print('Enter 1 to submit participants, 2 to view participicants, and 3 to vote. 0 to exit:')
        enter_or_vote = int(input("Enter selection now: "))
        if enter_or_vote == 1:
            print('Enter the number of people participating in the great chicken showdown!')
            participants = int(input(': '))
            get_part(participants, instructors, students)
            
        elif enter_or_vote == 2:
            print('\n' * 50)
            list_print(instructors, 'instructorlist.dat')
            list_print(students, 'studentlist.dat')
            name_list = get_names(instructors, students)
            random.shuffle(name_list)
            if (len(name_list) % 2) ==0:
                pope = name_list[:len(name_list)//2]
                chik = name_list[len(name_list)//2:]
            else:
                pope = name_list[:(len(name_list)+1)//2]
                chik = name_list[(len(name_list)+1)//2:]
            print("Here are the folks going to Chik-Fil-A")
            pprint.pprint(chik)
            print("Here are the folks going to Popeyes")
            pprint.pprint(pope)
    #time.sleep(2700)
        elif enter_or_vote == 3:
            ready = 0
            while ready != 1:
                ready = int(input('Enter 1 when all participants are ready to vote: '))
            get_vote(instructors)
            get_vote(students)
            print(f'Popeyes had {popeyes:} votes.')
            print(f'Chik Fil A had {chikfil:} votes.')
            time.sleep(5)
            exit()
def get_part(count, ins_list, stu_list):
    for i in range(count):
        print('\n' * 50) 
        print(f'Person {i+1:}')
        ptype = 0
        while ptype != 1 and ptype != 2:
            ptype = int(input('If the person is a student press 1\nIf the person is an instructor press 2: '))
        if ptype == 1:
            name = input('Enter the students name: ').title()
            diet = input('Enter the students dietary restrictions(if none enter None): ').title()
            rank = input('Enter the rank of the student: ')
            student_obj = sandwich.Student(name, diet, rank)
            stu_list.append(student_obj)
        elif ptype == 2:
            name = input('Enter the instructors name: ')
            diet = input('Enter the instructors dietary restrictions: ')
            ins_type = input('Enter the type of instructor they are: ')
            ins_obj = sandwich.Instructor(name, diet, ins_type)
            ins_list.append(ins_obj)
def list_print(list1, file1):
    output_file = open(file1, 'wb')
    pickle.dump(list1, output_file)
    output_file.close()
    for i in list1:
        if i.get_diet() != 'None':
            print(f'The name is: {i.get_name()}')
            print(f'The dietary restrictions are: {i.get_diet()}')
def get_names(list1, list2):
    big_list = list1 + list2
    name_list = []
    for i in big_list:
        names = i.get_name()
        name_list.append(names)
    return name_list
def get_vote(list1):
    global popeyes, chikfil
    for i in list1:
        print(f'{i.get_name():} enter your vote!')
        vote = 0
        while vote != 1 and vote != 2:
            vote = int(input('Enter 1 for Popeyes or 2 for the Chik Fil A sandwich: '))
        if vote == 1:
            popeyes += 1
        elif vote == 2:
            chikfil += 1
        print('Thank you for your vote')
def read_or_new_pickle(path, default):
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            try:
                return pickle.load(f)
            except Exception:
                pass
    with open(path, 'wb') as f:
        pickle.dump(default, f)
    return default            

main()