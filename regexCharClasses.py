import re

digitRegex = re.compile(r'(0|1|2|3|4|5|6|7|8|9|)')
#same as
digitRegex = re.compile(r'\d')

# \D any character that is not a numeric digit from 0 to 9
# \w any letter, numeric, or undescor character  'word'
# \W any numeric that is not a letter, numeric or undescore