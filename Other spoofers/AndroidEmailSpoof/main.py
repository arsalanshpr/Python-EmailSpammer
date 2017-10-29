#!/usr/local/bin/python
import smtplib
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import kivy
#End of imports

class MainScreen(Screen):
        pass

class AnotherScreen(Screen):
        pass

class AnotherScreen2(Screen):
        pass

class ScreenManagement(ScreenManager):
        pass

#class EmailSpoofer(Widget):
#        def on_touch_down(self,touch):
#                run_once = 0
#                while run_once < 1:
#                        server=smtplib.SMTP("smtp.gmail.com:587")
#                        server.starttls()
#                        server.login("coc.gamer66@gmail.com", "12341234ks")
#                        print("Email sent")
#                        server.sendmail("coc.gamer66@gmail.com", "kressckerl@gmail.com", "Hello")
#                        server.quit()
#                        run_once = 1
#                print("Done")

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
                run_once = 0
                while run_once < 1:
                        server=smtplib.SMTP("smtp.gmail.com:587")
                        server.starttls()
                        server.login("coc.gamer66@gmail.com", "12341234ks")
                        print("Email sent")
                        server.sendmail("coc.gamer66@gmail.com", "kressckerl@gmail.com", "Hello")
                        server.quit()
                        run_once = 1

presentation = Builder.load_file("main1.kv")

class EmailSpoof(App):
        def build(self):
                return presentation

EmailSpoof().run()
