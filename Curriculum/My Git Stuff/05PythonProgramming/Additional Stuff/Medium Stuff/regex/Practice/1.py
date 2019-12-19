"""
1. Recognize the following strings: “bat”, “bit”, “but”, “hat”,
“hit”, or “hut”.
"""
import re
string = '''
bat bit but hat hit hut
'''
pattern = re.compile(r'[a-z]{2}t')
matches = pattern.finditer(string)
for match in matches:
    print(match)
