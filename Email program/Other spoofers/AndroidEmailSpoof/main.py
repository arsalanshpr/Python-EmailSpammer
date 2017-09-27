import smtplib
#import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
#End of imports

class MainScreen(Screen):
        pass

class AnotherScreen(Screen):
        pass

class ScreenManagement(ScreenManager):
        pass

class Painter(Widget):
        
        def on_touch_down(self, touch):
                print(touch)
                with self.canvas:
                        touch.ud["line"] = Line(points=(touch.x, touch.y))

        def on_touch_move(self, touch):
                print(touch)
                touch.ud["line"].points += (touch.x, touch.y)

        def on_touch_up(self, touch):
                print("Moved finger",touch)

class EmailSpoofer():
        def send():
                toemail = "kressckerl@gmail.com"
                username = "coc.gamer66@gmail.com"
                password = "12341234ks"
                message = "Hello"
                spoof = "coc.gamer66@gmail.com"
                server=smtplib.SMTP("smtp.gmail.com:587")
                server.starttls()
                server.login(username, password)
                server.sendmail(spoof, toemail, message)
                print("Email sent")

presentation = Builder.load_file("main1.kv")



#Starting Class
class EmailSpoof(App):
        def build(self):
                return presentation #Before return DrawInput()
#               return Button(text="hello world").bind(on_press=callback)
#       
#               
#def callback(instance):
#       print("Hello world" % instance.text)
#       
#b = Button(text="Test1")
#b.bind(on_press=callback)
#textinput = TextInput(text='Hello world')
EmailSpoof().run()
