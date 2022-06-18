import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 650-555-4242')
print(mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 650-555-4242')
print(mo.group())
print(mo.group(1))
print(mo.group(2))

phoneNumRegex = re.compile(r'\(\d\d\d\)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (650)-555-4242')
print(mo.group())

#pipes
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
