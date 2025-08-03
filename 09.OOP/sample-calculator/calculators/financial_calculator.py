from basic_calculator import BasicCalculator

class FinancialCalculator(BasicCalculator):
	def monthly_interest_rate(self, annual_interest_rate):
		return self.divide(annual_interest_rate, 12)

	def month_from_years(self, years):
		return self.multiply(years, 12)
