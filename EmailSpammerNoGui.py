#!/usr/local/bin/python
import smtplib, getpass, os, sys, subprocess
amount = 1
fromemail = "example@example.com"
username = "example@example.com"
password = "password"
smtpserver = '"smtp.gmail.com:587"'
fromemail = raw_input("Please enter your email: ")
print ("Please enter your password(the text will be hidden): ")
password = getpass.getpass()
smtpserver = raw_input("Enter smtpserver, googles is: smtp.gmail.com:587: ")
toemail = raw_input("Please enter the target email: ")
message = raw_input("Please enter your nice message: ")
amount = raw_input("Please enter amount, a nice start is 50: ")
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
