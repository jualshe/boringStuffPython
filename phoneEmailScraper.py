#! /usr/local/bin/python
import re
import pyperclip

# Create regex for phone numbbers
phoneRegex = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?  # area code (optional)
(\s|-)        # firts separator
\d\d\d        # first 3 digits
-        # separator 
\d\d\d\d        # last 4 digits
(((ext(\.)?\s)|x)    #extension (optional)
(\d{2,5}))? )       #extension number-part (optional)
''', re.VERBOSE)

# without the verbose we would use
# re.compile('((\d\d\d) | (\(\d\d\d\)))?(\s|-)\d\d\d-\d\d\d\d(((ext(\.)?\s)|x)(\d{2,5}))?')

# TODO: create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com
[a-zA-Z0-9_.+]+    #name part
@                  # @symbol
[a-zA-Z0-9_.+]+    #domain part
''')

# Get the text off the clipbboard
text = pyperclip.paste()

# EXtract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneN

print(extractedPhone)
print(extractedEmail)
# TODO: copy the extracted email/phone to the clipboard
