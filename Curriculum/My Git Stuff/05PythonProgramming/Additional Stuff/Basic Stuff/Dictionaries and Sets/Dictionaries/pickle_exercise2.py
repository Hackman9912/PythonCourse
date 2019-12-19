"""

8. Name and Email Addresses
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person’s email address, add
a new name and email address, change an existing email address, and delete an existing
name and email address. The program should pickle the dictionary and save it to a file
when the user exits the program. Each time the program starts, it should retrieve the 
dictionary from the file and unpickle it.

"""

# This program maintains a dictionary binary file that stores names and emails and allows a user to interact with the data in the file
# import the cool pickle
import pickle
import pprint
# establish a global variable
user_choice = 5

# define main
def main():
    # call the global variable
    global user_choice
    # Open output file
    output_file = open('name_email.dat', 'rb+')
    # set end of file to false so that it will try the things
    end_of_file = False
    # loop to open the pickle load
    while end_of_file == False:
        # try to do the pickle load
        try:
            name_email = pickle.load(output_file)
        # If it wont work then move on
        except: 
            end_of_file = True
    # show the first display to get user choice
    first_display(user_choice)
    # send user choice to the dictionary to allow user to interact with dictionary
    menu(user_choice, name_email)
    # pickle the dictionary to the file
    pickle.dump(name_email, output_file)
    # close the file
    output_file.close()
# define the first display for user selection
def first_display(user_choice):
    # Display the different options to the user
    print("Choose an option")
    print("Enter 1 to look up an email address, 2 to add a new name and email")
    print("3 to change an existing email and 4 to delete an existing name and email")
    print("press 5 to display all names and emails or press 0 to quit")

# define the menu
def menu(user_choice, name_email):
    # get user choice
    user_choice = int(input("Enter choice: "))
    # make it so the selection must be 1 to 5
    while user_choice > 0 and user_choice < 6:
        # user chose 1 to search for an email
        if user_choice == 1:
            # get the name of the person they want to search for
            search = input("Enter the name of the person you want an email for (format is First Last): ")
            # if the name exists display the result
            if search in name_email:
                print('The email for', search, 'is ', name_email[search])
            # If the name does not exist ask if they want to add it and tell them to choose option 2
            else:
                print("The email for", search, "was not found.")
                print("If you would like to add it please choose option 2")
        # if user chose 2 then they will add an email to dictionary
        elif user_choice == 2:
            # User enters the name to add
            name_add = input("Enter the First Lastname for the name that needs added: ")
            # User enters the email to add
            email_add = input(f"Enter the email for {name_add:}: ")
            # Add the entry to the dictionary
            name_email[name_add] = email_add
            # print/validate the result
            print("You added: ", name_add, ":", name_email[name_add])
        # if the user chose 3 they will be changing the email of someone
        elif user_choice == 3:
            # Get name to edit
            name_edit = input("Enter the name of the person you want to change the email for (format is First Last): ")
            # If the name exists then do the edit
            if name_edit in name_email:
                email_edit = input(f'Enter the email you would like to assign for {name_edit:}: ')
                name_email[name_edit] = email_edit
                print("Here is your update: ", name_email[name_edit])
            # If the name does not exist then tell them to choose option 2 to add it
            else:
                print("The email for", name_edit, "was not found.")
                print("If you would like to add it please choose option 2")
        # If the user chose option 4 to remove an email
        elif user_choice == 4:
            # Get the name of the email the user wants to remove
            name_delt = input("Enter the name of the person you want to remove an email for: ")
            # If the name exists then remove it from the dictionary
            if name_delt in name_email:
                del name_email[name_delt]
                print("It is done")
            # If the name does not exist then tell the user it was not found
            else:
                print("The email for", name_edit, "was not found.")
        # If the user chose option 5 then display the name email dictionary
        elif user_choice == 5:
            print("Here are all of the names and emails in the record: ")
            # print the dictionary with pprint so that it is nice and perty for the user
            pprint.pprint(name_email, width=1)
        # if the user chose none of those and somehow stayed in the loop then say oops and exit
        else:
            print("oops")
            exit()
        # ask the user for more input or to quit
        user_choice = int(input("\n Press 0 to quit or make another selection from above: "))
# call main
main()

