from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):

    def build(self):
        Window.size = (400, 300)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        result = value ** 2
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        self.root.ids.input_number.text = str(int(self.root.ids.input_number.text) + int(change))
        self.handle_calculate(int(self.root.ids.input_number.text))


SquareNumberApp().run()
