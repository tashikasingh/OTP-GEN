import smtplib
import random

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_ = 'cgourav472@gmail.com'
your_pass = "waxrfyjsyxoupokx"
generated=''
name=''
id=''
def generate():
    otp=str(random.randrange(100000,999999)) 
    return otp

def establisconn(  name, to, otp):
    body = str("Hello "+name+" your OTP is :"+otp+". Do not share your OTP with anyone else. If you didn't request for an otp, ignore this.")
    subject = 'OTP GENERATOR'
    message = MIMEMultipart()
    message['From'] = from_
    message['To'] = to
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    text = message.as_string()
    return text

def send(text, to):
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(from_,your_pass)
    mail.sendmail(from_,to, text)
    mail.close()