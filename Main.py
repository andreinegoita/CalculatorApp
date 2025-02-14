from kivy.app import App
from kivy.lang import Builder

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
                # Evaluare expresie
                self.operand = str(eval(self.operand))
                label.text = self.operand
            except:
                label.text = "Error"
                self.operand = ""
        else:
            # Adăugăm spații pentru operatori (vizual mai clar)
            if text in "+-*/" and (self.operand == "" or self.operand[-1] in "+-*/"):
                return  # Evităm adăugarea a doi operatori consecutivi

            self.operand += text
            label.text = self.operand
            print(f"Apăsat: {text}, Operand: {self.operand}")


if __name__ == "__main__":
    CalculatorApp().run()
