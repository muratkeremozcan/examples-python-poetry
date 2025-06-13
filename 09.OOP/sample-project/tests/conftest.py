# Pytest automatically discovers this file and makes fixtures available to all tests.
# Fixtures defined here can be used in any test file without explicit imports.

import os
import pytest
import pandas as pd

# Ensure the project root is in the Python path
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prepare_smartphone_data import prepare_smartphone_data

# Get the path to the test data file
def get_data_path():
    """Helper function to get the path to the test data file."""
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data",
        "smartphones.csv"
    )

@pytest.fixture
def clean_smartphone_data():
    """Fixture to load and clean smartphone data."""
    data_path = get_data_path()
    return prepare_smartphone_data(data_path)
