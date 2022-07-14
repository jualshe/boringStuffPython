import re

re.compile(r'''
\d\d\d      #area code
-           #1st dash
\d\d\d      #first 3 digits
-           #second dash
\d\d\d\d    #last 4 digits''', re.VERBOSE)
