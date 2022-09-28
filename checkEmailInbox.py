import imapclient, pyzmail

conn = imapclient.IMAP4_TLS('imap.gmail.com', ssl=True)
# username and password
conn.login('', '')
conn.select_folder('INBOX', readonly=True)
# returns unique IDs
UIDs = conn.search(['SINCE 20-Sep-2022'])
# translate id to emails
rawMEssage = conn.fetch([47474], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMEssage[47474][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')

message.text_part == None
message.html_part == None

message.text_part.charset == None
# if True - then the decode will bbe UTF-8
message.text_part.get_payload().decode('UTF-8')
conn.logout()
