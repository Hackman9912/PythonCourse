while line != "":
        for line in plain_file:
            print("line", line)
            for x in line.lower():
                print("x", x)
                if y in encryption_code:
                    print("y", y)
                    letter = str(encryption_code[y])
                    encoded_file += letter
                    print(letter)
                else:
                    encryption_code += y
            encoded_file.write(letter + '\n')
        line = plain_file.readline()



        print(contents)
    encoded_file = open('encoded.txt', 'w')
    line = plain_file.readlines()
    print("line", contents)