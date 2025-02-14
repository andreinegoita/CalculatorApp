from kivy.app import App
from kivy.lang import Builder

from CalculatorUi import CalculatorUI


class CalculatorApp(App):

    def build(self):
        self.ui = CalculatorUI(self)
        return Builder.load_file("calculator.kv")

    def on_button_press(self, instance):
        self.ui.on_button_press(instance)


if __name__ == "__main__":
    CalculatorApp().run()