from helper_functions import validate_email, validate_name, validate_password


def validate_user(name, email, password):
  if validate_name(name) == False:
    raise ValueError("Invalid name: Please enter a valid name.")

  if validate_email(email) == False:
    raise ValueError("Invalid email: Please enter a valid email address.")

  if validate_password(password) == False:
    raise ValueError("Invalid password: Please enter a valid password.")

  return True


def register_user(name, email, password):
  try:
    validate_user(name, email, password)

  except ValueError:  # specifically catching only ValueError exceptions
    return False

  return {"name": name, "email": email, "password": password}


print(
    register_user("", "somebody@example.com", "securePassword123")
)  # Expected output: False (invalid name)
# print('\\')
print(register_user("Alice", "alice@example.com", "pass1234"))
