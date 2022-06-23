import re
# ? means 0 or one
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

# {}specific number of repetition

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('She said "HaHaHa" ')
print(mo.group())

haRegex = re.compile(r'HaHaHa')
mo = haRegex.search('She said "HaHaHa" ')
print(mo.group())

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )?){3}')
mo = phoneRegex.search('My numbers are 415-555-1234, 555-4242, 650-123-4567')
print(mo.group())


haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('She said "HaHaHa" ')
print(mo.group())

mo = haRegex.search('She said "HaHaHaHaHaHaHa" ')
print(mo.group())

haRegex = re.compile(r'(Ha){3,}')
mo = haRegex.search('She said "HaHaHaHaHaHaHa" ')
print(mo.group())

digitRegex = re.compile(r'(\d){3,5}') #greedy match
mo = digitRegex.search('123456789')
print(mo.group())

digitRegex = re.compile(r'(\d){3,5}?') #non-greedy match
mo = digitRegex.search('123456789')
print(mo.group())