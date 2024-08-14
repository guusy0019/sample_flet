class Calculator:
    def __init__(self):
        self.reset()

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True

    def calculate(self, operand1, operand2, operator):
        if operator == "+":
            return self.format_number(operand1 + operand2)
        elif operator == "-":
            return self.format_number(operand1 - operand2)
        elif operator == "*":
            return self.format_number(operand1 * operand2)
        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num
