'''
import smtplib

from email.mime.text import MIMEText
host = "smtp.gmail.com"
port = 587
username = "Hungyu.Wei@abilitycorp.com.tw"
password = "/.,mn09876"
from_email = username
to_list = ["Hungyu.Wei@abilitycorp.com.tw"]
#to_list = ["e94971360@livemail.tw"]
try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    the_msg['Subject'] = "Hello there!"
    the_msg["From"] = from_email
    #the_msg["To"]  = to_list[0]
    plain_txt = "Testing the message"
    email_conn.sendmail(from_email, to_list, plain_txt.as_string())
    email_conn.quit()
except smtplib.SMTPException:
    print("error sending message")
yyyyy")
me = "Hungyu.Wei@abilitycorp.com.tw"
you = "Hungyu.Wei@abilitycorp.com.tw"
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
'''
to_list = ["Hungyu.Wei@abilitycorp.com.tw","Tim.Lee@abilitycorp.com.tw","Panda.Wang@abilitycorp.com.tw"]
import win32com.client as win32
for maillist in to_list:
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    print(maillist)
    mail.To = maillist
    mail.Subject = '訂便當'
    mail.Body = '趕快訂便當'
    mail.Send()
