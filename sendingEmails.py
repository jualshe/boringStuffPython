import smtplib

connection = smtplib.SMTP('smtp.mail.yahoo.com', 465)
# smtp.gmail.com
type(connection)

print(connection)

connection.ehlo()
print(connection.ehlo())
connection.starttls()

# enter email and password
connection.login('shevchenkoj@yahoo.com', '')
# enter email from and email to
connection.sendmail('shevchenkoj@yahoo.com', 'shevchenkoj@yahoo.com',
                    'Subject: test subject \n\n Hi there! \n how are you? \n\n - Julia ')

connection.quit()
