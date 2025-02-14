from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operand = ""
        self.result_label = Label(text="0", font_size=40, size_hint=(1, 0.3))

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.result_label)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=32)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.operand = ""
            self.result_label.text = "0"
        elif text == "=":
            try:
                self.operand = str(eval(self.operand))
                self.result_label.text = self.operand
            except:
                self.result_label.text = "Error"
                self.operand = ""
        else:
            self.operand += text
            self.result_label.text = self.operand

if __name__ == "__main__":
    CalculatorApp().run()
