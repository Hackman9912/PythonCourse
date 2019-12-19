"""
2. Match any pair of words separated by a single space, that is,
first and last names.
"""
import re
text = '''
billy bob
rhonda jane
first last
'''
pattern = re.compile(r'[a-zA-Z]+ [a-zA-Z]+')
matches = pattern.finditer(text)
for match in matches:
    print(match)