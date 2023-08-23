"""smtp for sending mail using python"""

# import smtplib
# sender_mail = 'shaheen.fatma696@gmail.com'
# receivers_mail="amber.fatimaa696@gmail.com"
# password="eiljkjkbjvhmlxyt"
# message ='Subject:hiii\n\nthis is great'
# with smtplib.SMTP("smtp.gmail.com")  as c:
#    c.starttls()#security
#    c.login(user=sender_mail,password=password)
#    c.sendmail(from_addr=sender_mail,to_addrs= receivers_mail, msg=message)
#    print("Successfully sent email")
#
import random
import smtplib
import datetime as dt

with open("quotes.txt","r") as f:
   a=f.readlines()


today=dt.datetime.now()
weekday=today.weekday()
if weekday in range(7):# wednesday=2
   sender_mail = 'shaheen.fatma696@gmail.com'
   receivers_mail="amber.fatimaa696@gmail.com"
   password="eiljkjkbjvhmlxyt"
   message =f'Subject:Motivation quotes\n\n{random.choice(a)}'
   with smtplib.SMTP("smtp.gmail.com")  as c:

      c.starttls()#security
      c.login(user=sender_mail,password=password)
      c.sendmail(from_addr=sender_mail,to_addrs= receivers_mail, msg=message)
      print("Successfully sent email")

