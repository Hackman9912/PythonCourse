"""
1. Pet Class
    Write a class named Pet, which should have the following data attributes:
        • __name (for the name of a pet)
        • __animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’,
        and ‘Bird’)
        • __age (for the pet’s age)
        The Pet class should have an __init__ method that creates these attributes. It should also
        have the following methods:
        • set_name
        This method assigns a value to the __name field.
        • set_animal_type
        This method assigns a value to the __animal_type field.
        • set_age
        This method assigns a value to the __age field.
        • get_name
        This method returns the value of the name field.
        • get_type
        This method returns the value of the type field.
        • get_age
        This method returns the value of the age field.
    Once you have written the class, write a program that creates an object of the class and
    prompts the user to enter the name, type, and age of his or her pet. This data should be
    stored as the object’s attributes. Use the object’s accessor methods to retrieve the pet’s name,
    type, and age and display this data on the screen.

"""
import Pet

def main():
    pet = petlist()
    showpet(pet)

def petlist():
    pet_list = []
    print("Enter the number of pets to enter data for: ")
    for count in range(int(input())):
        print('Pet number', count + 1)
        name = input("Enter the pets name: ")
        atype = input("Enter the type of pet: ")
        age = int(input("Enter the age of the pet in years: "))
        print()

        pets = Pet.Pet(name, atype, age)

        pet_list.append(pets)
    return pet_list

def showpet(pet_list):
    if len(pet_list) > 0:
        print("\n" * 100)
        print("Here is the data you entered: ")
        for friend in pet_list:
            print()
            print("Name: ", friend.get_name())
            print("Type: ", friend.get_atype())
            print("Age: ", friend.get_age())
            print('....................')
    else:
        print("Looks like there are no pets here...")
        print("The cat wins again....")

main()