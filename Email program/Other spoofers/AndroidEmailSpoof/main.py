import smtplib
import kivy
from kivy.app import App
from kivy.uix.button import Button


class EmailSpoof(App):
	def build(self):
		return Button(text="Testing text")
		
def callback(instance):
	print("Hello world" % instance.text)
	
b = Button(text="Test1")
b.bind(on_press=callback)

EmailSpoof().run()
