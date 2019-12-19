"""
3. Match any word and single letter separated by a comma and
single space, as in last name, first initial.
"""
import re
text = '''
billy, b
rhonda, j
first, l
'''
pattern = re.compile(r'[a-zA-Z]+, [a-zA-Z]')
matches = pattern.finditer(text)
for match in matches:
    print(match)