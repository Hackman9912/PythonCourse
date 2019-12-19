# Regular Expressions or RegEx

import re

text_to_match = '''lol
Daniel 1234 abcd
this.thing@email.com
this_otherthing@email.com
    there_was_a_tab
    210-444-4444
888*888*8888
800-555-5555
900-111-1234
lol
lol lololol
lol
cat mat pat bat sat hat rat
Mr. Anderson
Mr Smith
Ms. Davis
Mrs. Robinson
Mr. T
'''


# *************************************** String Literals ******************************************
'''print('\tTab')


# compile() will allow us to separate our pattern matches into a variable that makes it easier to reuse our variable
pattern = re.compile(r'1234')

# match()
# determines if the regex matches at the beginning of the string. Returns none if its not at beginning, same as ^ anchor
match = pattern.match(text_to_match)
print(match)


# search() lets us search the entire string so it is better than match
search_item = pattern.search(text_to_match)
print(search_item)

# finditer()
pattern = re.compile(r'abcd')
matches = pattern.finditer(text_to_match)

for match in matches:
    print(match)'''


# ************************************** Meta Characters ****************************

'''
# . - the period or dot will find any character except new line
pattern = re.compile(r'.')
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# use . to find any character and \. to find any actual period or dot
pattern = re.compile(r'\.') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# \d finds any digits 0 to 9
pattern = re.compile(r'\d') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# The \D finds any non digit from 0 to 9
# Capitals essentially negate 
pattern = re.compile(r'\D') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# The \w finds any Word character (a-z, A-Z, 0-9 and _)
pattern = re.compile(r'\w') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# the \W finds any non Word characters.. the opposite of above
pattern = re.compile(r'\W') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# the \s finds any Whitespace (spaces, tabs, new lines)
pattern = re.compile(r'\s') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# the \S finds anything that is not space, tab or newline so similar to \w but has special characters
pattern = re.compile(r'\S') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)
'''

#**************************** Anchors ****************************************
# Anchors don't match characters but match invisible positions before or after characters
'''
# \b - finds word boundaries(anything prefixed with start of a new line, start of a string, tabs)
#  ie the spaces in front of the character. Use \b+the word that you want it to find. So \blol so finds the space in front of the word we search for and the word
pattern = re.compile(r'\blol') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# \B - finds nonword boundaries. So no spaces in between
pattern = re.compile(r'\Blol') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# ^ - finds matches at beginning of strings. Used as ^ + the text you want
pattern = re.compile(r'^lol') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# $ find matches at end of the string: used as the text you want + $
pattern = re.compile(r'lol$') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# Combining things
# find 3 numbers in a row
pattern = re.compile(r'\d\d\d') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# find phone numbers
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# [] are called a character set. They are used to search a group of characters. For the brackets you do not have to escape the characters. It also only matches a single character
pattern = re.compile(r'\d\d\d[-*]\d\d\d[-*]\d\d\d\d') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)
    

pattern = re.compile(r'[89]00[-*]\d\d\d[-*]\d\d\d\d') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# the - can be used to find a range of values can use the | (pipe) to be or: [a-d]|[A-D]. Can also just use them in the same bracket[a-dA-D].
pattern = re.compile(r'[a-dA-D]') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# if the ^ is used in a set it means negate whatever is in the set
pattern = re.compile(r'[^a-zA-Z]') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# match cat, mat, pat but not bat
pattern = re.compile(r'[^b]at') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)
'''
#************************** Quantifiers *********************
'''
# Match more than one character at once. Define what you want to find then {the number of them you want}. IE \d{3}

pattern = re.compile(r'\d{3}.\d{3}.\d{4}') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# the ? is find 0 or 1 match. Goes after the character you dont care if it has. IE Mr\.? so you use \ to escape the . and have it be literal and ? to say look for 1 or 0 of them
pattern = re.compile(r'Mr\.') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

pattern = re.compile(r'Mr\.?') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# + finds one or more
# The below finds Mr with or without a . some white space, a capital and 1 or more word characters
pattern = re.compile(r'Mr\.?\s[A-Z]\w+') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# splat is zero or more
# Gets mr T because of *
pattern = re.compile(r'Mr\.?\s[A-Z]\w*') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)

# () - groups allow us to match several different patterns
# Here we can match an 'M' an 'r' or 's' or 'rs'
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') 
matches = pattern.finditer(text_to_match)
for match in matches:
    print(match)
'''
# Find emails
emails = '''
TestUser@gmail.com
test.user@school.edu
test-123@this-place.net
bademail@.com
'''
'''
# match the first email address. The below will match the first email because it looks for any case of character and any number of char @ any case of character and any number of char .com
pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com') 
matches = pattern.finditer(emails)
for match in matches:
    print(match)

# include literal . in the set and | edu at the end
pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)') 
matches = pattern.finditer(emails)
for match in matches:
    print(match)

# include numbers and - in the set on both sides of the at add | net
pattern = re.compile(r'[a-zA-Z.0-9-]+@[a-zA-Z-]+\.(com|edu|net)') 
matches = pattern.finditer(emails)
for match in matches:
    print(match)

# find any email
pattern = re.compile(r'[a-zA-Z.0-9-_+]+@[a-zA-Z0-9-.]+\.[a-zA-Z0-9-.]+') 
matches = pattern.finditer(emails)
for match in matches:
    print(match)
'''





## Groups
urls = '''
http://testsite.com
https://www.google.com
https://youtube.com
https://www.nasa.gov
'''

'''
# We can group all of these to grab groups. Group 0 being all gorups then gorup 1 being the first group. Using the .group() we can see the specific groups of () groups we look for in our re.compile
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') 
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(0,1,2,3))

# substitute out groups 2 and 3 for our urls every time it finds a match
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') 
subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

# findall() - returns matches as a list of strings. It also uses groups to make the list
pattern = re.compile(r'(Mr|Ms|Mrs)(\.?)(\s[A-Z]\w*)') 
matches = pattern.findall(text_to_match)
for match in matches:
    print(match)

# If there are no groups it returns a list of strings
# If there is one group it returns that group as a list of strings
# If there are more than one groups it returns a list of tuples
pattern = re.compile(r'[a-zA-Z.0-9-_+]+@[a-zA-Z0-9-.]+\.[a-zA-Z0-9-.]+') 
matches = pattern.findall(emails)
for match in matches:
    print(match)
'''


# Flags
string = 'I cAan TyPeE GoOd'

'''
# The flag re.IGNORECASE, IGNORECASE is the flag and it....ignores case
# There are other flags
# They all have a shorthand version. IGNORECASE shorthand is I
pattern = re.compile(r'[ao]', re.IGNORECASE) 
matches = pattern.findall(string)
for match in matches:
    print(match)
'''