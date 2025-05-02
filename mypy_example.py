from typing import Dict, List, Optional


def greet(name: str) -> str:
  """Return a greeting for the given name."""
  return f"Hello, {name}!"


def calculate_total(prices: List[float], quantities: List[int]) -> float:
  """Calculate the total price."""
  if len(prices) != len(quantities):
    raise ValueError("Prices and quantities must have the same length")

  total: float = 0.0
  for price, quantity in zip(prices, quantities):
    total += price * quantity

  return total


def find_user(
    users: Dict[str, Dict[str, str]], user_id: str
) -> Optional[Dict[str, str]]:
  """Find a user by ID."""
  return users.get(user_id)


# Example usage
if __name__ == "__main__":
  # This is correct usage
  message = greet("World")
  print(message)

  # This would be caught by mypy if uncommented:
  # bad_message = greet(123)  # Type error: 123 is not a string

  prices = [10.5, 20.75, 5.0]
  quantities = [2, 1, 3]

  total = calculate_total(prices, quantities)
  print(f"Total: ${total:.2f}")

  # This would be caught by mypy if uncommented:
  # bad_total = calculate_total(prices, ["2", "1", "3"])  # Type error:
  # string is not an int
