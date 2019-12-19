"""
11. Processing Dates. In Section 1.2, we gave you the regex pattern
that matched the single or double-digit string representations of
the months January to September (0?[1-9]). Create the regex
that represents the remaining three months in the standard
calendar.
"""
import re
months = '''01
2
03
04
05
06
07
08
09
10
11
12
'''
pattern = re.compile(r'(\b(0?[1-9])\b|\b(1[1-2])\b)') 
matches = pattern.finditer(months)
for match in matches:
    print(match)