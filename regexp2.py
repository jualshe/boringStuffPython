import re
message = 'Call me 650-440-0172 tomorrow, or 650-440-0172 '
foundNumbber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found ' +chunk )
        foundNumbber = True
if not foundNumbber:
    print('Could not find any number')