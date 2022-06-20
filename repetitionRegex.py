import re

batRegex = re.compile(r'Bat(wo)?man')

mo = batRegex.search('The adventures of Batman')
print(mo.group())

mo = batRegex.search('The adventures of Batwoman')
print(mo.group())

mo = batRegex.search('The adventures of Batwowowowoman')
mo = None #True