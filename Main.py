from kivy.app import App
from kivy.lang import Builder
import math
import re


class CalculatorApp(App):
    def build(self):
        self.operand = ""
        return Builder.load_file("calculator.kv")

    def on_button_press(self, instance):
        text = instance.text
        label = self.root.ids.result_label

        if text == "C":
            self.operand = ""
            label.text = "0"

        elif text == "=":
            try:
                expression = self.operand

                expression = expression.replace("^", "**")

                expression = re.sub(r'√(\d+)', r'math.sqrt(\1)', expression)

                expression = re.sub(r'sin\((.*?)\)', r'math.sin(math.radians(\1))', expression)
                expression = re.sub(r'cos\((.*?)\)', r'math.cos(math.radians(\1))', expression)
                expression = re.sub(r'tan\((.*?)\)', r'math.tan(math.radians(\1))', expression)

                self.operand = str(eval(expression))
                label.text = self.operand

            except Exception as e:
                label.text = "Error"
                self.operand = ""
                print(f"Error: {e}")

        else:
            if text in "+-*/" and (self.operand == "" or self.operand[-1] in "+-*/"):
                return

            if text in ["sin", "cos", "tan"]:
                self.operand += f"{text}("

            elif text == "√":
                self.operand += "√"

            else:
                self.operand += text

            label.text = self.operand
            print(f"Apăsat: {text}, Operand: {self.operand}")


if __name__ == "__main__":
    CalculatorApp().run()
