import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('sahithi0327@gmail.com','biec ucpz tejc hyqt')
    msg=EmailMessage()
    msg['FROM']='sahithi0327@gmail.com'
    msg['SUBJECT']=subject
    msg['TO']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()

