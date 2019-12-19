'''
3. File Encryption and Decryption
Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For
example:
codes = { 'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', etc...}
Using this example, the letter A would be assigned the symbol %, the letter a would be
assigned the number 9, the letter B would be assigned the symbol @, and so forth.
The program should open a specified text file, read its contents, and then use the dictionary to 
write an encrypted version of the file’s contents to a second file. Each character in
the second file should contain the code for the corresponding character in the first file.
'''
# define main
def main():
    # open the files to work with
    plain_file = open('plain.txt', 'r')
    encoded_file = open('encoded.txt', 'w')
    # set the read line
    line = plain_file.readline()
    # set dictionary of encryption keys
    encryption_code = {
        "a": '1', "b": '3', "c": '5',
        "d": '7',"e": '9', "f": '/',
        "g": '!', "h": '*', "i": '?',
        "j": '@',"k": '(', "l": '>',
        "m": '#', "n": ')', "o": '<',
        "p": '$', "q": ';', "r": '+',
        "s": '%', "t": ':', "u": '=',
        "v": '^',"w": ',',"x" : '~',
        "y": '&', "z": '.'," " : "`",
        "." : 'g', "," : 'c', "!" : 'E',
        "?" : 'q', "\n" : "\n"
    }
    # while line is true
    while line:
        # iterate through each letter as it is lowercased
        for x in line.lower():
            # see if letter is in the key
            if x in encryption_code:
                # if it is replace it and write it to the encrypted file
                code = x.replace(x, encryption_code[x])
                encoded_file.write(code)
        # look at the next line
        line = plain_file.readline()
# call main
main()