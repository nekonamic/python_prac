from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class DynamicLabel(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_of_name = ['a', 'b', 'c']
