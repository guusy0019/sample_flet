from entities.calculator import Calculator

class CalculateUseCase:
    def __init__(self):
        self.calculator = Calculator()

    def execute(self, data, current_value):
        if current_value == "Error" or data == "AC":
            self.calculator.reset()
            return "0"

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if current_value == "0" or self.calculator.new_operand:
                self.calculator.new_operand = False
                return data
            else:
                return current_value + data

        elif data in ("+", "-", "*", "/"):
            result = self.calculator.calculate(self.calculator.operand1, float(current_value), self.calculator.operator)
            self.calculator.operator = data
            self.calculator.operand1 = float(result) if result != "Error" else 0
            self.calculator.new_operand = True
            return result

        elif data == "=":
            result = self.calculator.calculate(self.calculator.operand1, float(current_value), self.calculator.operator)
            self.calculator.reset()
            return result

        elif data == "%":
            return str(float(current_value) / 100)

        elif data == "+/-":
            if float(current_value) > 0:
                return "-" + current_value
            elif float(current_value) < 0:
                return str(self.calculator.format_number(abs(float(current_value))))

        return current_value
