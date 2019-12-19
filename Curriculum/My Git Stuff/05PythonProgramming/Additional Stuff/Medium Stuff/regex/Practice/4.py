"""
4. Match the set of all valid Python identifiers.
"""
import re
text = '''
Manpower
manpower
_manpower
myClass
var_1
1var
!Whatever
FalseBob
classRed
f@lse
'''
pattern = re.compile(r'(^)(?!False|class|finally|is|return|None |ontinue|for|lambda|try|True|def|from|nonlocal|while|and|del|global|not|with|as|elif|if|or|yield|assert|else|import|pass|break|except|in|raise|!|@|#|$|%)([a-zA-Z_][a-zA-Z_0-9]+)\b', re.MULTILINE)
matches = pattern.finditer(text)
for match in matches:
    print(match)

