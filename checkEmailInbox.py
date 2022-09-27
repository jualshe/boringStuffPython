import imapclient

conn = imapclient.IMAP4_TLS('imap.gmail.com', ssl=True)
# username and password
conn.login('', '')
conn.select_folder('INBOX', readonly=True)
