"""
5. Match a street address according to your local format (keep
your regex general enough to match any number of street
words, including the type designation). For example, American
street addresses use the format: 1180 Bordeaux Drive. Make
your regex flexible enough to support multi-word street
names such as: 3120 De la Cruz Boulevard.
"""
import re
text = '''
1180 Bordeaux Drive
3120 De la Cruz Boulevard
1535 Ft Hammond-Rhine Dr.
'''
pattern = re.compile(r'[0-9]+[\sa-zA-Z.-]+')
matches = pattern.finditer(text)
for match in matches:
    print(match)