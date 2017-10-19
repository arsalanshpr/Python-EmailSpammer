from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line
#End of imports
class DrawInput(Widget):
        
        def on_touch_down(self, touch):
                print(touch)
                with self.canvas:
                        touch.ud["line"] = Line(points=(touch.x, touch.y))

        def on_touch_move(self, touch):
                print(touch)
                touch.ud["line"].points += (touch.x, touch.y)

        def on_touch_up(self, touch):
                print("Moved finger",touch)

#Starting Class
class DrawAway(App):
        def build(self):
                return DrawInput() #starts "DrawInput" class

DrawAway().run()
