import smtplib
from Tkinter import *
amount = 1
fromemail = "email@email.com"
username = "email@email.com"
password = "password"
rb = ""
smtpserver='"smtp.gmail.com:587"'
grayoutgmail = ""
grayouthotmail = ""
grayoutyahoo = ""
ungray = ""
login = ""
master = Tk()
master.title("Email Program By Kresten")
#master.iconbitmap('favicon.ico')
class Email:
    def __init__(self,master):
        self.var = IntVar()
        frame = Frame(master)
        frame.grid()
        f2 = Frame(master,width=300,height=300)
        f2.grid(row=0,column=1)

def closeprogram():
    raise SystemExit

def send():
    toemail = e.get()
    username = e2.get()
    password = e1.get()
    message = e3.get()
    spoof = e6.get()
    server=smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username, password)
    server.sendmail(spoof, toemail, message)
    amount = e7.get()
    print amount
    i = 1 
    while i < int(amount):
        print(i)
        server.sendmail(spoof, toemail, message)
        i = i+1
    server.quit()

def callback():
    print("hi")

def grayouthotmail():
    e5.configure(state=DISABLED)
	smtpserver = '"smtp.live.com:587"'
	print smtpserver
	
def grayoutgmail():
	e5.configure(state=DISABLED)
	smtpserver = '"smtp.gmail.com:587"'
	print smtpserver
	
def grayoutyahoo():
	e5.configure(state=DISABLED)
	smtpserver = '"smtp.mail.yahoo.com:465"'
	print smtpserver

def ungray():
    e5.configure(state=NORMAL)
	login = e8.get()
	print(login)
	if login == "admin321":
		print ("Success") 


b = Button(master, text="Send", command=send, width=20, height=10)
b.grid()

e8 = Entry(master, width=35)
e8.grid()

b1 = Button(master, text="Exit", command=closeprogram)
b1.grid()

r1 = Radiobutton(master, text="GMail", variable=rb, value=1, command=grayoutgmail)
r1.grid()
r2 = Radiobutton(master, text="Yahoo", variable=rb, value=2, command=grayoutyahoo)
r2.grid()
r3 = Radiobutton(master, text="Bing", variable=rb, value=3, command=grayouthotmail)
r3.grid()
r4 = Radiobutton(master, text="Other", variable=rb, value=4, command=ungray)
r4.grid()
r1.invoke()

l7 = Label(text="Amount of emails (only numbers)")
l7.grid()
e7 = Entry(master, width=30)
e7.grid()

l6 = Label(text="From Email")
l6.grid()
e6 = Entry(master, width=30)
e6.grid()


l5 = Label(text="(smtp.server:port) e.g: smtp.gmail.com:587")
l5.grid()
e5 = Entry(master, width=30, state=NORMAL)
e5.grid()
e5.configure(state=DISABLED)

l3 = Label(text="Message")
l3.grid()
e3 = Entry(master, width=30)
e3.grid()

l2 = Label(text="To Email")
l2.grid()
e = Entry(master, width=30)
e.grid()

l1 = Label(text="Password")
l1.grid()
e1 = Entry(master, width=30, show="*")
e1.grid()

l = Label(text="Your email")
l.grid()
e2 = Entry(master, width=30)
e2.grid()

l4 = Label(text=" ")
l4.grid()

app = Email(master)
mainloop()
