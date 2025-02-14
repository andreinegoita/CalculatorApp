import math
import cmath
import re

class MathProcessor:

    @staticmethod
    def prepare_expression(expression):
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

    @staticmethod
    def evaluate_expression(expression):
        try:
            prepared_expression = MathProcessor.prepare_expression(expression)
            return str(eval(prepared_expression))
        except Exception as e:
            print(f"Eroare la evaluare: {e}")
            return "Error"
