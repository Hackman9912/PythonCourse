
import pickle
output_file = open('information.dat', 'wb+')
end_of_file = False

    
    

while not end_of_file:
        try:
            # Unpuckle the file
            name_email = pickle.load(output_file)

            # Display the object
            print(name_email)
        except:
            # set the flag to indicate end of file has been reached
            end_of_file = True
output_file.close()