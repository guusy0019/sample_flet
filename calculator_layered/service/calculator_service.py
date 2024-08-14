from usecase.calculate_use_case import CalculateUseCase

class CalculatorService:
    def __init__(self):
        self.use_case = CalculateUseCase()

    def handle_input(self, data, current_value):
        return self.use_case.execute(data, current_value)