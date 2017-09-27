import smtplib
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class EmailSpoof(App):
	def build(self):
		return Button(text="hello world").bind(on_press=callback)
	
		
def callback(instance):
	print("Hello world" % instance.text)
	
b = Button(text="Test1")
b.bind(on_press=callback)
textinput = TextInput(text='Hello world')

EmailSpoof().run()
