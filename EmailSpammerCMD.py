#!/usr/local/bin/python
import smtplib, getpass, os, sys
amount = 1
if sys.argv[1] == "-h" or sys.argv[1] == "-help":
    print "EmailSpammerCMD.py {your email} {password} {smtp server(smtp.gmail.com:587)} {reciever email} {message (in quots)} {amount}"
    sys.exit()
fromemail = sys.argv[1]
password = sys.argv[2]
smtpserver = sys.argv[3]
toemail = sys.argv[4]
message = sys.argv[5]
amount = sys.argv[6]
server=smtplib.SMTP(smtpserver)
server.starttls()
server.login(fromemail, password)
server.sendmail(fromemail, toemail, message)
print "Sending "+amount+" emails"
i = 1
while i < int(amount):
    print(i)
    server.sendmail(fromemail, toemail, message)
    i = i+1
print i
server.quit()

#fromemail = "example@example.com"
#username = "example@example.com"
#password = "password"
#smtpserver = '"smtp.gmail.com:587"'
