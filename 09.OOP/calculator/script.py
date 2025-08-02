import numpy as np

class BasicCalculator:
	def multiply(self, x, y):
		return np.multiply(x, y)

	def divide(self, x, y):
		return np.divide(x, y)

	def add(self, x, y):
		return np.add(x, y)

	def subtract(self, x, y):
		return np.subtract(x, y)
		

basic_calculator = BasicCalculator()
print(basic_calculator.divide(0.06, 12))

class FinancialCalculator(BasicCalculator):
	def calculate_monthly_interest_rate(self, annual_interest_rate):
		return self.divide(annual_interest_rate, 12)

financial_calculator = FinancialCalculator()
print(financial_calculator.calculate_monthly_interest_rate(0.06))