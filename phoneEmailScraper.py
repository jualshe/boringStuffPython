#! /usr/local/bin/python
import re, pyperclip

# TODO: create regex for phone numbbers
re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext 12345, x12345

((\d\d\d) | (\(\d\d\d\)))?  # area code (optional)
(\s|-)        # firts separator
\d\d\d        # first 3 digits
-        # separator 
\d\d\d\d        # last 4 digits
        #extension (optional)

''', re.VERBOSE)

# TODO: create a regex for email addresses


# TODO: Get the text off the clipbboard

# TODO: EXtract the email/phone from this text

# TODO: copy the extracted email/phone to the clipboard
