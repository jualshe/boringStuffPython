import re
#\d numeric from 0 to 9
digitRegex = re.compile(r'(0|1|2|3|4|5|6|7|8|9|)')
#same as
digitRegex = re.compile(r'\d')

# \D any character that is not a numeric digit from 0 to 9
# \w any letter, numeric, or undescore character  'word'
# \W any numeric that is not a letter, numeric or undescoree
# \s any space, tab or new line character
# \S any character that is not a space, tab or new line


lyrics = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans'

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(lyrics)
print(mo)

#making your own character classes

vowelRegex = re.compile(r'[aeiouAEOIU]') #r'(a|e|i|o|u)' (longer)
# (r'[a-z]') or (r'[a-f]') or (r'[A-F]')

mo = vowelRegex.findall('Robocop eats baby food.')
print(mo)

doubbleVowelRegex = re.compile(r'[aeiouAEOIU]{2}') #match two vowels in a row

mo = doubbleVowelRegex.findall('Robocop eats baby food.')
print(mo)

#neagtive character classes
consonantsRegex = re.compile(r'[^aeiouAEOIU]') #find all instead of selected
mo = consonantsRegex.findall('Robocop eats baby food.')
print(mo)

consonantsRegex = re.compile(r'[^aeiouAEOIU]{2}') #find all instead of selected and match two in  a row
mo = consonantsRegex.findall('Robocop eats baby food.')
print(mo)