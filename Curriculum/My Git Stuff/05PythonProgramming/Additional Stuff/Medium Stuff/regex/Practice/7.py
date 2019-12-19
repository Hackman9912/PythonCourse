"""
7. Match the set of all valid e-mail addresses (start with a loose
regex, and then try to tighten it as much as you can, yet
maintain correct functionality). Try to break what we did in class 
and improve it.
"""
import re
emails = '''
TestUser@gmail.com
test.user@school.edu
test-123@this-place.net
bademail@.com
range@rover
'''
pattern = re.compile(r'[a-zA-Z.0-9-_+]+@[a-zA-Z0-9-.]+\.[a-zA-Z0-9-.]+') 
matches = pattern.finditer(emails)
for match in matches:
    print(match)