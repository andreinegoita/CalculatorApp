from kivy.app import App
from kivy.lang import Builder
import math
import cmath
import re

class CalculatorApp(App):
    def build(self):
        self.operand = ""
        self.memory = None
        self.scientific_mode = False
        return Builder.load_file("calculator.kv")

    def on_button_press(self, instance):
        text = instance.text
        label = self.root.ids.result_label

        if text == "C":
            self.reset()
        elif text == "=":
            self.evaluate_expression(label)
        elif text == "M+":
            self.memory = self.operand
        elif text == "MR":
            self.recall_memory(label)
        elif text == "MC":
            self.clear_memory()
        elif text == "Mode":
            self.toggle_scientific_mode()
        else:
            self.append_operand(text, label)

    def reset(self):
        self.operand = ""
        self.root.ids.result_label.text = "0"

    def evaluate_expression(self, label):
        try:
            expression = self.prepare_expression(self.operand)
            self.operand = str(eval(expression))
            label.text = self.operand
        except Exception as e:
            label.text = "Error"
            self.operand = ""
            print(f"Error: {e}")

    def prepare_expression(self, expression):
        expression = expression.replace("^", "**")
        expression = re.sub(r'√(\d+)', r'math.sqrt(\1)', expression)
        expression = re.sub(r'ln\((.*?)\)', r'math.log(\1)', expression)
        expression = re.sub(r'log\((.*?)\)', r'math.log10(\1)', expression)
        expression = re.sub(r'exp\((.*?)\)', r'math.exp(\1)', expression)
        expression = re.sub(r'abs\((.*?)\)', r'math.fabs(\1)', expression)
        expression = re.sub(r'fact\((.*?)\)', r'math.factorial(int(\1))', expression)
        expression = re.sub(r'sin\((.*?)\)', r'math.sin(math.radians(\1))', expression)
        expression = re.sub(r'cos\((.*?)\)', r'math.cos(math.radians(\1))', expression)
        expression = re.sub(r'tan\((.*?)\)', r'math.tan(math.radians(\1))', expression)
        if "j" in expression:
            expression = expression.replace("math.", "cmath.")
        return expression

    def recall_memory(self, label):
        if self.memory:
            self.operand += self.memory
            label.text = self.operand

    def clear_memory(self):
        self.memory = None

    def toggle_scientific_mode(self):
        self.scientific_mode = not self.scientific_mode
        self.update_buttons()

    def append_operand(self, text, label):
        if text in "+-*/" and (self.operand == "" or self.operand[-1] in "+-*/"):
            return
        if text in ["sin", "cos", "tan", "log", "ln", "exp", "abs", "fact"]:
            self.operand += f"{text}("
        elif text == "√":
            self.operand += "√"
        else:
            self.operand += text
        label.text = self.operand

    def update_buttons(self):
        scientific_buttons = ["sin", "cos", "tan", "log", "ln", "exp", "abs", "fact"]
        for btn in self.root.ids:
            if btn in scientific_buttons:
                self.root.ids[btn].opacity = 1 if self.scientific_mode else 0
                self.root.ids[btn].disabled = not self.scientific_mode


if __name__ == "__main__":
    CalculatorApp().run()
