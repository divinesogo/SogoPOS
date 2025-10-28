from kivy.app import App
from kivy.uix.label import Label

class SogoPOS(App):
    def build(self):
        return Label(text="Hello from Sogo POS!", font_size=30)

if __name__ == '__main__':
    SogoPOS().run()
