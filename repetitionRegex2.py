import re

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d\-\d\d\d\d')
mo = phoneRegex.search('My phone number is 650-555-4242') #match object
print(mo.group())

mo = phoneRegex.search('My phone number is 555-4242') #match object
print(mo.group())

# * - match 0 or more times

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The adventure of Batman')
print(mo.group())

mo = batRegex.search('The adventure of Batwowowowowoman')
print(mo.group())

# + one or more (not optional as *)
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The adventure of Batman') #doens't show in the results
mo = batRegex.search('The adventure of Batwoman') #wo is shown at least once
print(mo.group())

#literal symbols matching
regex = re.compile(r'\+\*\?')
mo = regex.search('I am learning about +*? regex syntax')
print(mo.group())