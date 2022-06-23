import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneRegex.search('543-333-4444')
print(mo.group())

mo = phoneRegex.findall('hi there aloha 540-333-2222 and 111-222-3456')
print(mo)