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