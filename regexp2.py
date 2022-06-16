import re

# message = 'Call me 650-440-0172 tomorrow, or 650-440-0172 '

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Call me 650-440-1111 tomorrow, or 650-440-0000 for my office line')
print('found numbers: ' + str(mo))
