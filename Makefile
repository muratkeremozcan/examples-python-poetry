.PHONY: check lint install format format-check
# type-check is disabled as per user preference

lint:
	venv/bin/python -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

check:
	find . -name "*.py" -type f -exec python -m py_compile {} +

# Type checking disabled - uncomment if needed later
# type-check:
#	venv/bin/python -m mypy --config-file=mypy.ini .

install:
	pip install -r requirements.txt

format:
	venv/bin/python -m autopep8 --in-place --recursive --indent-size=2 --aggressive --aggressive .
	venv/bin/python -m isort .

format-check:
	venv/bin/python -m autopep8 --diff --recursive --indent-size=2 --aggressive --aggressive .
	venv/bin/python -m isort . --check

all: install lint check format-check
# type-check removed from 'all' command
