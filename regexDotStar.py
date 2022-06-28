import re
beginsWithHelloRegex = re.compile(r'^Hello') #shoudl appear in the beginning of the string
mo = beginsWithHelloRegex.search('Hello there')

print(mo)
print(mo.group())

mo = beginsWithHelloRegex.search('Hi there')
print(mo)   #---this returns none value

endsWithWordRegex = re.compile(r'world!$')
mo = endsWithWordRegex.search('Hello world!')
print(mo)

allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('12345x6789')
print(mo)