from financial_calculator import FinancialCalculator

class MortgageCalculator(FinancialCalculator):
	"""
    A class for calculating mortgage-related values.    
    Inherits from FinancialCalculator to utilize financial calculation methods.
    
    Attributes
    ----------
    loan_amount : float
        The total loan amount in dollars
    monthly_interest_rate : float
        The monthly interest rate (annual rate / 12)
    months : int
        The loan term in months (years * 12)
    """
	def __init__(self, loan_amount: float, annual_interest_rate: float, years: int):
		# t's a good habit to always call super().__init__() in init methods (future-proof in case the parent adds an init later)
		super().__init__() 
		self.loan_amount: float = loan_amount
		self.monthly_interest_rate: float = self.monthly_interest(annual_interest_rate)
		self.months: int = self.month_from_years(years)
		self.monthly_payment: float = self.calculate_monthly_payment()

	def calculate_monthly_payment(self):
		numerator: float = self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** self.months
		denominator: float = (1 + self.monthly_interest_rate) ** self.months - 1
		multiplier: float = self.divide(numerator, denominator)
		monthly_payment: float = round(self.multiply(self.loan_amount, multiplier), 2)	
		return monthly_payment

# use help(...object...) to get documentation
# use dir(...object...) to get list of attributes and methods
# print(help(FinancialCalculator))
# print(dir(FinancialCalculator))


  
mortgage_calculator = MortgageCalculator(300000, 0.059, 10)
print(f"Your monthly mortgage payment is ${round(mortgage_calculator.monthly_payment, 2)}.")
