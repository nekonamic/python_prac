from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabel(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_of_name = ['Jill', 'Dorothy', 'Gill']

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.list_of_name:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)

    def clear_all(self):
        self.root.ids.entries_box.clear_widgets()


DynamicLabel().run()
