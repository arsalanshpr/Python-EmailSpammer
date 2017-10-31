#!/usr/local/bin/python
import smtplib, getpass, os, sys, subprocess
amount = 1
if sys.argv[1] == "-h" or sys.argv[1] == "-help":
    print "EmailSpammerCMD.py {your email} {password} {smtp server(smtp.gmail.com:587)} {reciever email} {message (in quots)} {amount}"
    
fromemail = "example@example.com"
username = "example@example.com"
password = "password"
smtpserver = '"smtp.gmail.com:587"'
fromemail = sys.argv[1]
password = sys.argv[2]
smtpserver = sys.argv[3]
#smtpserver = raw_input("Enter smtpserver, googles is: smtp.gmail.com:587: ")
toemail = sys.argv[4]
#toemail = raw_input("Please enter the target email: ")
message = sys.argv[5]
#message = raw_input("Please enter your nice message: ")
amount = sys.argv[6]
#amount = raw_input("Please enter amount, a nice start is 50: ")
#insert more here

#send function VVV
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
server.quit()
pause = raw_input("Press ENTER to restart the program, or just exit")
os.startfile("EmailSpammerNoGui.py")
os.system('kill $PPID')
