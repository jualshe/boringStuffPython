import smtplib

connection = smtplib.SMTP('smtp.gmail.com', 587)
type(connection)

print(connection)

connection.ehlo()
print(connection.ehlo())
connection.starttls()

# enter email and password
connection.login('', '')
# enter email from and email to
connection.sendmail('', '', 'Subject: test subject \n\n Hi there! \n how are you? \n\n - Julia ')
