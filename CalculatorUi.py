from MathProcessor import MathProcessor
from MemoryManager import MemoryManager


class CalculatorUI:

    def __init__(self, app):
        self.app = app
        self.operand = ""
        self.scientific_mode = False
        self.memory_manager = MemoryManager()

    def on_button_press(self, instance):
        text = instance.text
        label = self.app.root.ids.result_label

        if text == "C":
            self.reset()
        elif text == "=":
            self.evaluate(label)
        elif text == "M+":
            self.memory_manager.store(self.operand)
        elif text == "MR":
            self.recall_memory(label)
        elif text == "MC":
            self.memory_manager.clear()
        elif text == "Mode":
            self.toggle_scientific_mode()
        else:
            self.append_operand(text, label)

    def reset(self):
        self.operand = ""
        self.app.root.ids.result_label.text = "0"

    def evaluate(self, label):
        result = MathProcessor.evaluate_expression(self.operand)
        self.operand = result if result != "Error" else ""
        label.text = result

    def recall_memory(self, label):
        self.operand += self.memory_manager.recall()
        label.text = self.operand

    def toggle_scientific_mode(self):
        self.scientific_mode = not self.scientific_mode
        self.update_buttons()

    def append_operand(self, text, label):
        if text in "+-*/" and (not self.operand or self.operand[-1] in "+-*/"):
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
        for btn in self.app.root.ids:
            if btn in scientific_buttons:
                self.app.root.ids[btn].opacity = 1 if self.scientific_mode else 0
                self.app.root.ids[btn].disabled = not self.scientific_mode