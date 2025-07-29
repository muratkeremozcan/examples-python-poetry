# Abstract Base Class is similar to Interface in TS, but it can also have concrete methods; that's the key difference


from abc import ABC, abstractmethod
from typing import Dict

class Company(ABC):
    @abstractmethod
    def create_budget(self, year: int, expenses: Dict[str, int]) -> None:
        pass

    def hire_employee(self, name: str) -> None:
        print(f'Welcome to the team {name}!')

# has to implement the abstract method, and inherits the concrete method
class Technology(Company):
    def __init__(self, name: str) -> None:
        self.name = name

    def create_budget(self, year: int, expenses: Dict[str, int]) -> None:
        for category, amount in expenses.items():
            print(f"{year} budget for {category} is {amount}")

t = Technology("Tina's tech advisors")
t.create_budget(2024, {"Salaries": 10000, "Supplies": 500})
t.hire_employee("Christian")

##########

class Company(ABC):
  @abstractmethod
  def pay_taxes(self, tax_rate: float) -> None:
    pass
  
  def report_revenue(self) -> None:
    print(f"{self.name} is reporting ${self.revenue} of revenue")

class Manufacturing(Company):
  def __init__(self, name: str, revenue: int):
    self.name = name
    self.revenue = revenue

  # Implement the pay_taxes() method
  def pay_taxes(self, tax_rate: float) -> None:
    tax_amount = self.revenue * tax_rate
    print(f"{self.name} is paying ${tax_amount} of taxes")	

m = Manufacturing("Morgan's Manufacturing", 5000)

m.pay_taxes(0.1)
m.report_revenue()
