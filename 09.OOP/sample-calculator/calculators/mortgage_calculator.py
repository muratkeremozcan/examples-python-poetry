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