"""
9. type(). The type() built-in function returns a type object,
which is displayed as the following Pythonic-looking string:

    # >>> type(0)
    # <type 'int'>
    # >>> type(.34)
    # <type 'float'>
    # >>> type(dir)
<type 'builtin_function_or_method'>

10. Create a regex that would extract the actual type name from
the string. Your function should take a string like this <type
'int'> and return int. (Ditto for all other types, such as
‘float’, ‘builtin_function_or_method’, etc.) Note: You
are implementing the value that is stored in the __name__
attribute for classes and some built-in types.
"""
import re
type1 = '''<type 'int'>
<type 'float'>
<type 'builtin_function_or_method'>
'''
stuff = re.findall(r"'(.*?)'", type1)
for match in stuff:
    print(match)

# pattern = re.compile(r"(['])([a-zA-Z_]+)(['])") 
# matches = pattern.finditer(type1)
# for match in matches:
#     print(match.group(2))