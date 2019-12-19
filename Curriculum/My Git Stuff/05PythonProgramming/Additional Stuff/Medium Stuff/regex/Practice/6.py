"""
6. Match simple Web domain names that begin with “www.”
and end with a “.com” suffix; for example, www.yahoo.com.
Extra Credit: If your regex also supports other high-level
domain names, such as .edu, .net, etc. (for example,
www.foothill.edu).
"""
import re
urls = '''www.yahoo.com
http://testsite.com
https://www.google.com
www.bob.com
https://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r'(^|\s)[w]{3}\.\w+\.\w+') 
matches = pattern.finditer(urls)
for match in matches:
    print(match)