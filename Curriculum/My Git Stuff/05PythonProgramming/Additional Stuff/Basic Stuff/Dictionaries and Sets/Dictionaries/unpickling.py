# import pickle
import pickle

def main():
    # Indicate the end of the file
    end_of_file = False

    input_file = open('information.dat', 'rb')
    # read to the end of the file
    while not end_of_file:
        try:
            # Unpuckle the file
            person = pickle.load(input_file)

            # Display the object
            display_data(person)
        except:
            # set the flag to indicate end of file has been reached
            end_of_file = True

    input_file.close()
# The display data function displays person data in the dictionary that is passed as an arguemtn
def display_data(person):
    # One way to display
    print("Name: ", person['name'])
    print("Age: ", person['age'])
    print("Weight: ", person['weight'])
    print()
    # Another way
    # print(f"'Name: {person['name']} \nAge: {person['age']} \nWeight: {person['weight']} \n")

# Call the main function
main()

