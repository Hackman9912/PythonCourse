"""
8. Match the set of all valid Web site addresses (URLs) (start
with a loose regex, and then try to tighten it as much as you
can, yet maintain correct functionality).Try to break what we did in 
class and improve it.
"""
import re
urls = '''www.yahoo.com
http://testsite.com
https://www.google.com
www.bob.com
https://youtube.com
https://www.nasa.gov
bob.com
'''
pattern = re.compile(r'(http|https)?(://)?([w]{3}\.)?\w+\.\w+\b') 
matches = pattern.finditer(urls)
for match in matches:
    print(match)