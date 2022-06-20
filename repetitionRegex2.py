import re

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d\-\d\d\d\d')
mo = phoneRegex.search('My phone number is 650-555-4242') #match object
print(mo.group())


mo = phoneRegex.search('My phone number is 555-4242') #match object
print(mo.group())