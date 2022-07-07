import re

beginsWithHelloRegex = re.compile(r'^Hello')  # shoudl appear in the beginning of the string
mo = beginsWithHelloRegex.search('Hello there')

print(mo)
print(mo.group())

mo = beginsWithHelloRegex.search('Hi there')
print(mo)  # ---this returns none value

endsWithWordRegex = re.compile(r'world!$')
mo = endsWithWordRegex.search('Hello world!')
print(mo)

allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('123456789')
print(mo)

mo = allDigitsRegex.search('12345x6789')
print(mo)

# anything except newline

# atRegex = re.compile(r'..at')
atRegex = re.compile(r'.{1,2}at')
mo = atRegex.findall('The cat inn the hat sat on the flat mat')
print(mo)

# dot star pattern .*

a = 'First Name: Al Alik Last Name: Sweigart'
print(a.find(':'))
print(a.find(':') + 2)
print(a[12:])

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.findall(a)
print(mo)
