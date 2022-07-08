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

# greedy/non-gready matching

serve = '<To serve humans> for dinner. kaka!>>'

nongreedy = re.compile(r'<(.*?)>')
mo = nongreedy.findall(serve)
print(mo)

greedy = re.compile(r'<(.*)>')
mo = greedy.findall(serve)
print(mo)

prime = '\nServe the pubblic trust. \nProtect the innocent. \nUpload the law.\n'
print(prime)

# greedy doesn't include the new line
dotStar = re.compile(r'.*')
mo = dotStar.search(prime)
print(mo)

# the way to include everything
dotStar = re.compile(r'.*', re.DOTALL)
mo = dotStar.search(prime)
print(mo)

# case insensitive regular expression match

vovelRegex = re.compile(r'[aeiou]')
mo = vovelRegex.findall('Al, why your programming book talks about Robbocop so much')
print(mo)

vovelRegex = re.compile(r'[aeiou]', re.IGNORECASE)  # re.IGNORECASE = re.I
mo = vovelRegex.findall('Al, why your programming book talks about Robbocop so much')
print(mo)
