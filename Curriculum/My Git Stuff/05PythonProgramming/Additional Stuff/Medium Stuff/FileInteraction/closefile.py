# Removes the need to close the file at the end
with open(r'C:\Users\student\Documents\philosophers.txt', 'r') as file:
    size_to_read = 50
    f_contents = file.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end = '-')
        f_contents = file.read(size_to_read)
    